import numpy as np
from bokeh.models import CustomJS, Toolbar
from bokeh.models.tools import RangeTool

from ...core.util import isscalar
from ..links import (
    DataLink,
    Link,
    RangeToolLink,
    RectanglesTableLink,
    SelectionLink,
    VertexTableLink,
)
from ..plot import GenericElementPlot, GenericOverlayPlot


class LinkCallback:

    source_model = None
    target_model = None
    source_handles = []
    target_handles = []

    on_source_events = []
    on_source_changes = []

    on_target_events = []
    on_target_changes = []

    source_code = None
    target_code = None

    def __init__(self, root_model, link, source_plot, target_plot=None):
        self.root_model = root_model
        self.link = link
        self.source_plot = source_plot
        self.target_plot = target_plot
        self.validate()

        references = {k: v for k, v in link.param.values().items()
                      if k not in ('source', 'target', 'name')}

        for sh in self.source_handles+[self.source_model]:
            key = f'source_{sh}'
            references[key] = source_plot.handles[sh]

        for p, value in link.param.values().items():
            if p in ('name', 'source', 'target'):
                continue
            references[p] = value

        if target_plot is not None:
            for sh in self.target_handles+[self.target_model]:
                key = f'target_{sh}'
                references[key] = target_plot.handles[sh]

        if self.source_model in source_plot.handles:
            src_model = source_plot.handles[self.source_model]
            src_cb = CustomJS(args=references, code=self.source_code)
            for ch in self.on_source_changes:
                src_model.js_on_change(ch, src_cb)
            for ev in self.on_source_events:
                src_model.js_on_event(ev, src_cb)
            self.src_cb = src_cb
        else:
            self.src_cb = None

        if target_plot is not None and self.target_model in target_plot.handles and self.target_code:
            tgt_model = target_plot.handles[self.target_model]
            tgt_cb = CustomJS(args=references, code=self.target_code)
            for ch in self.on_target_changes:
                tgt_model.js_on_change(ch, tgt_cb)
            for ev in self.on_target_events:
                tgt_model.js_on_event(ev, tgt_cb)
            self.tgt_cb = tgt_cb
        else:
            self.tgt_cb = None

    @classmethod
    def find_links(cls, root_plot):
        """
        Traverses the supplied plot and searches for any Links on
        the plotted objects.
        """
        plot_fn = lambda x: isinstance(x, (GenericElementPlot, GenericOverlayPlot))
        plots = root_plot.traverse(lambda x: x, [plot_fn])
        potentials = [cls.find_link(plot) for plot in plots]
        source_links = [p for p in potentials if p is not None]
        found = []
        for plot, links in source_links:
            for link in links:
                if not link._requires_target:
                    # If link has no target don't look further
                    found.append((link, plot, None))
                    continue
                potentials = [cls.find_link(p, link) for p in plots]
                tgt_links = [p for p in potentials if p is not None]
                if tgt_links:
                    found.append((link, plot, tgt_links[0][0]))
        return found

    @classmethod
    def find_link(cls, plot, link=None):
        """
        Searches a GenericElementPlot for a Link.
        """
        registry = Link.registry.items()
        for source in plot.link_sources:
            if link is None:
                links = [
                    l for src, links in registry for l in links
                    if src is source or (src._plot_id is not None and
                                         src._plot_id == source._plot_id)]
                if links:
                    return (plot, links)
            elif ((link.target is source) or
                (link.target is not None and
                    link.target._plot_id is not None and
                    link.target._plot_id == source._plot_id)):
                return (plot, [link])

    def validate(self):
        """
        Should be subclassed to check if the source and target plots
        are compatible to perform the linking.
        """


