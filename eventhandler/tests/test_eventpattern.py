from unittest import TestCase
from unittest.mock import MagicMock
from eventpattern import MainClass, Dataset


class TestEventPattern(TestCase):
    def test_event_pattern(self):
        main_class = MainClass()
        controller = main_class._controller
        dataset = Dataset()
        controller.on_modified = MagicMock()
        main_class.load_dataset(dataset)
        self.assertFalse(controller.on_modified.called)
        dataset.change_something()
        self.assertTrue(controller.on_modified.called)
