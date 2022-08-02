import unittest
from Models.Chauffeur import Chauffeur
#from n.chrome import okay
#from ..Models.Ruletka import Ruletka

class TestAnal(unittest.TestCase):
    #ruletka
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def testChauffeur__init__(self):
        likklechauffeur = Chauffeur()
        self.assertEqual(likklechauffeur.mainTemp, [])
        self.assertTrue(len(likklechauffeur.mainTemp)==0)


if __name__ == '__main__':
    unittest.main()