class RangeToolLinkCallback(LinkCallback):
    """
    Attaches a RangeTool to the source plot and links it to the
    specified axes on the target plot
    """

    def __init__(self, root_model, link, source_plot, target_plot):
        toolbars = list(root_model.select({'type': Toolbar}))
        axes = {}

        for axis in ('x', 'y'):
            if axis not in link.axes:
                continue

            axes[f'{axis}_range'] = target_plot.handles[f'{axis}_range']
            bounds = getattr(link, f'bounds{axis}', None)
            if bounds is None:
                continue

            start, end = bounds
            if start is not None:
                axes[f'{axis}_range'].start = start
                axes[f'{axis}_range'].reset_start = start
            if end is not None:
                axes[f'{axis}_range'].end = end
                axes[f'{axis}_range'].reset_end = end

        tool = RangeTool(**axes)
        source_plot.state.add_tools(tool)
        if toolbars:
            toolbars[0].tools.append(tool)


class DataLinkCallback(LinkCallback):
    """
    Merges the source and target ColumnDataSource
    """

    def __init__(self, root_model, link, source_plot, target_plot):
        src_cds = source_plot.handles['source']
        tgt_cds = target_plot.handles['source']
        if src_cds is tgt_cds:
            return

        src_len = [len(v) for v in src_cds.data.values()]
        tgt_len = [len(v) for v in tgt_cds.data.values()]
        if src_len and tgt_len and (src_len[0] != tgt_len[0]):
            raise ValueError('DataLink source data length must match target '
                            'data length, found source length of %d and '
                            'target length of %d.' % (src_len[0], tgt_len[0]))

        # Ensure the data sources are compatible (i.e. overlapping columns are equal)
        for k, v in tgt_cds.data.items():
            if k not in src_cds.data:
                continue
            v = np.asarray(v)
            col = np.asarray(src_cds.data[k])
            if len(v) and isinstance(v[0], np.ndarray):
                continue # Skip ragged arrays
            if not ((isscalar(v) and v == col) or
                    (v.dtype.kind not in 'iufc' and (v==col).all()) or
                    np.allclose(v, np.asarray(src_cds.data[k]), equal_nan=True)):
                raise ValueError('DataLink can only be applied if overlapping '
                                 'dimension values are equal, %s column on source '
                                 'does not match target' % k)

        src_cds.data.update(tgt_cds.data)
        renderer = target_plot.handles.get('glyph_renderer')
        if renderer is None:
            pass
        elif 'data_source' in renderer.properties():
            renderer.update(data_source=src_cds)
        else:
            renderer.update(source=src_cds)
        target_plot.handles['source'] = src_cds
        target_plot.handles['cds'] = src_cds
        for callback in target_plot.callbacks:
            callback.initialize(plot_id=root_model.ref['id'])


class SelectionLinkCallback(LinkCallback):

    source_model = 'selected'
    target_model = 'selected'

    on_source_changes = ['indices']
    on_target_changes = ['indices']

    source_handles = ['cds']
    target_handles = ['cds']

    source_code = """
    target_selected.indices = source_selected.indices
    target_cds.properties.selected.change.emit()
    """

    target_code = """
    source_selected.indices = target_selected.indices
    source_cds.properties.selected.change.emit()
    """

class RectanglesTableLinkCallback(DataLinkCallback):

    source_model = 'cds'
    target_model = 'cds'

    source_handles = ['glyph']

    on_source_changes = ['selected', 'data']
    on_target_changes = ['patching']

    source_code = """
    target_cds.data[columns[0]] = source_cds.data[source_glyph.left.field]
    target_cds.data[columns[1]] = source_cds.data[source_glyph.bottom.field]
    target_cds.data[columns[2]] = source_cds.data[source_glyph.right.field]
    target_cds.data[columns[3]] = source_cds.data[source_glyph.top.field]
    """

    target_code = """
    source_cds.data['left'] = target_cds.data[columns[0]]
    source_cds.data['bottom'] = target_cds.data[columns[1]]
    source_cds.data['right'] = target_cds.data[columns[2]]
    source_cds.data['top'] = target_cds.data[columns[3]]
    """

    def __init__(self, root_model, link, source_plot, target_plot=None):
        DataLinkCallback.__init__(self, root_model, link, source_plot, target_plot)
        LinkCallback.__init__(self, root_model, link, source_plot, target_plot)
        columns = [kd.name for kd in source_plot.current_frame.kdims]
        self.src_cb.args['columns'] = columns
        self.tgt_cb.args['columns'] = columns


