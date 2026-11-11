import unittest

from calculadora import media, somar, subtrair


class CalculadoraTest(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(2, 3), 5)

    def test_subtracao_preserva_ordem(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(4, 10), -6)

    def test_media_usa_quantidade_de_elementos(self):
        self.assertEqual(media([6, 8, 10]), 8.0)
        self.assertEqual(media([10]), 10.0)
        self.assertEqual(media([1, 2, 3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
