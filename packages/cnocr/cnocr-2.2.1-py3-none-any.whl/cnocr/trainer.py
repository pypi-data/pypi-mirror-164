# coding: utf-8
# Copyright (C) 2021, [Breezedeus](https://github.com/breezedeus).
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import logging
from copy import deepcopy
from pathlib import Path
from typing import Any, Optional, Union, List

import numpy as np
import torch
import torch.optim as optim
from torch import nn
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor

from .lr_scheduler import get_lr_scheduler


logger = logging.getLogger(__name__)


def get_optimizer(name: str, model, learning_rate, weight_decay):
    r"""Init the Optimizer

    Returns:
        torch.optim: the optimizer
    """
    OPTIMIZERS = {
        'adam': optim.Adam,
        'adamw': optim.AdamW,
        'sgd': optim.SGD,
        'adagrad': optim.Adagrad,
        'rmsprop': optim.RMSprop,
    }

    try:
        opt_cls = OPTIMIZERS[name.lower()]
        optimizer = opt_cls(
            model.parameters(), lr=learning_rate, weight_decay=weight_decay
        )
    except:
        logger.warning('Received unrecognized optimizer, set default Adam optimizer')
        optimizer = optim.Adam(
            model.parameters(), lr=learning_rate, weight_decay=weight_decay
        )
    return optimizer


class Accuracy(object):
    @classmethod
    def complete_match(cls, labels: List[List[str]], preds: List[List[str]]):
        assert len(labels) == len(preds)
        total_num = len(labels)
        hit_num = 0
        for label, pred in zip(labels, preds):
            if label == pred:
                hit_num += 1

        return hit_num / (total_num + 1e-6)

    @classmethod
    def label_match(cls, labels: List[List[str]], preds: List[List[str]]):
        assert len(labels) == len(preds)
        total_num = 0
        hit_num = 0
        for label, pred in zip(labels, preds):
            total_num += max(len(label), len(pred))
            min_len = min(len(label), len(pred))
            hit_num += sum([l == p for l, p in zip(label[:min_len], pred[:min_len])])

        return hit_num / (total_num + 1e-6)


class WrapperLightningModule(pl.LightningModule):
    def __init__(self, config, model):
        super().__init__()
        self.config = config
        self.model = model
        self._optimizer = get_optimizer(
            config['optimizer'],
            self.model,
            config['learning_rate'],
            config.get('weight_decay', 0),
        )

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        if hasattr(self.model, 'set_current_epoch'):
            self.model.set_current_epoch(self.current_epoch)
        else:
            setattr(self.model, 'current_epoch', self.current_epoch)
        res = self.model.calculate_loss(batch)

        # update lr scheduler
        sch = self.lr_schedulers()
        sch.step()

        losses = res['loss']
        self.log(
            'train_loss',
            losses.item(),
            on_step=True,
            on_epoch=True,
            prog_bar=True,
            logger=True,
        )
        return losses

    def validation_step(self, batch, batch_idx):
        if hasattr(self.model, 'validation_step'):
            return self.model.validation_step(batch, batch_idx, self)

        res = self.model.calculate_loss(
            batch, return_model_output=True, return_preds=True
        )
        losses = res['loss']
        preds, _ = zip(*res['preds'])
        val_metrics = {'val_loss': losses.item()}

        labels_list = batch[2]
        val_metrics['complete_match'] = Accuracy.complete_match(labels_list, preds)
        val_metrics['label_match'] = Accuracy.label_match(labels_list, preds)

        # 过滤掉NaN的指标。有些指标在某些batch数据上会出现结果NaN，比如batch只有正样本或负样本时，AUC=NaN
        val_metrics = {k: v for k, v in val_metrics.items() if not np.isnan(v)}
        self.log_dict(
            val_metrics, on_step=True, on_epoch=True, prog_bar=True, logger=True,
        )
        return losses

    def configure_optimizers(self):
        return [self._optimizer], [get_lr_scheduler(self.config, self._optimizer)]


