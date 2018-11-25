import unittest
from unittest.mock import MagicMock, sentinel, call

from switch_case import Switch, Case, switch as inst


class TestSwitch(unittest.TestCase):
    def test_resolve_single_truthy(self):
        truthy = MagicMock(return_value=True)
        switch = Switch([
            Case(truthy) >> sentinel.exact
        ])
        self.assertEqual(switch(sentinel.any), sentinel.exact)
        truthy.assert_called_once_with(sentinel.any)

    def test_resolve_single_falsy(self):
        falsy = MagicMock(return_value=False)
        switch = Switch([
            Case(falsy) >> sentinel.exact
        ])
        with self.assertRaises(ValueError):
            switch(sentinel.any)
        falsy.assert_called_once_with(sentinel.any)

    def test_resolve_multiple_truthy(self):
        truthy = MagicMock(return_value=True)
        switch = Switch([
            Case(truthy) >> sentinel.exact1,
            Case(truthy) >> sentinel.exact2
        ])
        self.assertEqual(switch(sentinel.any), sentinel.exact1)
        truthy.assert_called_once_with(sentinel.any)

    def test_resolve_multiple_falsy(self):
        falsy = MagicMock(return_value=False)
        switch = Switch([
            Case(falsy) >> sentinel.exact1,
            Case(falsy) >> sentinel.exact2
        ])
        with self.assertRaises(ValueError):
            switch(sentinel.any)
        falsy.assert_has_calls([
            call(sentinel.any),
            call(sentinel.any)
        ])

    def test_resolve_multiple_truthy_falsy(self):
        truthy = MagicMock(return_value=True)
        falsy = MagicMock(return_value=False)
        switch = Switch([
            Case(falsy) >> sentinel.exact1,
            Case(falsy) >> sentinel.exact2,
            Case(truthy) >> sentinel.exact3,
            Case(truthy) >> sentinel.exact4
        ])
        self.assertEqual(switch(sentinel.any), sentinel.exact3)
        falsy.assert_has_calls([
            call(sentinel.any),
            call(sentinel.any)
        ])
        truthy.assert_called_once_with(sentinel.any)

    def test_switch_single_case(self):
        switch = Switch() | Case(lambda x: True) >> sentinel.exact
        self.assertEqual(switch(sentinel.any), sentinel.exact)

    def test_switch_multiple_cases(self):
        switch = (
            Switch()
                | Case(lambda x: False) >> sentinel.exact1
                | Case(lambda x: True) >> sentinel.exact2)
        self.assertEqual(switch(sentinel.any), sentinel.exact2)

    def test_alias(self):
        self.assertIsInstance(inst, Switch)
        with self.assertRaises(ValueError):
            inst(sentinel.any)

    def test_immutable(self):
        switch1 = inst | Case(lambda x: True) >> sentinel.exact1
        switch2 = inst | Case(lambda x: True) >> sentinel.exact2

        self.assertEqual(switch1(sentinel.any), sentinel.exact1)
        self.assertEqual(switch2(sentinel.any), sentinel.exact2)
