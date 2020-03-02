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
        list = [1,2,3,4,5,6,7,8]
        self.assertEqual((1,8), task.function2(list))


if __name__ == "__main__":
    unittest.main()
