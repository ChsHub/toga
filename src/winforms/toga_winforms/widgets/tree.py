from ..libs import *
from .base import Widget

import toga


class ExtendedTreeNode(WinForms.UserControl):
    def __init__(self, data):
        super().__init__(data)
        #self.AAtree_node = WinForms.TreeNode()ListViewItem
        self.ControlAdded = WinForms.TreeView.ControlAdded


class ExtendedTree(WinForms.UserControl):
    def __init__(self):
        super().__init__()

    def Add1(self, Node):

        WinForms.TreeView.Add(Node)
        # WinForms.ListView.ColumnHeaderCollection(WinForms.ListView)


class Tree(Widget):
    def __init__(self, headings, id=None, style=None):
        super(Tree, self).__init__(headings, id=id, style=style)
        self._create()

    def create(self):
        self._container = self
        # Create a tree view.
        # The TreeView is scrollable by default in WinForms.

        self._impl = ExtendedTree()
        self._impl2 = WinForms.TreeView()
        dataColumn = []
        for heading in self.headings:
            col = WinForms.ColumnHeader()
            col.Text = heading
            dataColumn.append(col)

        self._impl.View = WinForms.View.Details
        self._impl.Columns.AddRange(dataColumn)

    def insert(self, parent, index, *data):

        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        if parent is None:
            parent = self._impl

        if index is None:
            node = ExtendedTreeNode(data)
            parent.Add1(node)
        else:
            node = parent.Items.Insert(index, data)

        return node
        """
    def _update_layout(self):
        pass

    def _set_app(self, app):
        pass

    def _set_window(self, window):
        pass

    def _set_container(self, window):
        pass
    """
