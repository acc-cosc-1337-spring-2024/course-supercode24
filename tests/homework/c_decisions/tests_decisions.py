import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_ration_calculation(self):
        self.assertAlmostEqual(get_options_ratio(5,20), 0.25)
        self.assertAlmostEqual(get_options_ratio(10,20), 0.5)

    def test_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(0.91), 'Excellent')
        self.assertEqual(get_faculty_rating(0.85), 'Very Good')
        self.assertEqual(get_faculty_rating(0.75), 'Good')
        self.assertEqual(get_faculty_rating(0.65), 'Needs Improvement')
        self.assertEqual(get_faculty_rating(0.59), 'Unacceptable')