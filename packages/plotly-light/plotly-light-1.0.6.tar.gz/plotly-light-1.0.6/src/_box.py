from typing import Union, Optional, List, Tuple
import plotly.graph_objects as go
from . import default


def box(data: Union[List, Tuple],
        name: Optional[str] = None,
        col: Optional[str] = None,
        opacity: float = 1,
        show_points: bool = False,
        only_points: bool = False,
        marker_size: Optional[float] = None,
        show_legend: bool = False,
        show_init: bool = True) -> go.Box:
    """Create a simple Trace object of a box plot.

    positional arguments:
      @ data : Sequence (of sequence(s)) of data values.

    optional arguments:
      @ name        : Display name of the trace in legend and plot.
      @ col         : Color of the plot.
      @ opacity     : Opacity of the plot.
      @ show_points : Plot markers as well as the box.
      @ only_points : Plot only markers and hide the box.
      @ show_legend : Show this trace in legend.
      @ show_init   : Show this trace initially.
    """
    return go.Box(y=data,
                  boxpoints='all' if show_points or only_points else None,
                  pointpos=0 if only_points else None,
                  hoveron='points' if only_points else None,
                  fillcolor="rgba(255,255,255,0)" if only_points else None,
                  line={"color": "rgba(255,255,255,0)"} if only_points else None,
                  marker={"color": default.layout["colorway"][0]
                          if col is None and only_points else col,
                          "size": marker_size},
                  opacity=opacity,
                  name=name,
                  showlegend=show_legend,
                  visible=None if show_init else "legendonly")


def violin(data: Union[List, Tuple],
           name: Optional[str] = None,
           col: Optional[str] = None,
           opacity: float = 1,
           show_box: bool = False,
           show_points: bool = False,
           show_legend: bool = False,
           show_init: bool = True) -> go.Box:
    """Create a simple Trace object of a box plot.

    positional arguments:
      @ data : Sequence (of sequence(s)) of data values.

    optional arguments:
      @ name        : Display name of the trace in legend and plot.
      @ col         : Color of the plot.
      @ opacity     : Opacity of the plot.
      @ show_box    : Show the box plot.
      @ show_points : Plot markers as well as the box.
      @ show_legend : Show this trace in legend.
      @ show_init   : Show this trace initially.
    """
    return go.Violin(y=data,
                     box_visible=show_box,
                     points="all" if show_points else None,
                     marker={"color": col},
                     opacity=opacity,
                     name=name,
                     showlegend=show_legend,
                     visible=None if show_init else "legendonly")
