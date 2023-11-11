# -*- coding: utf-8 -*-
import os
import warnings
from typing import Union

import pandas as pd
from qa4sm_reader.plotter import QA4SMPlotter
from qa4sm_reader.img import QA4SMImg, extract_periods
import qa4sm_reader.globals as globals


def plot_all(filepath: str,
             metrics: list = None,
             extent: tuple = None,
             out_dir: str = None,
             out_type: str = 'png',
             save_all: bool = True,
             save_metadata: Union[str, bool] = 'never',
             save_csv: bool = True,
             engine: str = 'h5netcdf',
             **plotting_kwargs) -> tuple:
    """
    Creates boxplots for all metrics and map plots for all variables.
    Saves the output in a folder-structure.

    Parameters
    ----------
    filepath : str
        path to the *.nc file to be processed.
    metrics : set or list, optional (default: None)
        metrics to be plotted. If None, all metrics with data are plotted
    extent : tuple, optional (default: None)
        Area to subset the values for -> (min_lon, max_lon, min_lat, max_lat)
    out_dir : str, optional (default: None)
        Path to output generated plot. If None, defaults to the current working directory.
    out_type: str or list
        extensions which the files should be saved in
    save_all: bool, optional (default: True)
        all plotted images are saved to the output directory
    save_metadata: str or bool, optional (default: 'never')
        for each metric, metadata plots are provided
        (see plotter.QA4SMPlotter.plot_save_metadata)
        - 'never' or False: No metadata plots are created
        - 'always': Metadata plots are always created for all metrics
                   (set the meta_boxplot_min_size to 0)
        - 'threshold' or True: Metadata plots are only created if the number
                               of points is above the `meta_boxplot_min_size`
                               threshold from globals.py. Otherwise a warning
                               is printed.
    save_csv: bool, optional. Default is True.
        save a .csv file with the validation statistics
    engine: str, optional (default: h5netcdf)
        Engine used by xarray to read data from file. For qa4sm this should
        be h5netcdf.
    plotting_kwargs: arguments for plotting functions.

    Returns
    -------
    fnames_boxplots: list
    fnames_mapplots: list
        lists of filenames for created mapplots and boxplots
    fnames_csv: list
    """
    if isinstance(save_metadata, bool):
        if not save_metadata:
            save_metadata = 'never'
        else:
            save_metadata = 'threshold'
    save_metadata = save_metadata.lower()

    _options = ['never', 'always', 'threshold']
    if save_metadata not in _options:
        raise ValueError(f"save_metadata must be one of: "
                         f"{', '.join(_options)} "
                         f"but `{save_metadata}` was passed.")

    # initialise image and plotter
    fnames_bplot, fnames_mapplot, fnames_csv = [], [], []
    periods = extract_periods(filepath)
    for period in periods:
        img = QA4SMImg(
            filepath,
            period=period,
            extent=extent,
            ignore_empty=True,
            engine=engine,
        )
        plotter = QA4SMPlotter(
            image=img,
            out_dir=os.path.join(out_dir, str(period)) if period else out_dir)

        if metrics is None:
            metrics = img.metrics

        # iterate metrics and create files in output directory
        for metric in metrics:
            metric_bplots, metric_mapplots = plotter.plot_metric(
                metric=metric,
                out_types=out_type,
                save_all=save_all,
                **plotting_kwargs)
            # there can be boxplots with no mapplots
            if metric_bplots:
                fnames_bplot.extend(metric_bplots)
            if metric_mapplots:
                fnames_mapplot.extend(metric_mapplots)
            if img.metadata and (save_metadata != 'never'):
                if save_metadata == 'always':
                    kwargs = {
                        'meta_boxplot_min_samples': 0
                    }
                else:
                    kwargs = {
                        'meta_boxplot_min_samples': globals.meta_boxplot_min_samples
                    }

                fnames_bplot.extend(
                    plotter.plot_save_metadata(
                        metric,
                        out_types=out_type,
                        **kwargs
                    ))


        if save_csv:
            out_csv = plotter.save_stats()
            fnames_csv.append(out_csv)

    return fnames_bplot, fnames_mapplot, fnames_csv


def get_img_stats(
    filepath: str,
    extent: tuple = None,
) -> pd.DataFrame:
    """
    Creates a dataframe containing summary statistics for each metric

    Parameters
    ----------
    filepath : str
        path to the *.nc file to be processed.
    extent : list
        list(x_min, x_max, y_min, y_max) to create a subset of the values

    Returns
    -------
    table : pd.DataFrame
        Quick inspection table of the results.
    """
    img = QA4SMImg(filepath, extent=extent, ignore_empty=True)
    table = img.stats_df()

    return table
