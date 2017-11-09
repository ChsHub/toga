import unittest

from colosseum import CSS

import toga
import toga_dummy
from toga_dummy.utils import TestCase


class PointTests(unittest.TestCase):
    def setUp(self):
        self.top = 50
        self.left = 100
        self.point = toga.Point(self.top, self.left)

    def test_point__repr__(self):
        self.assertEqual(self.point.__repr__(), '<Point (100,50)>')

    def test_point_left(self):
        self.assertEqual(self.point.left, 100)

    def test_point_top(self):
        self.assertEqual(self.point.top, 50)


class LayoutTests(TestCase):
    def setUp(self):
        super().setUp()

        self.widget = toga.Widget(factory=toga_dummy.factory)
        self.layout = toga.Layout(self.widget)

    def test_instantiation(self):
        self.assertEqual(self.layout.node, self.widget)

    def test_layout__repr__with_node(self):
        self.layout.width = 10
        self.layout.height = 20
        self.layout.left = 30
        self.layout.top = 40
        self.assertEqual(self.layout.__repr__(), '<Layout (dirty) (10x20 @ 30,40)>')

    def test_layout__repr__with_node_None(self):
        layout = toga.Layout(None)
        self.assertEqual(layout.__repr__(), '<Layout (dirty) (NonexNone @ 0,0)>')

    def test_layout__eq__(self):
        self.assertTrue(self.layout == self.layout)

    def test_layout_rest(self):
        self.layout.width = 100
        self.layout.height = 100
        self.layout.top = 100
        self.layout.left = 100
        self.assertEqual(self.layout.width, 100)
        self.assertEqual(self.layout.height, 100)
        self.assertEqual(self.layout.top, 100)
        self.assertEqual(self.layout.left, 100)
        self.layout.reset()
        self.assertEqual(self.layout.width, None)
        self.assertEqual(self.layout.height, None)
        self.assertEqual(self.layout.top, 0)
        self.assertEqual(self.layout.left, 0)

    def test_layout_dirty(self):
        self.layout.dirty = True
        self.assertTrue(self.layout.dirty)
        self.layout.dirty = False
        self.assertFalse(self.layout.dirty)
        self.layout.dirty = None
        self.assertIsNone(self.layout.dirty)

    def test_layout_right(self):
        self.layout.left = 50
        self.layout.width = 50
        self.assertEqual(self.layout.right, 100)

    def test_layout_bottom(self):
        self.layout.top = 50
        self.layout.height = 50
        self.assertEqual(self.layout.bottom, 100)

    def test_layout_absolute(self):
        pass

    def test_layout_origin(self):
        origin = self.layout.origin
        self.assertEqual(origin.top, 0)
        self.assertEqual(origin.left, 0)


class WidgetTests(TestCase):
    def setUp(self):
        super().setUp()

        self.id = 'widget_id'
        self.style = CSS(padding=666)

        self.widget = toga.Widget(id=self.id,
                                  style=self.style,
                                  factory=toga_dummy.factory)

    def test_arguments_were_set_correctly(self):
        self.assertEqual(self.widget.id, self.id)
        self.assertEqual(self.widget.style.padding, self.style.padding)

    def test_create_widget_with_no_style(self):
        widget = toga.Widget(factory=toga_dummy.factory)
        self.assertTrue(isinstance(widget.style, CSS))

    def test_adding_children(self):
        """
        """
        self.assertEqual(self.widget.children, [], 'No child was added, should return a empty list.')
        # Create a child widget to add to the our widget.
        child = toga.Widget(factory=toga_dummy.factory)

        with self.assertRaises(ValueError, msg='Widget cannot have children.'):
            self.widget.add(child)

        # Deliberately set widget._children = [] to allow it to have children.
        # Only for test purposes!
        self.widget._children = []
        self.widget.add(child)
        self.assertEqual(self.widget.children, [child])
