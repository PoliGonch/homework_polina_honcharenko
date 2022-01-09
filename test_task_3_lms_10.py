import unittest

import task_3_lms_10_function


class FunctionTestCase(unittest.TestCase):

    def test_function(self):
        test_list = task_3_lms_10_function.list_comprehension()
        self.assertEqual(test_list,
                         [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)])


if __name__ == '__main__':
    unittest.main()
