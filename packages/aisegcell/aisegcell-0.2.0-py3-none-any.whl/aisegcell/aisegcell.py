######################################################################################################################
# This script coordinates training and testing of cell segmentation with Pytorch Lightning                           #
# Author:               Melinda Kondorosy, Daniel Schirmacher                                                        #
#                       Cell Systems Dynamics Group, D-BSSE, ETH Zurich                                              #
# Python Version:       3.8.6                                                                                        #
# PyTorch Version:      1.7.1                                                                                        #
# PyTorch Lightning Version: 1.5.9                                                                                   #
######################################################################################################################
import argparse
import os
import random
import re
from datetime import date
from typing import List, Tuple

import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import CSVLogger

from aisegcell.models.unet import LitUnet
from aisegcell.utils.callbacks import CheckpointCallback
from aisegcell.utils.datamodule import DataModule


def train():
    """
    Main function to train Unet with argparse arguments.

    """
    # get user input
    desc = "Program to train a Unet for cell segmentation."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to CSV file containing training image file paths.",
    )

    parser.add_argument(
        "--data_val",
        type=str,
        required=True,
        help="Path to CSV file containing validation image file paths.",
    )

    parser.add_argument(
        "--output_base_dir",
        type=str,
        required=True,
        help="Path to output directory.",
    )

    parser.add_argument(
        "--model",
        type=str,
        default="Unet",
        help="Model type to train. Default is Unet",
    )

    parser.add_argument(
        "--checkpoint",
        type=str,
        default=None,
        help="Path to checkpoint file of trained pl.LightningModule. Default is None.",
    )

    parser.add_argument(
        "--devices",
        type=str,
        nargs="+",
        default=["cpu"],
        help='Devices to use for model training. Can be GPU IDs as in default or "cpu". Default is "cpu".',
    )

    parser.add_argument(
        "--epochs",
        type=int,
        default=5,
        help="Number of training epochs. Default is 5.",
    )

    parser.add_argument(
        "--batch_size",
        type=int,
        default=2,
        help="Number of samples per mini-batch. Default is 2.",
    )

    parser.add_argument(
        "--lr",
        type=float,
        default=1e-4,
        help="Learning rate of the optimizer. Default is 1e-4.",
    )

    parser.add_argument(
        "--base_filters",
        type=int,
        default=32,
        help="Number of base_filters of Unet.Default is 32.",
    )

    parser.add_argument(
        "--shape",
        type=int,
        nargs="+",
        default=[1024, 1024],
        help="Shape [heigth, width] that all images will be cropped/padded to before Unet submission. Default is [1024,1024].",
    )

    parser.add_argument(
        "--receptive_field",
        type=int,
        default=128,
        help="Receptive field of an neuron in the deepest layer.Default is 128.",
    )

    parser.add_argument(
        "--log_frequency",
        type=int,
        default=50,
        help="Log performance metrics every N gradient steps during training. Default is 50.",
    )

    parser.add_argument(
        "--loss_weight",
        type=float,
        default=1.0,
        help="Weight of the foreground class compared to the background class for the binary cross entropy loss. Default is 1.",
    )

    parser.add_argument(
        "--bilinear",
        action="store_true",
        help="If flag is used, use bilinear upsampling, else transposed convolutions.",
    )

    # set default to false
    parser.add_argument(
        "--multiprocessing",
        action="store_true",
        help="If flag is used, all GPUs given in devices will be used for traininig/inference. Does not support CPU.",
    )

    parser.add_argument(
        "--retrain",
        action="store_true",
        help="If flag is used, best scores for model saving will be reset (required for training on new data).",
    )

    parser.add_argument(
        "--transform_intensity",
        action="store_true",
        help="If flag is used random intensity transformations will be applied to image.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="None or Int to use for random seeding. Default is None.",
    )

    args = parser.parse_args()

    data = args.data
    data_val = args.data_val
    model = args.model
    checkpoint = args.checkpoint
    devices = args.devices
    output_base_dir = args.output_base_dir
    epochs = args.epochs
    batch_size = args.batch_size
    lr = args.lr
    base_filters = args.base_filters
    shape = tuple(args.shape)
    receptive_field = args.receptive_field
    log_frequency = args.log_frequency

    bilinear = args.bilinear
    multiprocessing = args.multiprocessing
    retrain = args.retrain
    transform_intensity = args.transform_intensity
    seed = args.seed
    loss_weight = args.loss_weight

    assert (
        min(shape) >= receptive_field
    ), "min(shape) >= receptive_field is required."

    # create directories
    d = date.today()
    identifier = (
        str(d.year)[2:]
        + str(d.month).zfill(2)
        + str(d.day).zfill(2)
        + "_"
        + args.model
    )
    rnd_id = str(random.getrandbits(15)).zfill(5)

    while os.path.exists(
        os.path.join(args.output_base_dir, f"{identifier}_{rnd_id}")
    ):
        rnd_id = str(random.getrandbits(15)).zfill(5)

    identifier += f"_{rnd_id}"

    output_base_dir = os.path.join(output_base_dir, identifier)
    os.makedirs(output_base_dir, exist_ok=True)

    del d, rnd_id

    # ensure compatibility of devices with $CUDA_VISIBLE_DEVICES input
    if len(devices) == 1 and "," in devices[0]:
        devices = devices[0].split(",")

    if "cpu" in devices:
        accelerator = "cpu"
        gpus = None
        strategy = None
        sync_batchnorm = False
        num_processes = 1  # NOTE: currently not intended to support multi-process CPU training
    else:
        accelerator = "gpu"
        gpus = [int(device) for device in devices]
        num_processes = len(gpus)

    # assert correct setup for multiprocessing
    if multiprocessing:
        assert (
            accelerator == "gpu"
        ), "multiprocessing is only enabled for GPU devices."
        assert (
            len(gpus) > 1
        ), f"multiprocessing requires >1 devices, but {len(gpus)} devices are provided."

        # NOTE: currently only single node training supported (else -> batch_size / (ngpus * nnodes))
        batch_size = int(batch_size / len(gpus))
        sync_batchnorm = True  # set sync_batchnorm for multiprocessing
        strategy = "ddp"
    elif accelerator == "gpu":
        gpus = 1
        strategy = None
        num_processes = 1
        sync_batchnorm = False

    # set up data
    data_module = DataModule(
        path_data=data,
        path_data_val=data_val,
        batch_size=batch_size,
        shape=shape,
        transform_intensity=transform_intensity,
    )

    # random seeding
    if seed is not None:
        pl.seed_everything(seed, workers=True)
    # not functioning due to bilinear
    #     deterministic = True
    # else:
    #     deterministic = False

    # load model
    if model == "Unet":
        model = LitUnet(
            base_filters=base_filters,
            bilinear=bilinear,
            receptive_field=receptive_field,
            learning_rate=lr,
            loss_weight=loss_weight,
        )
    else:
        raise ValueError(f'model type "{model}" is not implemented.')
    # if checkpoint is None:
    # else:
    #     if os.path.isfile(checkpoint):
    #         model = LitUnet.load_from_checkpoint(checkpoint)
    #     else:
    #         raise FileNotFoundError(f'The file "{checkpoint}" does not exist.')

    # set up callback for best model
    checkpoint_best_loss = ModelCheckpoint(
        monitor="loss_val",
        filename="best-loss-{epoch}-{step}",
        mode="min",
    )

    checkpoint_best_f1 = ModelCheckpoint(
        monitor="f1",
        filename="best-f1-{epoch}-{step}",
        mode="max",
    )

    checkpoint_best_iou = ModelCheckpoint(
        monitor="iou",
        filename="best-iou-{epoch}-{step}",
        mode="max",
    )

    # callback for latest model
    checkpoint_latest = ModelCheckpoint(
        monitor=None,
        filename="latest-{epoch}-{step}",
        mode="max",
        save_top_k=1,
    )

    # update max_epoch when loading from checkpoint
    if checkpoint is not None:
        epoch_pattern = re.compile(r"epoch=([0-9]+)")
        old_epoch = int(epoch_pattern.search(checkpoint)[1])
        epochs += old_epoch

    # train model
    logger = CSVLogger(output_base_dir, name="lightning_logs")
    trainer = pl.Trainer(
        max_epochs=epochs,
        default_root_dir=output_base_dir,
        accelerator=accelerator,
        gpus=gpus,
        strategy=strategy,
        num_processes=num_processes,
        # deterministic=deterministic,
        logger=logger,
        callbacks=[
            checkpoint_best_loss,
            checkpoint_best_f1,
            checkpoint_best_iou,
            checkpoint_latest,
            CheckpointCallback(retrain=retrain),
        ],
        sync_batchnorm=sync_batchnorm,
        log_every_n_steps=log_frequency,
        # num_nodes = nnodes, # NOTE: currently not supported
    )
    trainer.fit(model, data_module, ckpt_path=checkpoint)