class PlTrainer(object):
    """
    封装 PyTorch Lightning 的训练器。
    """

    def __init__(self, config, ckpt_fn=None):
        self.config = config

        lr_monitor = LearningRateMonitor(logging_interval='step')
        callbacks = [lr_monitor]

        mode = self.config.get('pl_checkpoint_mode', 'min')
        monitor = self.config.get('pl_checkpoint_monitor')
        fn_fields = ckpt_fn or []
        fn_fields.append('{epoch:03d}')
        if monitor:
            fn_fields.append('{' + monitor + ':.4f}')
            checkpoint_callback = ModelCheckpoint(
                monitor=monitor,
                mode=mode,
                filename='-'.join(fn_fields),
                save_last=True,
                save_top_k=5,
            )
            callbacks.append(checkpoint_callback)

        self.pl_trainer = pl.Trainer(
            limit_train_batches=self.config.get('limit_train_batches', 1.0),
            limit_val_batches=self.config.get('limit_val_batches', 1.0),
            gpus=self.config.get('gpus'),
            max_epochs=self.config.get('epochs', 20),
            precision=self.config.get('precision', 32),
            callbacks=callbacks,
            stochastic_weight_avg=False,
        )

    def fit(
        self,
        model: nn.Module,
        train_dataloader: Any = None,
        val_dataloaders: Optional[Union[DataLoader, List[DataLoader]]] = None,
        datamodule: Optional[pl.LightningDataModule] = None,
        resume_from_checkpoint: Optional[Union[Path, str]] = None,
    ):
        r"""
        Runs the full optimization routine.

        Args:
            model: Model to fit.

            train_dataloader: Either a single PyTorch DataLoader or a collection of these
                (list, dict, nested lists and dicts). In the case of multiple dataloaders, please
                see this :ref:`page <multiple-training-dataloaders>`
            val_dataloaders: Either a single Pytorch Dataloader or a list of them, specifying validation samples.
                If the model has a predefined val_dataloaders method this will be skipped
            datamodule: A instance of :class:`LightningDataModule`.
            resume_from_checkpoint: Path/URL of the checkpoint from which training is resumed. If there is
                no checkpoint file at the path, start from scratch. If resuming from mid-epoch checkpoint,
                training will start from the beginning of the next epoch.
        """
        steps_per_epoch = (
            len(train_dataloader)
            if train_dataloader is not None
            else len(datamodule.train_dataloader())
        )
        self.config['steps_per_epoch'] = steps_per_epoch
        if resume_from_checkpoint is not None:
            pl_module = WrapperLightningModule.load_from_checkpoint(
                resume_from_checkpoint, config=self.config, model=model
            )
            self.pl_trainer = pl.Trainer(resume_from_checkpoint=resume_from_checkpoint)
        else:
            pl_module = WrapperLightningModule(self.config, model)

        self.pl_trainer.fit(pl_module, train_dataloader, val_dataloaders, datamodule)

        fields = self.pl_trainer.checkpoint_callback.best_model_path.rsplit(
            '.', maxsplit=1
        )
        fields[0] += '-model'
        output_model_fp = '.'.join(fields)
        resave_model(
            self.pl_trainer.checkpoint_callback.best_model_path, output_model_fp
        )
        self.saved_model_file = output_model_fp


def resave_model(module_fp, output_model_fp, map_location=None):
    """PlTrainer存储的文件对应其 `pl_module` 模块，需利用此函数转存为 `model` 对应的模型文件。"""
    checkpoint = torch.load(module_fp, map_location=map_location)
    state_dict = {}
    if all([k.startswith('model.') for k in checkpoint['state_dict'].keys()]):
        for k, v in checkpoint['state_dict'].items():
            state_dict[k.split('.', maxsplit=1)[1]] = v
    torch.save({'state_dict': state_dict}, output_model_fp)
