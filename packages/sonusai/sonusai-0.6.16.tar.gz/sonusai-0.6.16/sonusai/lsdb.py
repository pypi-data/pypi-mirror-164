"""sonusai lsdb

usage: lsdb [-ht] [-i MIXID] [-c TID] MIXDB

Options:
    -h, --help
    -i MIXID, --mixid MIXID         Mixture ID to generate and analyze.
    -c TID, --truth_index TID       Analyze mixtures that contain this truth index.
    -t, --targets                   List all target files.

List mixture data information from a SonusAI mixture database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file or an HDF5 file containing a SonusAI mixture database.
                The HDF5 file contains:
                    attribute:  mixdb
                    dataset:    feature (optional)
                    dataset:    truth_f (optional)

"""
from typing import Union

import numpy as np

from sonusai import logger
from sonusai.mixture import MixtureDatabase


def lsdb(mixdb: MixtureDatabase,
         mixid: int = None,
         feature: Union[np.ndarray, None] = None,
         truth_f: Union[np.ndarray, None] = None,
         truth_index: Union[int, None] = None,
         list_targets: bool = False) -> None:
    from sonusai import SonusAIError
    from sonusai.mixture import SAMPLE_RATE
    from sonusai.mixture import get_feature_stats
    from sonusai.mixture import get_truth_indices_for_target
    from sonusai.queries import get_mixids_from_truth_index
    from sonusai.utils import print_class_count
    from sonusai.utils import print_mixture_details
    from sonusai.utils import seconds_to_hms

    desc_len = 24

    if feature is not None:
        logger.info(f'Feature shape {feature.shape}')

    if truth_f is not None:
        logger.info(f'Truth shape   {truth_f.shape}')

    if feature is not None and truth_f is not None:
        f_frames = feature.shape[0]
        t_frames = truth_f.shape[0]
        if f_frames != t_frames:
            logger.warn(f'Number of feature frames, {f_frames} does not match number of truth frames, {t_frames}.')

    total_samples = sum([sub.samples for sub in mixdb.mixtures])
    total_duration = total_samples / SAMPLE_RATE
    fs = get_feature_stats(feature_mode=mixdb.feature,
                           frame_size=mixdb.frame_size,
                           num_classes=mixdb.num_classes,
                           truth_mutex=mixdb.truth_mutex)

    logger.info(f'{"Mixtures":{desc_len}} {len(mixdb.mixtures)}')
    logger.info(f'{"Duration":{desc_len}} {seconds_to_hms(seconds=total_duration)}')
    logger.info(f'{"Targets":{desc_len}} {len(mixdb.targets)}')
    logger.info(f'{"Target augmentations":{desc_len}} {len(mixdb.target_augmentations)}')
    logger.info(f'{"Noise augmentations":{desc_len}} {len(mixdb.noise_augmentations)}')
    logger.info(f'{"Noises":{desc_len}} {len(mixdb.noises)}')
    logger.info(f'{"Feature":{desc_len}} {mixdb.feature}')
    logger.info(f'{"Feature shape":{desc_len}} {fs.stride} x {fs.num_bands} ({fs.stride * fs.num_bands} total params)')
    logger.info(f'{"Feature samples":{desc_len}} {fs.feature_samples} samples ({fs.feature_ms} ms)')
    logger.info(f'{"Feature step samples":{desc_len}} {fs.feature_step_samples} samples ({fs.feature_step_ms} ms)')
    logger.info(f'{"Feature overlap":{desc_len}} {fs.step / fs.stride} ({fs.feature_step_ms} ms)')
    logger.info(f'{"SNRs":{desc_len}} {mixdb.snrs}')
    logger.info(f'{"Classes":{desc_len}} {mixdb.num_classes}')
    logger.info(f'{"Truth mutex":{desc_len}} {mixdb.truth_mutex}')
    print_class_count(record=mixdb, length=desc_len)
    # TBD add class weight calculations here
    logger.info('')

    if list_targets:
        logger.info('Target details:')
        idx_len = int(np.ceil(np.log10(len(mixdb.targets))))
        for idx, target in enumerate(mixdb.targets):
            desc = f'  {idx:{idx_len}} Name'
            logger.info(f'{desc:{desc_len}} {target.name}')
            desc = f'  {idx:{idx_len}} Truth index'
            logger.info(f'{desc:{desc_len}} {get_truth_indices_for_target(target)}')
        logger.info('')

    if truth_index is not None:
        if 0 <= truth_index > mixdb.num_classes:
            raise SonusAIError(f'Given truth_index is outside valid range of 1-{mixdb.num_classes}')
        ids = get_mixids_from_truth_index(mixdb=mixdb, predicate=lambda x: x in [truth_index])[truth_index]
        logger.info(f'Mixtures with truth index {truth_index}: {ids}')
        logger.info('')

    print_mixture_details(mixdb=mixdb, mixid=mixid, desc_len=desc_len, print_fn=logger.info, all_class_counts=True)


def main():
    import os

    import h5py
    from docopt import docopt

    import sonusai
    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.mixture import load_mixdb
    from sonusai.utils import human_readable_size
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    mixdb_name = args['MIXDB']
    mixid = args['--mixid']
    truth_index = args['--truth_index']
    list_targets = args['--targets']

    if mixid is not None:
        mixid = int(mixid)

    if truth_index is not None:
        truth_index = int(truth_index)

    log_name = 'lsdb.log'
    create_file_handler(log_name)
    update_console_handler(False)
    initial_log_messages('lsdb')

    logger.info(f'Analyzing {mixdb_name} ({human_readable_size(os.path.getsize(mixdb_name), 1)})')

    mixdb = load_mixdb(name=mixdb_name)

    feature = None
    truth_f = None
    if h5py.is_hdf5(mixdb_name):
        with h5py.File(mixdb_name, 'r') as f:
            if 'feature' in f.keys():
                feature = np.array(f['/feature'])
            if 'truth_f' in f.keys():
                truth_f = np.array(f['/truth_f'])

    lsdb(mixdb=mixdb,
         mixid=mixid,
         feature=feature,
         truth_f=truth_f,
         truth_index=truth_index,
         list_targets=list_targets)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
