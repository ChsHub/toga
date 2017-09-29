import toga
from colosseum import CSS

from src.winforms.toga_winforms.widgets.table import Table
#from src.gtk.toga_gtk.widgets.tree import Tree


class TreeTable(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        tree = Table(['Navigate', 'Size'])

        tree.insert(None, 'root1', '5mb')

        tree.insert( None, 'root2', '5mb')

        tree.insert(None,  'root2.1', '5mb')
        tree.insert(None,  'root2.2', "12")

        tree.insert( None, 'root2.2.1', "1212")
        tree.insert(None,  'root2.2.3', '23')
        tree.insert( None, 'root2.2.2', '23')

        self.main_window.content = tree
        self.main_window.show()


def main():
    return TreeTable('Converter', 'org.pybee.converter')


if __name__ == '__main__':
    main().main_loop()