def _args_inference():
    """
    Receive user input for inference.

    """
    # get user input
    desc = "Program to test/predict Unet for cell segmentation."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to CSV file containing test image file paths.",
    )

    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Path to checkpoint file of trained pl.LightningModule.",
    )

    parser.add_argument(
        "--output_base_dir",
        type=str,
        required=True,
        help="Path to output directory.",
    )

    parser.add_argument(
        "--suffix",
        type=str,
        default="",
        help="Suffix to append to all mask file names.",
    )

    parser.add_argument(
        "--devices",
        type=str,
        nargs="+",
        default=["cpu"],
        help='Devices to use for model training. Can be GPU IDs as in default or "cpu".',
    )

    return parser.parse_args()


def _initialise_inferrence(
    data: str,
    model: str,
    devices: List[str],
    output_base_dir: str,
    suffix: str,
    napari: bool = False,
) -> Tuple[pl.Trainer, pl.LightningModule, pl.LightningDataModule]:
    """
    Construct trainer, model, and data module for testing/predicting
    """
    os.makedirs(output_base_dir, exist_ok=True)

    # ensure compatibility of devices with $CUDA_VISIBLE_DEVICES input
    if len(devices) == 1 and "," in devices[0]:
        devices = devices[0].split(",")

    if "cpu" in devices:
        accelerator = "cpu"
        gpus = None
    else:
        accelerator = "gpu"
        gpus = [int(device) for device in devices]
        gpus = gpus[:1]  # test only on one gpu

    # load model
    if os.path.isfile(model):
        model = LitUnet.load_from_checkpoint(model)
        model.suffix = suffix
        model.napari = napari
    else:
        raise FileNotFoundError(f'The file "{model}" does not exist.')

    # set up data
    data_module = DataModule(
        path_data=data,
        path_data_val=data,
        path_data_test=data,
        path_data_predict=data,
        batch_size=1,
    )

    # test model
    logger = CSVLogger(output_base_dir, name="lightning_logs")
    trainer = pl.Trainer(
        default_root_dir=output_base_dir,
        accelerator=accelerator,
        gpus=gpus,
        logger=logger,
    )

    return trainer, model, data_module


