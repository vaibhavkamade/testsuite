import unittest

from calculator import Calculator


class calculatorTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()
        

    def test_add(self):
        self.assertEqual(Calculator.add(10,20),30)
        self.assertEqual(Calculator.add(-10,-20),-30)
        self.assertEqual(Calculator.add(-10,20),10)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(20,10),10)
        self.assertEqual(Calculator.subtract(-20,-10),-10)
        self.assertEqual(Calculator.subtract(-20,10),-30)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(5,4),20)
        self.assertEqual(Calculator.multiply(-5,-4),20)
        self.assertEqual(Calculator.multiply(-5,4),-20)

    def test_divide(self):
        self.assertEqual(Calculator.divide(40,20),2)
        self.assertEqual(Calculator.divide(10,20),0.5)
        

    def test_dividebyzero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(40,0)


if __name__ == '__main__':
    unittest.main()