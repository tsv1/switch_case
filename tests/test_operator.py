import unittest
from typing import Callable
from unittest.mock import MagicMock, sentinel

from switch_case import Operator
from switch_case import _ as inst


class TestOperator(unittest.TestCase):
    def test_eq(self):
        predicate = Operator() == 0

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(0))
        self.assertFalse(predicate(1))

    def test_ne(self):
        predicate = Operator() != 0

        self.assertIsInstance(predicate, Callable)
        self.assertFalse(predicate(0))
        self.assertTrue(predicate(1))

    def test_lt(self):
        predicate = Operator() < 0

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(-1))
        self.assertFalse(predicate(1))
        self.assertFalse(predicate(0))

    def test_le(self):
        predicate = Operator() <= 0

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(-1))
        self.assertTrue(predicate(0))
        self.assertFalse(predicate(1))

    def test_gt(self):
        predicate = Operator() > 0

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(1))
        self.assertFalse(predicate(0))
        self.assertFalse(predicate(-1))

    def test_ge(self):
        predicate = Operator() >= 0

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(1))
        self.assertTrue(predicate(0))
        self.assertFalse(predicate(-1))

    def test_curry(self):
        mock = MagicMock(return_value=sentinel.res)
        curried = Operator()(mock, sentinel.arg1, key1=sentinel.kwarg1)

        self.assertEqual(curried(sentinel.arg2, key1=sentinel.kwarg2), sentinel.res)
        mock.assert_called_once_with(sentinel.arg2, sentinel.arg1, key1=sentinel.kwarg2)

    def test_infix(self):
        mock = MagicMock(return_value=sentinel.res)
        predicate = Operator() /mock/ sentinel.arg1

        self.assertIsInstance(predicate, Callable)
        self.assertEqual(predicate(sentinel.arg2), sentinel.res)
        mock.assert_called_once_with(sentinel.arg2, sentinel.arg1)

    def test_alias(self):
        self.assertIsInstance(inst, Operator)

    def test_immutable(self):
        eq = inst == sentinel.val
        ne = inst != sentinel.val

        self.assertTrue(eq(sentinel.val))
        self.assertFalse(ne(sentinel.val))
