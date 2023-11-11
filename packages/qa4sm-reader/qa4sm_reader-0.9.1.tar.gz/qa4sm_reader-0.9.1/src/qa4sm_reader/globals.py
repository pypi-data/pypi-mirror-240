# -*- coding: utf-8 -*-
"""
Settings and global variables used in the reading and plotting procedures
"""
# todo: reduce dependency on globals (e.g flexible if new datasets/versions are added)
import warnings

import cartopy.crs as ccrs
import matplotlib.colors as cl
import matplotlib.pyplot as plt

# PLOT DEFAULT SETTINGS
# =====================================================
matplotlib_ppi = 72  # Don't change this, it's a matplotlib convention.
index_names = ['lat', 'lon',
               'gpi']  # Names used for 'latitude' and 'longitude' coordinate.
time_name = 'time'  # not used at the moment, dropped on load
period_name = 'period'  # not used at the moment, dropped on load

dpi_min = 100  # Resolution in which plots are going to be rendered.
dpi_max = 200
title_pad = 12.0  # Padding below the title in points. default padding is matplotlib.rcParams['axes.titlepad'] = 6.0
data_crs = ccrs.PlateCarree()  # Default map projection. use one of

# === map plot defaults ===
scattered_datasets = [
    'ISMN'
]  # dataset names which require scatterplots (values is scattered in lat/lon)
map_figsize = [11.32, 6.10]  # size of the output figure in inches.
naturalearth_resolution = '110m'  # One of '10m', '50m' and '110m'. Finer resolution slows down plotting. see https://www.naturalearthdata.com/
crs = ccrs.PlateCarree(
)  # projection. Must be a class from cartopy.crs. Note, that plotting labels does not work for most projections.
markersize = 4  # diameter of Marker in points.
map_pad = 0.15  # padding relative to map height.
grid_intervals = [
    2, 5, 10, 30
]  # grid spacing in degree to choose from (plotter will try to make 5 gridlines in the smaller dimension)
max_title_len = 8 * map_figsize[
    0]  # maximum length of plot title in chars. if longer, it will be broken in multiple lines.

# === boxplot_basic defaults ===
boxplot_printnumbers = True  # Print 'median', 'nObs', 'stdDev' to the boxplot_basic.
boxplot_height = 6
boxplot_width = 2.1  # times (n+1), where n is the number of boxes.
boxplot_title_len = 8 * boxplot_width  # times the number of boxes. maximum length of plot title in chars.
tick_size = 8.5

# === watermark defaults ===
watermark = u'made with QA4SM (qa4sm.eu)'  # Watermark string
watermark_pos = 'bottom'  # Default position ('top' or 'bottom' or None)
watermark_fontsize = 8  # fontsize in points (matplotlib uses 72ppi)
watermark_pad = 5  # padding above/below watermark in points (matplotlib uses 72ppi)

# === filename template ===
ds_fn_templ = "{i}-{ds}.{var}"
ds_fn_sep = "_with_"

# === metadata files to save ===
out_metadata_plots = {
    "lc": ["lc_2010"],
    "climate": ["climate_KG"],
    "soil": ["instrument_depth", "soil_type"],
    "frm_class": ['frm_class'],
}

# === calculation errors (pytesmo) === #TODO: import from pytesmo
status = {
    -1: 'Other error',
    0: 'Success',
    1: 'Not enough data',
    2: 'Metric calculation failed',
    3: 'Temporal matching failed',
    4: 'No overlap for temporal match',
    5: 'Scaling failed',
    6: 'Unexpected validation error',
    7: 'Missing GPI data',
    8: 'Data reading failed'
}

# helper dict to replace some error codes and have merged categories
# (e.g.: No overlap for temporal match -> Temporal matching failed)
status_replace = {
    4: 3,
    7: 1,
}

