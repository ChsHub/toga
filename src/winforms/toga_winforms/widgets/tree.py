from ..libs import WinForms

from toga.interface import Tree as TreeInterface

from .base import WidgetMixin


class Tree(TreeInterface, WidgetMixin):
    def __init__(self, headings, id=None, style=None):
        super(Tree, self).__init__(headings, id=id, style=style)

        self._tree = None
        self._columns = None
        self._data = None

        self._create()

    def create(self):

        self._container = self
        # Create a tree view.
        # The TreeView is scrollable by default in WinForms.
        self._impl = WinForms.TreeView()

        self._columns = []
        for heading in self.headings:
            pass
            # renderer = Gtk.CellRendererText()
            # column = Gtk.TreeViewColumn(heading, renderer, text=0)
            # self._table.append_column(column)

            # self._impl = Gtk.ScrolledWindow()
            # self._impl.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
            # self._impl.add(self._table)
            # self._impl.set_min_content_width(200)
            # self._impl.set_min_content_height(200)

    def insert(self, parent, index, *data):

        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        if parent is None:
            parent = self._impl

        if index is None:
            node = WinForms.TreeNode(data[0])

            parent.Nodes.Add(node)
        else:
            node = parent.Nodes.Insert(index, data[0])

        return node
