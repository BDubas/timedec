from timedec import timer
import unittest

class TestTimer(unittest.TestCase):
    DEFAULT_NUMBER = 10000

    def fake_func(self):
        return "hello"

    def test_correct_work(self):
        result = timer(self.DEFAULT_NUMBER)(self.fake_func)()
        print(result)
        self.assertEqual(result.returned, "hello")

    def test_wrapper(self):
        result = timer(self.DEFAULT_NUMBER)(self.fake_func)
        self.assertEqual(result.__name__, self.fake_func.__name__)