# === colormaps used for plotting metrics ===
# Colormaps can be set for classes of similar metrics or individually for metrics.
# Any colormap name can be used, that works with matplotlib.pyplot.cm.get_cmap('colormap')
# more on colormaps: https://matplotlib.org/users/colormaps.html | https://morphocode.com/the-use-of-color-in-maps/


def get_status_colors():
    # function to get custom cmap for calculation errors
    # limited to 14 different error entries to produce distinct colors
    cmap = plt.cm.get_cmap('Set3', len(status) - 2)
    colors = [cmap(i) for i in range(cmap.N)]
    colors.insert(0, (0, 0.66666667, 0.89019608, 1.0))
    colors.insert(0, (0.45882353, 0.08235294, 0.11764706, 1.0))
    cmap = cl.ListedColormap(colors=colors)
    return cmap


_cclasses = {
    'div_better': plt.cm.get_cmap(
        'RdYlBu'
    ),  # diverging: 1 good, 0 special, -1 bad (pearson's R, spearman's rho')
    'div_worse': plt.cm.get_cmap(
        'RdYlBu_r'
    ),  # diverging: 1 bad, 0 special, -1 good (difference of bias)
    'div_neutr':
    plt.cm.get_cmap('RdYlGn'),  # diverging: zero good, +/- neutral: (bias)
    'seq_worse': plt.cm.get_cmap(
        'YlGn_r'
    ),  # sequential: increasing value bad (p_R, p_rho, rmsd, ubRMSD, RSS)
    'seq_better': plt.cm.get_cmap(
        'YlGn'),  # sequential: increasing value good (n_obs, STDerr)
    'qua_neutr':
    get_status_colors(),  # qualitative category with 2 forced colors
}

_colormaps = {  # from /qa4sm/validator/validation/graphics.py
    'R': _cclasses['div_better'],
    'p_R': _cclasses['seq_worse'],
    'rho': _cclasses['div_better'],
    'p_rho': _cclasses['seq_worse'],
    'RMSD': _cclasses['seq_worse'],
    'BIAS': _cclasses['div_neutr'],
    'n_obs': _cclasses['seq_better'],
    'urmsd': _cclasses['seq_worse'],
    'mse': _cclasses['seq_worse'],
    'mse_corr': _cclasses['seq_worse'],
    'mse_bias': _cclasses['seq_worse'],
    'mse_var': _cclasses['seq_worse'],
    'RSS': _cclasses['seq_worse'],
    'tau': _cclasses['div_better'],
    'p_tau': _cclasses['seq_worse'],
    'snr': _cclasses['div_better'],
    'err_std': _cclasses['seq_worse'],
    'beta': _cclasses['div_neutr'],
    'status': _cclasses['qua_neutr'],
}

# Colorbars for difference plots
_diff_colormaps = {  # from /qa4sm/validator/validation/graphics.py
    'R': _cclasses['div_better'],
    'p_R': _cclasses['div_worse'],
    'rho': _cclasses['div_better'],
    'p_rho': _cclasses['div_worse'],
    'tau': _cclasses['div_better'],
    'p_tau': _cclasses['div_worse'],
    'RMSD': _cclasses['div_worse'],
    'BIAS': _cclasses['div_worse'],
    'urmsd': _cclasses['div_worse'],
    'RSS': _cclasses['div_worse'],
    'mse': _cclasses['div_worse'],
    'mse_corr': _cclasses['div_worse'],
    'mse_bias': _cclasses['div_worse'],
    'mse_var': _cclasses['div_worse'],
    'snr': _cclasses['div_better'],
    'err_std': _cclasses['div_worse'],
    'beta': _cclasses['div_worse'],
}

# METRICS AND VARIABLES DEFINITIONS
# =====================================================
# 0=common metrics, 2=paired metrics (2 datasets), 3=triple metrics (TC, 3 datasets)
metric_groups = {
    0: ['n_obs'],
    2: [
        'R', 'p_R', 'rho', 'p_rho', 'RMSD', 'BIAS', 'urmsd', 'mse', 'mse_corr',
        'mse_bias', 'mse_var', 'RSS', 'tau', 'p_tau', 'status'
    ],
    3: ['snr', 'err_std', 'beta', 'status']
}