def test(
    data: str,
    model: str,
    devices: List[str],
    output_base_dir: str,
    suffix: str,
) -> None:
    """
    Run model testing.
    """
    trainer, model, data_module = _initialise_inferrence(
        data=data,
        model=model,
        devices=devices,
        output_base_dir=output_base_dir,
        suffix=suffix,
    )
    trainer.test(model, data_module)


def predict(
    data: str,
    model: str,
    devices: List[str],
    output_base_dir: str,
    suffix: str,
    napari: bool = False,
) -> None:
    """
    Run model prediction.
    """
    trainer, model, data_module = _initialise_inferrence(
        data=data,
        model=model,
        devices=devices,
        output_base_dir=output_base_dir,
        suffix=suffix,
        napari=napari,
    )
    trainer.predict(model, data_module)


def test_cli():
    """
    CLI wrapper for test().
    """
    args = _args_inference()

    data = args.data
    model = args.model
    suffix = args.suffix
    devices = args.devices
    output_base_dir = args.output_base_dir

    test(
        data=data,
        model=model,
        devices=devices,
        output_base_dir=output_base_dir,
        suffix=suffix,
    )


def predict_cli():
    """
    CLI wrapper for predict().
    """
    args = _args_inference()

    data = args.data
    model = args.model
    suffix = args.suffix
    devices = args.devices
    output_base_dir = args.output_base_dir

    predict(
        data=data,
        model=model,
        devices=devices,
        output_base_dir=output_base_dir,
        suffix=suffix,
    )
