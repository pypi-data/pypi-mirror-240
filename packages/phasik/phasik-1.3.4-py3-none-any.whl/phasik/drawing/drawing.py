"""
Useful drawing functions
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap

from phasik.utils.utils import get_extrema_of_binary_series

__all__ = [
    "plot_events",
    "plot_interval",
    "plot_phases",
    "threshold_plot",
    "plot_edge_series",
]


def plot_events(
    events,
    ax=None,
    text_y_pos=None,
    text_x_offset=0,
    period=None,
    n_periods=1,
    add_labels=True,
    orientation="vertical",
    zorder=-1,
    alpha=1,
    va="bottom",
):
    """Visualize the occurence of events as vertical lines.

    This function was designed to be used in complement to another function `plot_cluster_sets`
    that draws objects over time (horizontal axis). The vertical lines are drawn at the
    horizontal value corresponding to the time of occurrence of the event.

    Parameters
    ----------
    events : list of tuples (time, name, line_style)
        * time - time at which the event occurred
        * name - the name of the event
        * line_style - any string accepted by matplotlib.lines.Line2D.set_linestyle
    ax : matplotlib.Axes, optional
        Axes on which to plot the events
    text_y_pos : float, optional
        Height at which to place the name of the event (default None)
    text_x_offset : float, optional
        Distance along x-axis by which to offset the placement of the event name (default 0)
    period: float or None, optional
        Length of time of one period, if events repeat periodically.
    n_periods : int, optional
        Number of periods to draw, if events repeat periodically.
    add_labels : bool, optional
        Wether to display the label of each vertical line, True by default.
    orientation : {"vertical, horizontal"}, optonal
        Orientation of the lines marking the events. Default: "horizontal".
    zorder : float, optional
        Zorder of the lines marking the events. Default: -1.
    alpha : float
        Transparency of the lines marking the events. Default: 1.
    va : str, optional
        Direction with respect to which doing the vertical alignment. Default: "bottom"

    Returns
    -------
    matplotlib.axes.Axes
        The axis object to draw on

    See Also
    --------
    plot_phases
    plot_cluster_sets

    Examples
    --------
    >>> import phasik as pk
    >>> events = [(5, "START", "dashed"), (33, "bud", "dashed"), (36, "ori", "dashed")]
    >>> cluster_sets.plot(axs=(ax1, ax2), with_silhouettes=True)
    >>> pk.plot_events(events, ax=ax1)

    """

    if ax is None:
        ax = plt.gca()
    if text_y_pos is None:
        text_y_pos = 1.01 * ax.get_ylim()[1]
    if text_x_offset < 0:
        text_x_offset = -text_x_offset

    for event in events:
        time, name, line_style = event
        if orientation == "vertical":
            ax.axvline(
                x=time,
                c="k",
                ls=line_style,
                label=name,
                zorder=zorder,
                alpha=alpha,
            )
            text_x_pos = time - text_x_offset if time > 0 else time + text_x_offset
            if add_labels:
                ax.text(
                    text_x_pos,
                    text_y_pos,
                    name,
                    fontsize="small",
                    rotation=90,
                    va=va,
                    ha="center",
                )
        elif orientation == "horizontal":
            ax.axhline(
                y=time,
                c="k",
                ls=line_style,
                label=name,
                zorder=zorder,
                alpha=alpha,
            )
        else:
            print(
                "WARNING: wrong orientation, must be one of {'vertical', 'horizontal'}"
            )

    if period is not None and n_periods > 1:
        # repeat events over n periods
        for k in range(1, n_periods):
            for event in events:
                time, name, line_style = event
                time += period * k

                if orientation == "vertical":
                    ax.axvline(
                        x=time,
                        c="k",
                        ls=line_style,
                        label=name,
                        zorder=zorder,
                        alpha=alpha,
                    )
                    text_x_pos = (
                        time - text_x_offset if time > 0 else time + text_x_offset
                    )
                    if add_labels:
                        ax.text(
                            text_x_pos,
                            text_y_pos,
                            name,
                            fontsize="small",
                            rotation=90,
                            va=va,
                            ha="center",
                        )
                elif orientation == "horizontal":
                    ax.axhline(
                        y=time,
                        c="k",
                        ls=line_style,
                        label=name,
                        zorder=zorder,
                        alpha=alpha,
                    )
                else:
                    print(
                        "WARNING: wrong orientation, must be one of {'vertical', 'horizontal'}"
                    )
    return ax


def plot_phases(phases, ax=None, y_pos=None, ymin=0, ymax=1, t_offset=0, color="k"):
    """Visualize temporal phases as shaded intervals

    This function was designed to be used in complement to another function `plot_cluster_sets`
    that draws objects over time (horizontal axis). The phases are drawn as shaded regions
    spanning the time interval corresponding to the phases.

    Parameters
    ----------
    phases : list of tuples (start_time, end_time, name)
        The start time, end time, and name of each phase to visualize
    ax : matplotlib.Axes
        Axes on which to plot the phases
    y_pos : float or None, optional
        Height at which to place the name of the phase
    ymin : float, optional
        Height at which to start shaded region (default 0)
    ymax : float, optional
        Height at which to stop shaded region (default 1)
    t_offset : float, optional
        Offset of phase on the time axis
    color : color
        Color to draw the intervals in.

    Returns
    -------
    matplotlib.axes.Axes
        The axis object to draw on

    See Also
    --------
    plot_events
    plot_cluster_sets

    Examples
    --------
    >>> import phasik as pk
    >>> phases = [(0, 35, "G1"), (35, 70, "S"), (70, 78, "G2")]
    >>> cluster_sets.plot(axs=(ax1, ax2), with_silhouettes=True)
    >>> pk.plot_phases(phases, ax=ax1, y_pos=0.05, ymax=0.1)


    """

    if ax is None:
        ax = plt.gca()

    y_pos = y_pos if y_pos is not None else 1.01
    y_lim = ax.get_ylim()
    absolute_y_pos = y_lim[0] + y_pos * (y_lim[1] - y_lim[0])

    for i, phase in enumerate(phases):
        start_time, end_time, name = phase
        start_time += t_offset
        end_time += t_offset
        mid_time = (start_time + end_time) / 2
        alpha_interval = 0.5 / len(phases)
        ax.axvspan(
            xmin=start_time,
            xmax=end_time,
            ymin=ymin,
            ymax=ymax,
            color=color,
            alpha=alpha_interval * (i + 1),
        )
        ax.text(
            mid_time,
            absolute_y_pos,
            name,
            fontweight="bold",
            va="center",
            ha="center",
        )

    return ax


def plot_interval(
    binary_series, times, y=0, peak=None, color="k", ax=None, zorder=None
):
    """Plot a binary series as a sequence of coloured intervals

    Specifically, draw rectangles to mark intervals where the binary series
    has value 1 (where it has value 0, do nothing).

    Parameters
    ----------
    binary_series : ndarray
        2D array of binary data to plot
    times : ndarray
        1D array consisting of the corresponding time points
    y : float, optional
        Height (y-axis value) at which to plot the interval (default 0)
    peak : float, optional
        Time at which to mark the presence of peak with a red star. By default (None),
        not drawn.
    color : str, optional
        Color to use for the intervals (default 'k')
    ax : matplotlib.Axes, optional
        Axes to plot on
    zorder : int, optional
        Height of the z-axis on which to plot the interval (default None)

    Returns
    -------
    matplotlib.axes.Axes
        The axis object to draw on

    Examples
    --------
    >>> import phasik as pk
    >>> binary_series = [1, 1, 1, 0, 0, 1, 1, 0]
    >>> times = list(range(8))
    >>> pk.plot_interval(binary_series, times, peak=2)

    """

    if ax is None:
        ax = plt.gca()

    xmins, xmaxs = get_extrema_of_binary_series(binary_series, times)
    rect_height = 0.5

    for xmin, xmax in zip(xmins, xmaxs):
        rect = patches.Rectangle(
            (xmin, y),
            xmax - xmin,
            rect_height,
            fill=True,
            color=color,
            zorder=zorder,
        )
        ax.add_patch(rect)
    if peak is not None:
        ax.plot(peak, y + rect_height / 2, "r*")

    return ax


def threshold_plot(
    x, y, threshold, color_below_threshold, color_above_threshold, ax=None
):
    """
    Plot values above a certain threshold in a particular colour

    Parameters
    ----------
    x : array
        1D array of values to plot along x-axis
    y : array
        1D array of values to plot along y-axis
    threshold : float
        Only plot in colour the points (x,y) with y >= threshold
    color_below_threshold : color
        Colour to use for points below threshold
    color_above_threshold : list colors
        Colour to use for points above threshold
    ax : matplotlib.Axes, optional
        Axes to use

    Returns
    -------
    line_collection : matplotlib LineCollection
    """

    if ax is None:
        ax = plt.gca()

    # Create a colormap for red, green and blue and a norm to color
    # f' < -0.5 red, f' > 0.5 blue, and the rest green
    cmap = ListedColormap([color_below_threshold, color_above_threshold])
    norm = BoundaryNorm([np.min(y), threshold, np.max(y)], cmap.N)

    # Create a set of line segments so that we can color them individually
    # This creates the points as a N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be numlines x points per line x 2 (x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Create the line collection object, setting the colormapping parameters.
    # Have to set the actual values used for colormapping separately.
    line_collection = LineCollection(segments, cmap=cmap, norm=norm)
    line_collection.set_array(y)

    ax.add_collection(line_collection)
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(y) * 1.1, np.max(y) * 1.1)
    return line_collection


def plot_edge_series(temporal_network, edges, ax=None, **kwargs):
    """Draw time series of edge weights, for the specified edges

    Parameters
    ----------
    temporal_network : pk.TempNet
        Temporal network
    edges: list of str
        List of edges to plot
    ax : matplotlib.Axes, optional
        Axes to use
    **kwargs :
        Other parameters to pass to matplotlib's plot

    Returns
    -------
    matplotlib.axes.Axes
        The axis object to draw on

    Examples
    --------
    >>> import phasik as pk
    >>> pk.plot_edge_series(temporal_network, ["A-B", "B-C"])
    """

    times = temporal_network.times

    if ax is None:
        ax = plt.gca()

    for edge in edges:
        ax.plot(times, temporal_network.edge_timeseries()[edge], **kwargs)

    return ax
