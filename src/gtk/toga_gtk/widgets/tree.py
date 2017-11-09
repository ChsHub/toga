from gi.repository import Gtk
from .base import Widget


class Tree(Widget):
    def create(self):
        self.tree = None
        self.columns = None

        self.data = Gtk.TreeStore(*[str for h in self.interface.headings])
        # Create a tree view, and put it in a scroll view.
        # The scroll view is the _impl, because it's the outer container.
        self.table = Gtk.TreeView(self.data)

        self.columns = []
        for heading in self.interface.headings:
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(heading, renderer, text=0)
            self.table.append_column(column)

        self.native = Gtk.ScrolledWindow()
        self.native.interface = self.interface
        self.native.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.native.add(self.table)
        self.native.set_min_content_width(200)
        self.native.set_min_content_height(200)

    def insert(self, parent, index, *data):
        if len(data) != len(self.interface.headings):
            raise Exception('Data size does not match number of headings')

        if index is None:
            node = self.data.append(parent, data)
        else:
            node = self.data.insert(parent, index, data)
        return node


    def insert_node(self, node):
        raise NotImplementedError()

    def remove_node(self, node):
        raise NotImplementedError()

    def refresh(self):
        raise NotImplementedError()

    def refresh_node(self, node):
        raise NotImplementedError()

    def set_on_select(self, handler):
        pass