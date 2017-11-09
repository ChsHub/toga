from ..libs import WinForms
from .base import Widget


class Table(Widget):
    def create(self):
        self._connections = []
        self._container = self
        self.native = WinForms.ListView()

        dataColumn = []
        for heading in self.interface.headings:
            col = WinForms.ColumnHeader()
            col.Text = heading
            dataColumn.append(col)

        self.native.View = WinForms.View.Details
        self.native.Columns.AddRange(dataColumn)

    def insert(self, index, *data):
        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        if index is None:
            listViewItem = WinForms.ListViewItem(data)
            self.native.Items.Add(listViewItem)
        else:
            listViewItem = WinForms.ListViewItem(data)
            self.native.Items.Insert(index, listViewItem)

    def refresh(self):

        if self.interface.data is not None:
            self.native.BeginUpdate()

            for row in self.interface.data.rows:
                list_view_item = WinForms.ListViewItem(row)
                self.native.Items.Add(list_view_item)

            self.native.EndUpdate()

    def set_on_select(self, handler):
        return
        for conn_id in self._connections:
            # Disconnect all other on_select handlers, so that if you reassign
            # the on_select, it doesn't trigger the old ones too.
            self.selection.disconnect(conn_id)
            self._connections.remove(conn_id)

        if handler is None:
            return

        def _handler(selection):
            tree_model, tree_iter = selection.get_selected()

            if tree_iter:
                tree_path = tree_model.get_path(tree_iter)
                index = tree_path.get_indices()[0]
                handler(self.table, row=index)
            else:
                handler(self.table, row=None)

        self._connections.append(self.selection.connect("changed", _handler))