# === variable template ===
# how the metric is separated from the rest
var_name_metric_sep = {
    0: "{metric}",
    2: "{metric}_between_",
    3: "{metric}_{mds_id:d}-{mds}_between_"
}
var_name_CI = {
    0: "{metric}_ci_{bound}_between_",
    2: "{metric}_ci_{bound}_between_",
    3: "{metric}_ci_{bound}_{mds_id:d}-{mds}_between_"
}
# how two datasets are separated, ids must be marked as numbers with :d!
var_name_ds_sep = {
    0: None,
    2: "{ref_id:d}-{ref_ds}_and_{sat_id0:d}-{sat_ds0}",
    3:
    "{ref_id:d}-{ref_ds}_and_{sat_id0:d}-{sat_ds0}_and_{sat_id1:d}-{sat_ds1}"
}

# === metadata templates ===
_ref_ds_attr = 'val_ref'  # global meta values variable that links to the reference dc
_scale_ref_ds = 'val_scaling_ref'  # global meta values variable that links to the scaling reference dc
_ds_short_name_attr = 'val_dc_dataset{:d}'  # attribute convention for other datasets
_ds_pretty_name_attr = 'val_dc_dataset_pretty_name{:d}'  # attribute convention for other datasets
_version_short_name_attr = 'val_dc_version{:d}'  # attribute convention for other datasets
_version_pretty_name_attr = 'val_dc_version_pretty_name{:d}'  # attribute convention for other datasets
_val_dc_variable_pretty_name = 'val_dc_variable_pretty_name{:d}'  # attribute convention for variable name

# format should have (metric, ds, ref, other ds)
_variable_pretty_name = {
    0: "{}",
    2: "{}\nof {}\nwith {} as reference",
    3: "{} of {} \n against {}, {}"
}

# check if every metric has a colormap
for group in metric_groups.keys():
    assert all([m in _colormaps.keys() for m in metric_groups[group]])

# Value ranges of metrics, either absolute values, or a quantile between 0 and 1
_metric_value_ranges = {  # from /qa4sm/validator/validation/graphics.py
    'R': [-1, 1],
    'p_R': [0, 1],  # probability that observed correlation is statistical fluctuation
    'rho': [-1, 1],
    'p_rho': [0, 1],
    'tau': [-1, 1],
    'p_tau': [0, 1],
    'RMSD': [0, None],
    'BIAS': [None, None],
    'n_obs': [0, None],
    'urmsd': [0, None],
    'RSS': [0, None],
    'mse': [0, None],
    'mse_corr': [0, None],
    'mse_bias': [0, None],
    'mse_var': [0, None],
    'snr': [None, None],
    'err_std': [None, None],
    'beta': [None, None],
    'status': [-1, len(status)-2],
}
# mask values out of range
_metric_mask_range = {
    'err_std': [0, None],  # values below 0 exit but should be marked
}

# check if every metric has a colormap
for group in metric_groups.keys():
    assert all([m in _colormaps.keys() for m in metric_groups[group]])

# label format for all metrics
_metric_description = {  # from /qa4sm/validator/validation/graphics.py
    'R': '',
    'p_R': '',
    'rho': '',
    'p_rho': '',
    'tau': '',
    'p_tau': '',
    'RMSD': ' in {}',
    'BIAS': ' in {}',
    'n_obs': '',
    'urmsd': ' in {}',
    'RSS': ' in ({})²',
    'mse': ' in ({})²',
    'mse_corr': ' in ({})²',
    'mse_bias': ' in ({})²',
    'mse_var': ' in ({})²',
    'snr': ' in dB',
    'err_std': ' in {}',
    'beta': ' in {}',
    'status': '',
}


