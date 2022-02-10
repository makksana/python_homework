import math_functions
import unittest
print('Task 1', end='\n\n')

# Pick your solution to one of the exercises in this module.
# Design tests for this solution and
# write tests using unittest library.


class MathematicianTestCase(unittest.TestCase):

    def setUp(self):
        self.num = math_functions.Mathematician()

    def test_squeres_nums(self):
        sq = [3, 4, 6, 8, 10]
        sq2 = self.num.square_nums(sq)
        self.assertEqual(sq2, [9, 16, 36, 64, 100])

    def test_removed_positives(self):
        p = [-2, 15, -31, 45, 96]
        p1 = self.num.remove_positives(p)
        self.assertEqual(p1, [-2, -31])
        self.assertNotEqual(p1, [15, 45, 96])

    def test_filtered_leaps(self):
        leap = [2001, 1995, 2003, 1884]
        leap_years = self.num.filter_leaps(leap)
        self.assertEqual(leap_years, [1884])


if __name__ == '__main__':
    unittest.main()
