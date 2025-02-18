from unittest import TestCase

import dynamic_programming


class Test(TestCase):
    def test_n_sum(self):
        result = dynamic_programming.n_sum(0)
        self.assertIs(result, 0)
        result = dynamic_programming.n_sum(1)
        self.assertIs(result, 1)
        result = dynamic_programming.n_sum(5)
        self.assertIs(result, 15)

