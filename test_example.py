import unittest

import function_example


class NameTestCase(unittest.TestCase):

    def test_first_and_last_names(self):
        full = function_example.full_name('carl', 'johnson')
        full2 = function_example.full_name('cARL', 'jOHNSON')
        self.assertEqual(full, 'Carl Johnson')
        self.assertEqual(full2, 'Carl Johnson')


class SquaresTestCase(unittest.TestCase):

    def test_squares(self):
        l = [1, 2, 3, 4]
        l2 = function_example.squares(l)
        self.assertEqual(l2, [1, 4, 9, 16])

