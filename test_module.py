import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555555, 0.6666666666666666, 10.666666666666666], [4.222222222222222, 10.666666666666666, 6.222222222222221], 6.987654320987654],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 3.265986323710904], [2.0548046676563256, 3.265986323710904, 2.494438257849294], 2.6434171674156266],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=1)
        self.assertAlmostEqual(actual['variance'][2], expected['variance'][2], places=1)
        self.assertAlmostEqual(actual['standard deviation'][1][2], expected['standard deviation'][1][2], places=1)
        self.assertEqual(actual['max'][2], expected['max'][2])
        self.assertEqual(actual['min'][1][1], expected['min'][1][1])
        self.assertEqual(actual['sum'][1][0], expected['sum'][1][0])

    def test_calculate_raises(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
