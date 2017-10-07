import toga
from colosseum import CSS

from src.winforms.toga_winforms.dialogs import save_file


class OptionContainerTry(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        button = toga.Button("TEST", on_press=lambda x: save_file(self.main_window, "Open", "", "*"))
        self.main_window.content = button
        self.main_window.show()



def main():
    return OptionContainerTry('Converter', 'org.pybee.converter')


if __name__ == '__main__':
    main().main_loop()
