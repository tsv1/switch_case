import unittest
from unittest.mock import MagicMock, sentinel

from switch_case.curry import curry


class TestCurry(unittest.TestCase):
    def test_curry_without_args(self):
        mock = MagicMock(return_value=sentinel.res)
        curried = curry(mock)

        self.assertEqual(curried(), sentinel.res)
        mock.assert_called_once_with()

    def test_curry_with_args(self):
        mock = MagicMock(return_value=sentinel.res)
        curried = curry(mock, sentinel.arg1)

        self.assertEqual(curried(sentinel.arg2), sentinel.res)
        mock.assert_called_once_with(sentinel.arg2, sentinel.arg1)

    def test_curry_with_kwargs(self):
        mock = MagicMock(return_value=sentinel.res)
        curried = curry(mock, key1=sentinel.kwarg1)

        self.assertEqual(curried(key2=sentinel.kwarg2), sentinel.res)
        mock.assert_called_once_with(key1=sentinel.kwarg1, key2=sentinel.kwarg2)

    def test_curry_with_args_and_kwargs(self):
        mock = MagicMock(return_value=sentinel.res)
        curried = curry(mock, sentinel.arg1, key1=sentinel.kwarg1)

        self.assertEqual(curried(sentinel.arg2, key1=sentinel.kwarg2), sentinel.res)
        mock.assert_called_once_with(sentinel.arg2, sentinel.arg1, key1=sentinel.kwarg2)
