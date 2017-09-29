#import src.core.toga as toga
import unittest
from colosseum import CSS
import toga
#from src.winforms.toga_winforms.widgets.tree import Tree
#from src.gtk.toga_gtk.widgets.tree import Tree


class TreeTest(toga.App):


    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        tree = toga.Tree(['Navigate'])

        tree.insert(None, None, 'root1')

        root2 = tree.insert(None, None, 'root2')

        tree.insert(root2, None, 'root2.1')
        root2_2 = tree.insert(root2, None, 'root2.2')

        tree.insert(root2_2, None, 'root2.2.1')
        tree.insert(root2_2, None, 'root2.2.2')
        tree.insert(root2_2, None, 'root2.2.3')


        self.main_window.content = tree
        self.main_window.show()


def main():
    return TreeTest('Converter', 'org.pybee.converter')


#if __name__ == '__main__':
    #main().main_loop()


class TestTree(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()