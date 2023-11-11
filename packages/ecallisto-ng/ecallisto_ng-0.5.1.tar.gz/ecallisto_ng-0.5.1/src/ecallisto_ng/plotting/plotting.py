import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

from ecallisto_ng.data_fetching.get_data import NoDataAvailable, get_data
from ecallisto_ng.plotting.utils import (
    fill_missing_timesteps_with_nan, return_strftime_based_on_range,
    return_strftime_for_ticks_based_on_range,
    timedelta_to_sql_timebucket_value)


def plot_spectogram(
    df,
    instrument_name=None,
    start_datetime=None,
    end_datetime=None,
    title="Radio Flux Density",
    size=18,
    color_scale=px.colors.sequential.Plasma,
):
    # Create a new dataframe with rounded column names
    df = df.copy()
    df.columns = df.columns.astype(float)

    # If instrument name is not provided, try to get it from the dataframe
    if instrument_name is None:
        instrument_name = df.attrs.get("FULLNAME", "Unknown")

    # If start_datetime is not provided, try to get it from the dataframe
    if start_datetime is None:
        start_datetime = df.index.min()
    if end_datetime is None:
        end_datetime = df.index.max()

    # Make datetime prettier
    if isinstance(start_datetime, str):
        start_datetime = pd.to_datetime(start_datetime)
    if isinstance(end_datetime, str):
        end_datetime = pd.to_datetime(end_datetime)

    fig = px.imshow(
        df.T,
        color_continuous_scale=color_scale,
        zmin=df.min().min(),
        zmax=df.max().max(),
    )
    fig.update_layout(
        title=f"{instrument_name} {title}",
        xaxis_title="Datetime [UT]",
        yaxis_title="Frequency [MHz]",
        font=dict(family="Computer Modern, monospace", size=size, color="#4D4D4D"),
        plot_bgcolor="black",
        xaxis_showgrid=True,
        yaxis_showgrid=False,
    )
    return fig


