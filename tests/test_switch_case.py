import unittest
from functools import partial

from switch_case import switch, case, default, _


class TestSwitchCase(unittest.TestCase):
    def test_switch_case(self):
        reason = (
            switch
                | case(_ == 200) >> "OK"
                | case(_ == 500) >> "ERROR"
                | default        >> "UNKNOWN")

        self.assertEqual(reason(200), "OK")
        self.assertEqual(reason(500), "ERROR")
        self.assertEqual(reason(400), "UNKNOWN")
