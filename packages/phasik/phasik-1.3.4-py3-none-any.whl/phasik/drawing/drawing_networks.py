"""
Functions to visualize networks and temporal networks
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sb
from matplotlib import animation
from matplotlib.lines import Line2D

import phasik as pk

__all__ = [
    "standard_node_params",
    "standard_edge_params",
    "standard_label_params",
    "standard_params",
    "draw_graph",
    "highlight_subgraphs",
    "animate_temporal_network",
]


def standard_params(color):
    """
    Returns a dictionary containing standard values of plotting parameters

    Parameters
    ----------
    color : color
        Color to use for nodes and edges
    Returns
    -------
    dict

    """
    return {
        "node_color": color,
        "edge_color": color,
        "font_color": "k",
        "font_size": "medium",
        "edgecolors": "k",
        "node_size": 100,
        "bbox": dict(
            facecolor=color,
            edgecolor="black",
            boxstyle="round, pad=0.2",
            alpha=1,
        ),
    }


def standard_node_params(color):
    """
    Returns a dictionary containing standard values of node plotting parameters

    Parameters
    ----------
    color : color
        Color to use for nodes
    Returns
    -------
    dict

    """
    return {"node_color": color, "edgecolors": "k", "node_size": 100}


def standard_edge_params(color):
    """
    Returns a dictionary containing standard values of edge plotting parameters

    Parameters
    ----------
    color : color
        Color to use for edges
    Returns
    -------
    dict

    """
    return {
        "edge_color": color,
    }


def standard_label_params(color):
    """
    Returns a dictionary containing standard values of label plotting parameters

    Parameters
    ----------
    color : color
        Color to use for labels
    Returns
    -------
    dict

    """
    return {
        "font_color": "k",
        "font_size": "medium",
        "bbox": dict(
            facecolor=color,
            edgecolor="black",
            boxstyle="round, pad=0.2",
            alpha=1,
        ),
    }


def draw_graph(
    graph,
    ax=None,
    pos=None,
    color="mediumseagreen",
    edge_widths=None,
    edge_colors=None,
    edge_cmap=None,
    edge_vmin=None,
    edge_vmax=None,
    label_nodes=True,
    colorbar=True,
):
    """Basic graph drawing function

    Parameters
    ----------
    graph : networkx.Graph
        Graph to visualise
    ax : matplotlib.Axes, optional
        Axes on which to draw the graph
    pos : dict
        Dictionary of node positions of the form {node_id : (x, y)}
    color : str, optional
        Color to use for the graph nodes and edges (default 'mediumseagreen')
    edge_widths: float or array of floats
        Line width of edges
    edge_colors: color or array of colors
        Edge color. Can be a single color or a sequence of colors with the same length as
        edgelist. Color can be string or rgb (or rgba) tuple of floats from 0-1.
        If numeric values are specified they will be mapped to colors using the edge_cmap
        and edge_vmin,edge_vmax parameters.
    edge_cmap: Matplotlib colormap, optional
        Colormap for mapping intensities of edges
    edge_vmin,edge_vmax: floats, optional
        Minimum and maximum for edge colormap scaling
    label_nodes : bool, optional
        Whether to label the nodes or just leave them as small circles (default True)
    colorbar : bool, optional
        Wether to draw a colorbar

    Returns
    -------
    matplotlib.axes.Axes
        The axis object to draw on

    Examples
    --------
    >>> import networkx as nx
    >>> import phasik as pk
    >>> G = nx.fast_gnp_random_graph(10, 0.5)
    >>> pk.draw_graph(G)
    """

    if ax is None:
        ax = plt.gca()

    if pos is None:
        pos = nx.spring_layout(graph)

    params_nodes = standard_node_params(color)
    params_edges = standard_edge_params(color)
    params_labels = standard_label_params(color)

    if edge_widths is not None:
        params_edges["width"] = edge_widths
    if edge_colors is not None:
        params_edges["edge_color"] = edge_colors

    nx.draw_networkx_nodes(graph, ax=ax, pos=pos, **params_nodes)
    im = nx.draw_networkx_edges(
        graph,
        ax=ax,
        pos=pos,
        edge_cmap=edge_cmap,
        edge_vmin=edge_vmin,
        edge_vmax=edge_vmin,
        **params_edges,
    )
    if label_nodes:
        nx.draw_networkx_labels(graph, ax=ax, pos=pos, **params_labels)

    if colorbar:
        if edge_colors is not None:
            if len(edge_colors) == len(graph.edges):
                plt.colorbar(im, ax=ax, label="edge color scale")

    return ax


def highlight_subgraphs(graphs, colors, ax=None, pos=None, label_nodes=True):
    """Draw multiple nested subgraphs on the same axes

    Parameters
    ----------
    graphs : list of networkx.Graph

    colors : list of str
        List of colors, one for each of the graphs in 'graphs'
    ax : matplotlib.Axes, optional
        Axes to plot on
    pos : dict
        Dictionary of node positions
    label_nodes : bool, optional
        Whether or not to label the graph nodes or leave them as circles

    Returns
    -------
    None

    Examples
    --------
    >>> import networkx as nx
    >>> import phasik as pk
    >>> graphs = [nx.fast_gnp_random_graph(10, 0.5) for i in range(3)]
    >>> pk.highlight_subgraphs(graphs, ["red", "blue", "green"])
    """

    if ax is None:
        ax = plt.gca()

    if pos is None:
        pos = nx.spring_layout(graphs[0])

    for graph, color in zip(graphs, colors):
        draw_graph(
            graph=graph,
            pos=pos,
            ax=ax,
            label_nodes=label_nodes,
            color=color,
            edge_colors=color,
        )

    return


def animate_temporal_network(
    temporal_network,
    color_temporal="red",
    color_constant="silver",
    width_scale=1.5,
    with_labels=True,
    pos=None,
    ax=None,
    interval=20,
    frames=None,
):
    """Return animation of the temporal network evolving over time

    Parameters
    ----------
    temporal_network : phasik.TemporalNetwork
        Temporal network to visualise
    color_temporal : str
        Color of the time-varying edges, defaults to 'red'
    color_constant : str
        Color of the constant edges (defaults to 'silver'), i.e. for which we have no
        temporal information
    width_scale : float
        Scale factor for width of the temporal edges compared to the constant ones
    with_labels : bool, optional
        Wether to draw node labels
    pos : dict
        Dictionary of node positions
    ax : matplotlib.axis
        Axes to plot the animation on
    interval : int
        Interval of time between frames, in ms.
    frames : int
        Number of frames of the animation (should be at most the number of timepoints (default))

    Returns
    -------
    matplotlib.animation

    Examples
    --------
    >>> import phasik as pk
    >>> pk.animate_temporal_network(temporal_network)
    """

    if frames is None:
        frames = temporal_network.T()

    aggregated_network = temporal_network.aggregated_network(output="normalised")
    if pos is None:
        pos = nx.spring_layout(aggregated_network)

    if ax is None:
        fig, ax = plt.subplots(figsize=(15, 12))
    else:
        fig = plt.gcf()

    if isinstance(temporal_network, pk.PartiallyTemporalNetwork):
        edges_temporal = temporal_network.temporal_edges
        edges_all = list(aggregated_network.edges())
        edges_constant = list(set(edges_all).difference(edges_temporal))
    elif isinstance(temporal_network, pk.TemporalNetwork):
        edges_temporal = list(aggregated_network.edges())
        edges_all = edges_temporal
        edges_constant = list(set(edges_all).difference(edges_temporal))
    else:
        raise TypeError(
            "'temporal_network' must be of type TemporalNetowkr or PartiallyTemporalNetwork"
        )

    params_nodes = pk.standard_node_params(color_constant)
    del params_nodes["node_color"]  # will be set below
    param_labels = pk.standard_label_params(color_constant)

    def update_network(i):
        ax.clear()

        snapshot_network = temporal_network.network_at_time(
            time_index=i, output="weighted"
        )

        # constant network
        nx.draw_networkx_nodes(
            aggregated_network,
            node_color=color_constant,
            pos=pos,
            ax=ax,
            **params_nodes,
        )
        nx.draw_networkx_edges(
            snapshot_network,
            edgelist=edges_constant,
            edge_color=color_constant,
            pos=pos,
            ax=ax,
        )

        if with_labels:
            nx.draw_networkx_labels(aggregated_network, pos=pos, ax=ax, **param_labels)

        # changing edges
        weights = np.array(
            [
                w
                for u, v, w in snapshot_network.edges.data("weight")
                if (u, v) in edges_temporal
            ]
        )
        width_min = 0.7  # set minimum width for visualisation
        widths = np.maximum(weights * width_scale, width_min)
        nx.draw_networkx_edges(
            snapshot_network,
            edgelist=edges_temporal,
            edge_color=color_temporal,
            width=widths,
            pos=pos,
            ax=ax,
        )

        ax.set_title(f"Time: {i} min")
        sb.despine(left=True, bottom=True)

        custom_lines = [
            Line2D([0], [0], color=color_constant, lw=width_scale),
            Line2D([0], [0], color=color_temporal, lw=width_scale),
        ]

        ax.legend(custom_lines, ["Constant edges", "Temporal edges"])

    ani = animation.FuncAnimation(
        fig, update_network, frames=frames, interval=interval, blit=False
    )

    return ani
