# coding:utf-8
import unittest
import src.fizzbuzz as fb

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_normal(self):
        self.assertEqual(1, fb.fizzbuzz(1))

    def test_fizz(self):
        self.assertEqual("Fizz", fb.fizzbuzz(3))

    def test_buzz(self):
        self.assertEqual("Buzz", fb.fizzbuzz(5))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fb.fizzbuzz(15))


if __name__ == "__main__":
    unittest.main()