def plot_spectogram_mpl(
    df,
    instrument_name=None,
    start_datetime=None,
    end_datetime=None,
    title="Radio Flux Density",
    fig_size=(9, 6),
    cmap="plasma",
):
    # Create a new dataframe with rounded column names
    df = df.copy()

    # Drop any rows where the datetime col is NaN
    df = df[df.index.notnull()]

    # Reverse the columns
    df = df.iloc[:, ::-1]

    # If instrument name is not provided, try to get it from the dataframe
    if instrument_name is None:
        instrument_name = df.attrs.get("FULLNAME", "Unknown")

    # If start_datetime is not provided, try to get it from the dataframe
    if start_datetime is None:
        start_datetime = df.index.min()
    if end_datetime is None:
        end_datetime = df.index.max()

    # Make datetime prettier
    if isinstance(start_datetime, str):
        start_datetime = pd.to_datetime(start_datetime)
    if isinstance(end_datetime, str):
        end_datetime = pd.to_datetime(end_datetime)

    strf_format = return_strftime_based_on_range(end_datetime - start_datetime)
    strf_format_ticks = return_strftime_for_ticks_based_on_range(
        end_datetime - start_datetime
    )
    sd_str = start_datetime.strftime(strf_format)
    ed_str = end_datetime.strftime(strf_format)

    fig, ax = plt.subplots(figsize=fig_size)

    # Set NaN color to black
    current_cmap = plt.get_cmap(cmap).copy()
    current_cmap.set_bad(color="black")

    # The imshow function in matplotlib displays data top-down, so we need to reverse the rows
    cax = ax.imshow(
        df.T.iloc[::-1],
        aspect="auto",
        extent=[0, df.shape[0], 0, df.shape[1]],
        cmap=current_cmap,
        interpolation="none",
    )

    def find_nearest_idx(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return idx

    # Calculate the rough spacing for around 15 labels
    spacing = max(1, int(df.shape[1] / 15))

    # Create target ticks
    target_ticks = np.unique((df.columns.astype(float) / 10).astype(int) * 10)

    # Finding the closest indices in the DataFrame to the target_ticks
    major_ticks = [
        find_nearest_idx(df.columns.astype(float), tick) for tick in target_ticks
    ]

    # Set major ticks and their appearance
    ax.set_yticks(major_ticks, minor=False)  # This line was missing
    ax.tick_params(axis="y", which="major", length=10, labelsize="medium")

    # Create labels based on the position
    major_labels = [str(int(round(float(df.columns[i]), 0))) for i in major_ticks]
    ax.set_yticklabels(major_labels, minor=False)

    # Assuming df index is datetime, this will format the x-ticks
    # Compute the spacing required to get close to 30 x-labels
    spacing = max(1, df.shape[0] // 15)

    x_ticks = np.arange(0, df.shape[0], spacing)
    ax.set_xticks(x_ticks)
    # Get format
    strf_format_ticks = return_strftime_for_ticks_based_on_range(
        end_datetime - start_datetime
    )
    ax.set_xticklabels(
        df.index[x_ticks].strftime(strf_format_ticks), rotation=60, ha="center"
    )
    # Title
    title = f"{instrument_name} {title} | {sd_str} to {ed_str}"
    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Time [UT]")
    ax.set_ylabel("Frequency [MHz]")
    ax.grid(False)

    # Adding colorbar
    cbar = fig.colorbar(cax)
    cbar.set_label("Amplitude")

    fig.tight_layout()
    return fig


def plot_with_fixed_resolution_mpl(
    instrument,
    start_datetime_str,
    end_datetime_str,
    sampling_method,
    resolution=720,
    fig_size=(9, 6),
):
    """
    Plots the spectrogram for the given instrument between specified start and end datetime strings
    with a fixed resolution using Matplotlib.

    Parameters:
    - instrument (str): The name of the instrument for which the spectrogram needs to be plotted.
    - start_datetime_str (str or pd.Timestamp): The starting datetime for the data range.
        Can be a string in the format 'YYYY-MM-DD HH:MM:SS' or a Pandas Timestamp.
    - end_datetime_str (str or pd.Timestamp): The ending datetime for the data range.
        Can be a string in the format 'YYYY-MM-DD HH:MM:SS' or a Pandas Timestamp.
    - sampling_method (str): The sampling method to be used for the data aggregation.
        Can be one of 'max', 'min', 'avg'.
    - resolution (int, optional): The desired resolution for plotting. Default is 720.
        Determines the time bucketing for the data aggregation.
    - fig_size (tuple, optional): The desired figure size. Default is (9, 6).
        The figure size is passed to Matplotlib's `figsize` parameter.

    Returns:
    None. A spectrogram is plotted using Matplotlib.

    Usage:
    plot_with_fixed_resolution_mpl('some_instrument', '2022-03-31 18:46:00', '2022-04-01 18:46:00', resolution=500)

    Note:
    The function internally calls other utility functions including:
    - timedelta_to_sql_timebucket_value() to convert the time delta to an appropriate format for SQL queries.
    - get_data() to fetch the data based on the provided parameters.
    - fill_missing_timesteps_with_nan() to handle any missing data points.
    - plot_spectogram_mpl() to generate the actual spectrogram plot.
    """

    # Make datetime prettier
    if isinstance(start_datetime_str, str):
        start_datetime = pd.to_datetime(start_datetime_str)
    if isinstance(end_datetime_str, str):
        end_datetime = pd.to_datetime(end_datetime_str)

    time_delta = (end_datetime - start_datetime) / resolution
    # Create parameter dictionary
    params = {
        "instrument_name": instrument,
        "start_datetime": start_datetime_str,
        "end_datetime": end_datetime_str,
        "timebucket": timedelta_to_sql_timebucket_value(time_delta),
        "agg_function": sampling_method,
    }
    # Get data
    try:
        df = get_data(**params)
    except NoDataAvailable as e:
        print(e)
        return None

    df_filled = fill_missing_timesteps_with_nan(df, start_datetime, end_datetime)

    # Plot
    return plot_spectogram_mpl(
        df_filled, instrument, start_datetime, end_datetime, fig_size=fig_size
    )
