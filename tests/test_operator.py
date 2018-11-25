import unittest
from unittest.mock import sentinel
from typing import Callable

from switch_case import Operator, _ as inst


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

    def test_alias(self):
        self.assertIsInstance(inst, Operator)

    def test_immutable(self):
        eq = inst == sentinel.val
        ne = inst != sentinel.val

        self.assertTrue(eq(sentinel.val))
        self.assertFalse(ne(sentinel.val))