# units for all datasets
def get_metric_units(dataset, raise_error=False):
    # function to get m.u. with possibility to raise error
    _metric_units = {  # from /qa4sm/validator/validation/graphics.py
        'ISMN': 'm³/m³',
        'C3S': 'm³/m³',  # old name
        'C3S_combined': 'm³/m³',
        'GLDAS': 'm³/m³',
        'ASCAT': '% saturation',
        'SMAP': 'm³/m³',   # old name
        'SMAP_L3': 'm³/m³',
        'ERA5': 'm³/m³',
        'ERA5_LAND': 'm³/m³',
        'ESA_CCI_SM_active': '% saturation',
        'ESA_CCI_SM_combined': 'm³/m³',
        'ESA_CCI_SM_passive': 'm³/m³',
        'SMOS': 'm³/m³',   # old name
        'SMOS_IC': 'm³/m³',
        'CGLS_CSAR_SSM1km': '% saturation',
        'CGLS_SCATSAR_SWI1km': '% saturation',
        'SMOS_L3': 'm³/m³',
        'SMOS_L2': 'm³/m³',
        'SMAP_L2': 'm³/m³',
        'SMOS_SBPCA': 'm³/m³',
    }

    try:
        return _metric_units[dataset]

    except KeyError:
        if raise_error:
            raise KeyError(
                f"The dataset {dataset} has not been specified in {__name__}")

        else:
            warnings.warn(
                f"The dataset {dataset} has not been specified in {__name__}. "
                f"Set 'raise_error' to True to raise an exception for this case."
            )

            return "n.a."


# label name for all metrics
_metric_name = {  # from /qa4sm/validator/validation/globals.py
    'R': 'Pearson\'s r',
    'p_R': 'Pearson\'s r p-value',
    'rho': 'Spearman\'s ρ',
    'p_rho': 'Spearman\'s ρ p-value',
    'RMSD': 'Root-mean-square deviation',
    'BIAS': 'Bias (difference of means)',
    'n_obs': '# observations',
    'urmsd': 'Unbiased root-mean-square deviation',
    'RSS': 'Residual sum of squares',
    'tau': 'Kendall rank correlation',
    'p_tau': 'Kendall tau p-value',
    'mse': 'Mean square error',
    'mse_corr': 'Mean square error correlation',
    'mse_bias': 'Mean square error bias',
    'mse_var': 'Mean square error variance',
    'snr': 'Signal-to-noise ratio',
    'err_std': 'Error standard deviation',
    'beta': 'TC scaling coefficient',
    'status': 'Validation errors'
}

# BACKUPS
# =====================================================
# to fallback to in case the dataset attributes in the .nc file are
# missing some entries. Sould have variable short name as keys as these
# should be always available in the template.

# fallback for dataset pretty names in case they are not in the metadata
_dataset_pretty_names = {  # from qa4sm\validator\fixtures\datasets.json
    'ISMN': 'ISMN',
    'C3S_combined': 'C3S SM combined',
    'C3S': 'C3S SM combined',  # old name for C3S_combined
    'GLDAS': 'GLDAS',
    'ASCAT': 'H-SAF ASCAT SSM CDR',
    'SMAP_L3': 'SMAP level 3',
    'SMAP': 'SMAP level 3',  # old name for SMAP_L3
    'ERA5': 'ERA5',
    'ERA5_LAND': 'ERA5-Land',
    'ESA_CCI_SM_active': 'ESA CCI SM active',
    'ESA_CCI_SM_combined': 'ESA CCI SM combined',
    'ESA_CCI_SM_passive': 'ESA CCI SM passive',
    'SMOS_IC': 'SMOS IC',
    'SMOS': 'SMOS IC',  # old name for SMOS IC
    'CGLS_CSAR_SSM1km': 'CGLS S1 SSM',
    'CGLS_SCATSAR_SWI1km': 'CGLS SCATSAR SWI',
    'SMOS_L3': 'SMOS L3',
    'SMOS_L2': 'SMOS L2',
    'SMAP_L2': 'SMAP L3',
    'SMOS_SBPCA': 'SMOS SBPCA',
}

