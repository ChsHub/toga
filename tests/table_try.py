import toga
#from colosseum import CSS

from src.winforms.toga_winforms.widgets.table import Table
# from src.gtk.toga_gtk.widgets.tree import Tree


def build(app):
    #self.main_window = toga.MainWindow(self.name)
   # self.main_window.app = self
    box = toga.Box()

    table = toga.Table(['Navigate', 'Size'])
#    table.style = CSS(height=50, width=614)

    table.insert(None, 'root1', '5mb')

    table.insert(None, 'root2', '5mb')

    table.insert(None, 'root2.1', '5mb')
    table.insert(None, 'root2.2', "12")

    table.insert(None, 'root2.2.1', "1212")
    table.insert(None, 'root2.2.3', '23')
    table.insert(None, 'root2.2.2', '23')

    box.add(toga.Label("Hello"))
    box.add(table)
    box.add(toga.Label("World"))
   # self.main_window.content = box
   # self.main_window.show()
    return table


def main():
    return toga.App('First App', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
