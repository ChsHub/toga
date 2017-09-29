import toga
from colosseum import CSS

from src.winforms.toga_winforms.widgets.tree import Tree
#from src.gtk.toga_gtk.widgets.tree import Tree


class TreeTry(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        tree = Tree(['Navigate', 'Size'])

        tree.insert(None, None, 'root1', '5mb')

        root2 = tree.insert(None, None, 'root2', '5mb')

        tree.insert(root2, None, 'root2.1', '5mb')
        root2_2 = tree.insert(root2, None, 'root2.2', "12")

        tree.insert(root2_2, None, 'root2.2.1', "1212")
        tree.insert(root2_2, None, 'root2.2.3', '23')
        tree.insert(root2_2, 1, 'root2.2.2', '23')

        self.main_window.content = tree
        self.main_window.show()


def main():
    return TreeTry('Converter', 'org.pybee.converter')


if __name__ == '__main__':
    main().main_loop()
