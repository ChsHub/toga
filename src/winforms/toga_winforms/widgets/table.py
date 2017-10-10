from ..libs import *
from .base import Widget
from src.core.toga.widgets.table import Table

class Table(Widget):

    def create(self):
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