# available backups
_backups = {
    "_version_short_name_attr": "_dataset_version_pretty_names",
    "_val_dc_variable_pretty_name": "_dataset_variable_names"
}

# fallback for dataset __version pretty names in case they are not in the metadata
_dataset_version_pretty_names = {  # from qa4sm\validator\fixtures\versions.json
    "C3S_V201706": "v201706",
    "C3S_V201812": "v201812",
    "C3S_V201912": "v201912",
    "SMAP_V5_PM": "v5 PM/ascending",
    "SMAP_V5_AM": "v5 AM/descending",
    "ASCAT_H113": "H113",
    "ISMN_V20180712_TEST": "20180712 testset",
    "ISMN_V20180712_MINI": "20180712 mini testset",
    "ISMN_V20180830_GLOBAL": "20180830 global",
    "ISMN_V20190222_GLOBAL": "20190222 global",
    "ISMN_V20191211_GLOBAL": "20191211 global",
    "ISMN_V20210131": "20210131 global",
    "ISMN_V20230110": "20230110 global",
    "GLDAS_NOAH025_3H_2_1": "NOAH025 3H.2.1",
    "GLDAS_TEST": "TEST",
    "ESA_CCI_SM_C_V04_4": "v04.4",
    "ESA_CCI_SM_A_V04_4": "v04.4",
    "ESA_CCI_SM_P_V04_4": "v04.4",
    "ESA_CCI_SM_C_V04_5": "v04.5",
    "ESA_CCI_SM_A_V04_5": "v04.5",
    "ESA_CCI_SM_P_V04_5": "v04.5",
    "SMOS_105_ASC": "V.105 Ascending",
    "SMOS_105_DES": "V.105 Descending",
    "ERA5_test": " ERA5 test",
    "ERA5_20190613": "v20190613",
    "ERA5_LAND_V20190904": "v20190904",
    "ERA5_LAND_TEST": "ERA5-Land test",
    "CGLS_CSAR_SSM1km_V1_1": "v1_1",
    "CGLS_SCATSAR_SWI1km_V1_0": "v1_0",
    "SMOSL3_v339_ASC": "version 339 Ascending",
    "SMOSL3_v339_DESC": "version 339 Descending",
    "SMAPL2_V8": 'V8',
    "SMOSL2_700": 'v700',
    "SMOS_SBPCA_v724": "v724",
}

# fallback for dataset val_dc_variable in case they are not in the metadata
# subdivided by version in case anything changes between versions (e.g. measuring depths in GLDAS)
_dataset_variable_names = {  # from qa4sm\validator\fixtures\versions.json
    "C3S_V201706": "soil moisture",
    "C3S_V201812": "soil moisture",
    "C3S_V201912": "soil moisture",
    "SMAP_V5_PM": "soil moisture",
    "SMAP_V5_AM": "soil moisture",
    "ASCAT_H113": "soil moisture",
    "ISMN_V20180712_TEST": "soil moisture",
    "ISMN_V20180712_MINI": "soil moisture",
    "ISMN_V20180830_GLOBAL": "soil moisture",
    "ISMN_V20190222_GLOBAL": "soil moisture",
    "ISMN_V20191211_GLOBAL": "soil moisture",
    "ISMN_V20210131": "soil moisture",
    "ISMN_V20230110": "soil moisture",
    "GLDAS_NOAH025_3H_2_1": "soil moisture depth unknown",
    "GLDAS_TEST": "soil moisture depth unknown",
    "ESA_CCI_SM_C_V04_4": "soil moisture",
    "ESA_CCI_SM_A_V04_4": "soil moisture",
    "ESA_CCI_SM_P_V04_4": "soil moisture",
    "ESA_CCI_SM_C_V04_5": "soil moisture",
    "ESA_CCI_SM_A_V04_5": "soil moisture",
    "ESA_CCI_SM_P_V04_5": "soil moisture",
    "SMOS_105_ASC": "soil moisture",
    "SMOS_105_DES": "soil moisture",
    "ERA5_test": "svwl1",
    "ERA5_20190613": "svwl1",
    "ERA5_LAND_V20190904": "svwl1",
    "ERA5_LAND_TEST": "svwl1",
    "CGLS_CSAR_SSM1km_V1_1": "soil moisture",
    "CGLS_SCATSAR_SWI1km_V1_0": "SWI",
    "SMOSL3_v339_ASC": "soil moisture",
    "SMOSL3_v339_DESC": "soil moisture",
    "SMOSL2_sm": 'soil moisture',
    "SMAPL2_soil_moisture": 'soil moisture',
}


