import unittest
from unittest.mock import MagicMock, call, sentinel

from switch_case import Case, Switch
from switch_case import switch as inst


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

    def test_switch_with_expr(self):
        truthy = MagicMock(return_value=True)
        switch = Switch()(sentinel.expr) | Case(truthy) >> sentinel.smth
        self.assertEqual(switch(), sentinel.smth)
        truthy.assert_called_once_with(sentinel.expr)

    def test_switch_with_2_expr(self):
        switch = Switch()(sentinel.expr1) | Case(lambda x: True) >> sentinel.smth
        with self.assertRaises(ValueError):
            switch(sentinel.expr2)

    def test_switch_without_expr(self):
        switch = Switch([Case(lambda x: True) >> sentinel.smth])
        with self.assertRaises(ValueError):
            switch()

    def test_switch_without_cases(self):
        switch = Switch(cases=[], expr=sentinel.expr)
        with self.assertRaises(ValueError):
            switch()

    def test_switch_resolve(self):
        truthy = MagicMock(return_value=True)
        switch = inst(sentinel.expr) | Case(truthy) >> sentinel.smth
        self.assertEqual(~switch, sentinel.smth)
        truthy.assert_called_once_with(sentinel.expr)

    def test_alias(self):
        self.assertIsInstance(inst, Switch)

    def test_immutable(self):
        switch1 = inst | Case(lambda x: True) >> sentinel.exact1
        switch2 = inst | Case(lambda x: True) >> sentinel.exact2

        self.assertEqual(switch1(sentinel.any), sentinel.exact1)
        self.assertEqual(switch2(sentinel.any), sentinel.exact2)

    def test_immutable_expr(self):
        truthy1 = MagicMock(return_value=True)
        truthy2 = MagicMock(return_value=True)
        switch1 = inst(sentinel.expr1) | Case(truthy1) >> sentinel.exact1
        switch2 = inst(sentinel.expr2) | Case(truthy2) >> sentinel.exact2

        self.assertEqual(switch1(), sentinel.exact1)
        truthy1.assert_called_once_with(sentinel.expr1)

        self.assertEqual(switch2(), sentinel.exact2)
        truthy2.assert_called_once_with(sentinel.expr2)
