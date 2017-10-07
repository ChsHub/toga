from toga.interface import Table as TableInterface

from ..libs import WinForms
from .base import WidgetMixin      

class Table(TableInterface, WidgetMixin):

    def __init__(self, headings, id=None, style=None, on_select=None):
        super(Table, self).__init__(headings, id=id, style=style)
        self._create()

    def create(self):
        self._impl = WinForms.ListView()

        dataColumn = []
        for heading in self.headings:
            col = WinForms.ColumnHeader()
            col.Text = heading
            dataColumn.append(col)

        self._impl.View = WinForms.View.Details
        self._impl.Columns.AddRange(dataColumn)
 
    def insert(self, index, *data):
        if len(data) != len(self.headings):
            raise Exception('Data size does not match number of headings')

        if index is None:
            listViewItem = WinForms.ListViewItem(data)
            self._impl.Items.Add(listViewItem)  
        else:
            listViewItem = WinForms.ListViewItem(data)
            self._impl.Items.Insert(index, listViewItem)  
         
    def rehint(self):
        # Width & height of a label is known and fixed.
        # self._impl.Size = Size(0, 0)
        print("REHINT label", self, self._impl.PreferredSize)

        self.style.hint(
            min_width=100,
            min_height=100,
            height=self._impl.PreferredSize.Height,
            width=self._impl.PreferredSize.Width
        )