# ----------- fallback for resolution information -----------------------
def get_resolution_info(dataset, raise_error=False):
    # function to get resolution information with possibility to raise error
    # This info is first looked for in the validation file; if not present,
    # this function works as fallback unless the specific dataset is not
    # listed in the lookup table, in which case an error can be rased, according
    # to 'raise_error'

    resolution = {  # from /qa4sm/validator/fixtures/datasets.json
        'ISMN': None,
        'C3S_combined': 0.25,
        'C3S': 0.25,   # old name, unused
        'GLDAS': 0.25,
        'ASCAT': 12.5,
        'SMAP': 36,   # old name, unused
        'SMAP_L3': 36,
        'ERA5': 0.25,
        'ERA5_LAND': 0.1,
        'ESA_CCI_SM_active': 0.25,
        'ESA_CCI_SM_combined': 0.25,
        'ESA_CCI_SM_passive': 0.25,
        'SMOS': 25,   # old name, unused
        'SMOS_IC': 25,
        'CGLS_CSAR_SSM1km': 1,
        'CGLS_SCATSAR_SWI1km': 1,
        'SMOS_L3': 25,
        'SMOS_L2': 15,
        'SMAP_L2': 35,
        'SMOS_SBPCA': 15,
    }

    # fallback for resolution unit information
    resolution_units = {  # from /qa4sm/validator/fixtures/datasets.json
        'ISMN': 'point',
        'C3S': 'deg',  # old name, unused
        'C3S_combined': 'deg',
        'GLDAS': 'deg',
        'ASCAT': 'km',
        'SMAP': 'km',   # old name, unused
        'SMAP_L3': 'km',
        'ERA5': 'deg',
        'ERA5_LAND': 'deg',
        'ESA_CCI_SM_active': 'deg',
        'ESA_CCI_SM_combined': 'deg',
        'ESA_CCI_SM_passive': 'deg',
        'SMOS': 'km',   # old name, unused
        'SMOS_IC': 'km',
        'CGLS_CSAR_SSM1km': 'km',
        'CGLS_SCATSAR_SWI1km': 'km',
        'SMOS_L3': 'km',
        'SMOS_L2': 'km',
        'SMAP_L2': 'km',
        'SMOS_SBPCA': 'km',
    }

    try:
        dataset_res = resolution[dataset]
        dataset_units = resolution_units[dataset]

        return dataset_res, dataset_units

    except KeyError:
        if raise_error:
            raise KeyError(
                f"The dataset {dataset} has not been specified in {__name__}")

        else:
            warnings.warn(
                f"The dataset {dataset} has not been specified in {__name__}. "
                f"Set 'raise_error' to True to raise an exception for this case."
            )

            return None, None


# METADATA STATICS
# =====================================================
# information needed for plotting the metadata-boxplots

# Min number of samples per bin to create a boxplot:
meta_boxplot_min_samples = 5

