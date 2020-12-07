from unittest import TestCase
from main import solution_part_1, solution_part_2


class TestSolutoins(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1("testData.txt"), 4)

    def test_solution_part_2(self):
        self.assertEqual(solution_part_2("testData.txt"), 32)
        self.assertEqual(solution_part_2("testData_2.txt"), 126)
