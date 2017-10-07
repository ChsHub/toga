import unittest
from unittest.mock import MagicMock, Mock
import toga
import toga_dummy


class TestNumberInput(unittest.TestCase):
    def setUp(self):
        self.factory = MagicMock()
        self.factory.NumberInput = MagicMock(return_value=MagicMock(spec=toga_dummy.factory.NumberInput))

        self.nr_input = toga.NumberInput(factory=self.factory)

    def test_factory_called(self):
        self.factory.NumberInput.assert_called_once_with(interface=self.nr_input)