lc_classes = {
    "unknown": "Not provided",
    0: 'Other',
    10: 'Cropland',
    11: 'Cropland',
    12: 'Cropland',
    20: 'Cropland',
    30: 'Cropland',
    40: 'Tree cover',
    50: 'Tree cover',
    60: 'Tree cover',
    61: 'Tree cover',
    62: 'Tree cover',
    70: 'Tree cover',
    71: 'Tree cover',
    72: 'Tree cover',
    80: 'Tree cover',
    81: 'Tree cover',
    82: 'Tree cover',
    90: 'Tree cover',
    100: 'Tree cover',
    110: 'Tree cover',
    120: 'Grassland',
    121: 'Grassland',
    122: 'Grassland',
    130: 'Grassland',
    140: 'Other',
    150: 'Other',
    152: 'Other',
    153: 'Other',
    160: 'Tree cover',
    170: 'Tree cover',
    180: 'Grassland',
    190: 'Urban areas',
    200: 'Other',
    201: 'Other',
    202: 'Other',
    210: 'Other',
    220: 'Other'
}

climate_classes = {
    "unknown": "Not provided",
    "masked": "Not provided",
    "Af": "Tropical",
    "Am": "Tropical",
    "As": "Tropical",
    "Aw": "Tropical",
    "BWk": "Arid",
    "BWh": "Arid",
    "BWn": "Arid",
    "BSk": "Arid",
    "BSh": "Arid",
    "BSn": "Arid",
    "Csa": "Temperate",
    "Csb": "Temperate",
    "Csc": "Temperate",
    "Cwa": "Temperate",
    "Cwb": "Temperate",
    "Cwc": "Temperate",
    "Cfa": "Temperate",
    "Cfb": "Temperate",
    "Cfc": "Temperate",
    "Dsa": "Continental",
    "Dsb": "Continental",
    "Dsc": "Continental",
    "Dsd": "Continental",
    "Dwa": "Continental",
    "Dwb": "Continental",
    "Dwc": "Continental",
    "Dwd": "Continental",
    "Dfa": "Continental",
    "Dfb": "Continental",
    "Dfc": "Continental",
    "Dfd": "Continental",
    "ET": "Polar",
    "EF": "Polar",
    "W": "Water",
    "Mediterranean": "Mediterranean",
}

metadata = {
    "clay_fraction": ("clay fraction", None, "continuous", "[% weight]"),
    "climate_KG":
    ("Koeppen-Geiger climate class", climate_classes, "classes", None),
    "climate_insitu": ("climate in-situ", climate_classes, "classes", None),
    "elevation": ("elevation", None, "continuous", "[m]"),
    "instrument": ("instrument type", None, "discrete",
                   None),  # todo: improve labels (too packed)
    "lc_2000": ("land cover class (2000)", lc_classes, "classes", None),
    "lc_2005": ("land cover class (2005)", lc_classes, "classes", None),
    "lc_2010": ("land cover class (2010)", lc_classes, "classes", None),
    "lc_insitu": ("land cover class in-situ", lc_classes, "classes",
                  None),  # todo: handle custom names
    "network": ("network", None, "discrete", None),
    "organic_carbon":
    ("concentration of organic carbon", None, "continuous", "[% weight]"),
    "sand_fraction": ("sand fraction", None, "continuous", "[% weight]"),
    "saturation": ("saturation", None, "continuous", "[m³/m³]"),
    "silt_fraction": ("silt fraction", None, "continuous", "[% weight]"),
    "station": ("station", None, "discrete", None),
    "instrument_depthfrom": ("upper depth", None, "continuous", "[m]"),
    "instrument_depthto": ("lower depth", None, "continuous", "[m]"),
    # --- generated during the image initialization:
    "soil_type": ("soil granulometry", None, "discrete", None),
    "instrument_depth": ("instrument depth", None, "continuous", "[m]"),
    # --- FRM4SM QI, not always present
    "frm_class": ("FRM Classification", None, "discrete", None)
}

soil_types = ["clay_fraction", "silt_fraction", "sand_fraction"]
instrument_depths = ["instrument_depthfrom", "instrument_depthto"]

# metrics to be excluded from the automatic plotting
_metadata_exclude = [
    'p_R',
    'p_rho',
    'tau',
    'p_tau',
    'status',
]