class VertexTableLinkCallback(LinkCallback):

    source_model = 'cds'
    target_model = 'cds'

    on_source_changes = ['selected', 'data', 'patching']
    on_target_changes = ['data', 'patching']

    source_code = """
    var index = source_cds.selected.indices[0];
    if (index == undefined) {
      var xs_column = [];
      var ys_column = [];
    } else {
      var xs_column = source_cds.data['xs'][index];
      var ys_column = source_cds.data['ys'][index];
    }
    if (xs_column == undefined) {
      var xs_column = [];
      var ys_column = [];
    }
    var xs = []
    var ys = []
    var empty = []
    for (var i = 0; i < xs_column.length; i++) {
      xs.push(xs_column[i])
      ys.push(ys_column[i])
      empty.push(null)
    }
    var [x, y] = vertex_columns
    target_cds.data[x] = xs
    target_cds.data[y] = ys
    var length = xs.length
    for (var col in target_cds.data) {
      if (vertex_columns.indexOf(col) != -1) { continue; }
      else if (col in source_cds.data) {
        var path = source_cds.data[col][index];
        if ((path == undefined)) {
          var data = empty;
        } else if (path.length == length) {
          var data = source_cds.data[col][index];
        } else {
          var data = empty;
        }
      } else {
        var data = empty;
      }
      target_cds.data[col] = data;
    }
    target_cds.change.emit()
    target_cds.data = target_cds.data
    """

    target_code = """
    if (!source_cds.selected.indices.length) { return }
    var [x, y] = vertex_columns
    var xs_column = target_cds.data[x]
    var ys_column = target_cds.data[y]
    var xs = []
    var ys = []
    var points = []
    for (var i = 0; i < xs_column.length; i++) {
      xs.push(xs_column[i])
      ys.push(ys_column[i])
      points.push(i)
    }
    var index = source_cds.selected.indices[0]
    var xpaths = source_cds.data['xs']
    var ypaths = source_cds.data['ys']
    var length = source_cds.data['xs'].length
    for (var col in target_cds.data) {
      if ((col == x) || (col == y)) { continue; }
      if (!(col in source_cds.data)) {
        var empty = []
        for (var i = 0; i < length; i++)
          empty.push([])
        source_cds.data[col] = empty
      }
      source_cds.data[col][index] = target_cds.data[col]
      for (var p of points) {
        for (var pindex = 0; pindex < xpaths.length; pindex++) {
          if (pindex != index) { continue }
          var xs = xpaths[pindex]
          var ys = ypaths[pindex]
          var column = source_cds.data[col][pindex]
          if (column.length != xs.length) {
            for (var ind = 0; ind < xs.length; ind++) {
              column.push(null)
            }
          }
          for (var ind = 0; ind < xs.length; ind++) {
            if ((xs[ind] == xpaths[index][p]) && (ys[ind] == ypaths[index][p])) {
              column[ind] = target_cds.data[col][p]
              xs[ind] = xs[p];
              ys[ind] = ys[p];
            }
          }
        }
      }
    }
    xpaths[index] = xs;
    ypaths[index] = ys;
    source_cds.change.emit()
    source_cds.properties.data.change.emit();
    source_cds.data = source_cds.data
    """


callbacks = Link._callbacks['bokeh']

callbacks[RangeToolLink] = RangeToolLinkCallback
callbacks[DataLink] = DataLinkCallback
callbacks[SelectionLink] = SelectionLinkCallback
callbacks[VertexTableLink] = VertexTableLinkCallback
callbacks[RectanglesTableLink] = RectanglesTableLinkCallback
