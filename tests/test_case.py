import unittest
from unittest.mock import MagicMock, sentinel

from switch_case import Case
from switch_case import case as case_factory


class TestCase(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(TypeError):
            case = Case()

    def test_match(self):
        mock = MagicMock(return_value=True)
        case = Case(predicate=mock)

        self.assertTrue(case.match(sentinel.val))
        mock.assert_called_once_with(sentinel.val)

    def test_resolve(self):
        mock = MagicMock(return_value=True)
        case = Case(predicate=mock)

        self.assertEqual(case >> sentinel.val, case)
        self.assertEqual(case.resolve(), sentinel.val)
        mock.assert_not_called()

    def test_resolve_without_value(self):
        case = Case(lambda x: True)
        with self.assertRaises(ValueError):
            case.resolve()

    def test_factory(self):
        mock = MagicMock(return_value=True)
        case = case_factory(mock)

        self.assertIsInstance(case, Case)
        self.assertTrue(case.match(sentinel.val))
        mock.assert_called_once_with(sentinel.val)
