from unittest import TestCase
from unittest.mock import MagicMock
from baghandler import Observable, Observer


class TestBagHandler(TestCase):
    def test_bag_handler(self):
        observable = Observable()
        observer = Observer(observable)
        observer.notify = MagicMock()
        self.assertEqual(observable._observers, [observer])
        observable.notify_observer('test')
        self.assertTrue(observer.notify.called)

