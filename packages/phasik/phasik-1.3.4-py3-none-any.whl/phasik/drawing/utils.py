"""
General utility functions for plots
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
import seaborn as sb
from matplotlib.colors import ListedColormap

__all__ = [
    "palette_20_ordered",
    "configure_sch_color_map",
    "display_name",
    "label_subplot_grid_with_shared_axes",
    "adjust_margin",
]


def palette_20_ordered(as_map=False):
    """Create an ordered color palette of 20 colors.

    The function uses the 'tab20' color palette from seaborn and rearranges the colors
    in an ordered pattern. By default, the colors are returned as a list, but if `as_map`
    is set to True, a `ListedColormap` object is returned.

    Parameters
    ----------
    as_map : bool, optional
        Whether to return the colors as a `ListedColormap` object (default is False).

    Returns
    -------
    list or ListedColormap
        The ordered color palette. If `as_map` is True, a `ListedColormap` object is returned.

    Examples
    --------
    >>> cmap = pk.palette_20_ordered(as_map=True)

    """
    pal = sb.color_palette("tab20", n_colors=20)
    pal2_arr = np.append(pal[::2], pal[1::2], axis=0)
    pal2 = sb.color_palette(pal2_arr)
    if as_map:
        pal2 = ListedColormap(pal2)
    return pal2


def configure_sch_color_map(cmap):
    """
    Set SciPy's colour palette to use a particular color map

    Parameters
    ----------
    cmap : colormap
        Colormap to set

    Returns
    -------
    None
    """
    rgbs = cmap(np.linspace(0, 1, 10))
    sch.set_link_color_palette([mpl.colors.rgb2hex(rgb[:3]) for rgb in rgbs])


def display_name(key):
    """Get a more user-friendly name for certain keywords.

    This function takes a keyword `key` and returns a more user-friendly name
    for that keyword if it exists in the predefined `names` dictionary.
    If the keyword is not found in the dictionary, it is returned as is.

    Parameters
    ----------
    key : str
        The keyword for which a display name is needed.

    Returns
    -------
    str
        The display name for the given keyword, or the original keyword if not found.

    Examples
    --------
    >>> display_name('maxclust')
    'Max # clusters'
    >>> display_name('distance')
    'Distance threshold'
    >>> display_name('unknown')
    'unknown'
    """

    names = {"maxclust": "Max # clusters", "distance": "Distance threshold"}
    return names.get(key, key)


def label_subplot_grid_with_shared_axes(axes, n_subplots, xlabel, ylabel):
    """
    Remove unused axes in grid.

    If number of axes is not-rectangular, there will be unused
    axes at the end of the grid. This removes those axes and
    ads axes ticks.

    Parameters
    ----------
    axes :list of matplotlib.Axes
        Axes containing the subplots
    n_subplots : int
        Number of subplots in the grid; need not be a 'rectangular' number
    xlabel : str
        Label of the x-axis
    ylabel : str
        Label of the y-axis

    Returns
    -------
    axes :list of matplotlib.Axes
        Axes containing the subplots
    """

    rows, columns = axes.shape

    if rows > 1:
        axes_left = axes[:, 0]
    else:
        axes_left = [axes[0]]
    for ax in axes_left:
        ax.set_ylabel(ylabel)

    # Bottom row will potentially have fewer subplots than all other rows.
    size_of_extra_row = n_subplots % columns

    if size_of_extra_row != 0 and rows > 1:
        # Delete blank subplots and add x-axis ticks to subplots on penultimate row above blank subplots
        blank_axes = axes[-1, size_of_extra_row:]
        above_blank_axes = axes[-2, size_of_extra_row:]
        axes_on_extra_row = axes[-1, :size_of_extra_row]
        for ax in blank_axes:
            plt.delaxes(ax)
        for ax in above_blank_axes:
            ax.xaxis.set_tick_params(labelbottom=True)
            ax.set_xlabel(xlabel)
        for ax in axes_on_extra_row:
            ax.set_xlabel(xlabel)

    else:
        for ax in axes.flatten()[-columns:]:
            ax.set_xlabel(xlabel)

    return ax


def adjust_margin(ax=None, top=0, bottom=0, left=0, right=0):
    """Extend the margin of a plot by a percentage of its original width/height

    Parameters
    ----------
    ax : matplotlib.Axes, optional
        Axes whose margins to adjust
    top : float, optional
        Percentage (as decimal) by which to increase top margin. Default: 0.
    bottom : float, optional
        Percentage (as decimal) by which to increase bottom margin. Default: 0.
    left : float, optional
        Percentage (as decimal) by which to increase left margin. Default: 0.
    right : float, optional
        Percentage (as decimal) by which to increase right margin. Default: 0.

    Returns
    -------
    ax : matplotlib.Axes, optional
        Axes with adjusted margins
    """

    if ax is None:
        ax = plt.gca()

    if top or bottom:
        y_limits = ax.get_ylim()
        difference = y_limits[-1] - y_limits[0]
        new_y_limits = [
            y_limits[0] - difference * bottom,
            y_limits[-1] + difference * top,
        ]
        ax.set_ylim(new_y_limits)

    if left or right:
        x_limits = ax.get_xlim()
        difference = x_limits[-1] - x_limits[0]
        new_x_limits = [
            x_limits[0] - difference * left,
            x_limits[-1] + difference * right,
        ]
        ax.set_xlim(new_x_limits)

    return ax
