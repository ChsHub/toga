import toga
from colosseum import CSS

from src.winforms.toga_winforms.widgets.splitcontainer import SplitContainer


# from src.gtk.toga_gtk.widgets.tree import Tree


class SplitContainerTry(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        tree = SplitContainer()



        self.main_window.content = tree
        self.main_window.show()


def main():
    return SplitContainerTry('Converter', 'org.pybee.converter')


if __name__ == '__main__':
    main().main_loop()
