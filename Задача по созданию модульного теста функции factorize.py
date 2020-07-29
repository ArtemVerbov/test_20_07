import unittest
from test import factorize


def factorize(x: int) -> int:
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if x == 0:
        return (0,)
    if x == 1:
        return (1,)
    if x < 0:
        raise ValueError
    if type(x) != int:
        raise TypeError
    i = 2
    primfac = []
    while i * i <= x:
        while x % i == 0:
            primfac.append(int(i))
            x = x / i
        i = i + 1
    if x > 1:
        primfac.append(int(x))
    return tuple(primfac)
#
#
# print(factorize(1))


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in (1.5, 'string'):
            with self.subTest(i=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in (-1, -10, -100):
            with self.subTest(i=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        for n, a in (0, (0,)), (1, (1,)):
            with self.subTest(i=n):
                self.assertEqual(factorize(n), a)

    def test_simple_numbers(self):
        for n, a in (3, (3,)), (13, (13,)), (29, (29,)):
            with self.subTest(i=n):
                self.assertEqual(factorize(n), a)

    def test_two_simple_multipliers(self):
        for n, a in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(i=n):
                self.assertEqual(factorize(n), a)

    def test_many_multipliers(self):
        for n, a in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(i=n):
                self.assertEqual(factorize(n), a)


if __name__ == '__main__':
    unittest.main()
