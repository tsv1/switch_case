import unittest
from unittest.mock import sentinel
from typing import Callable

from switch_case import Operator, _ as inst


class TestOperator(unittest.TestCase):
    def test_eq(self):
        predicate = Operator() == sentinel.val

        self.assertIsInstance(predicate, Callable)
        self.assertTrue(predicate(sentinel.val))

        self.assertFalse(predicate(sentinel.not_val))

    def test_ne(self):
        predicate = Operator() != sentinel.val

        self.assertIsInstance(predicate, Callable)
        self.assertFalse(predicate(sentinel.val))

        self.assertTrue(predicate(sentinel.not_val))

    def test_alias(self):
        self.assertIsInstance(inst, Operator)

    def test_immutable(self):
        eq = inst == sentinel.val
        ne = inst != sentinel.val

        self.assertTrue(eq(sentinel.val))
        self.assertFalse(ne(sentinel.val))
