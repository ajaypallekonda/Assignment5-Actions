import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_function1(self):
        area = task.function1(3)
        self.assertEqual(area, (9 * math.pi))

    def test_function2(self):
        lists = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual((1, 8), task.function2(lists))

    def test_function3(self):
        date1 = [2020, 2, 1]
        date2 = [2020, 3, 15]

        self.assertEqual(task.function3(date1, date2), 43)


if __name__ == "__main__":
    unittest.main()
