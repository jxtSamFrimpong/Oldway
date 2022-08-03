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

    def testChauffeur__init__mainTemp(self):
        likklechauffeur = Chauffeur()
        self.assertEqual(likklechauffeur.mainTemp, [])
        self.assertTrue(len(likklechauffeur.mainTemp)==0)

    def testChauffeur__init__chrome_options(self):
        likklechauffeur = Chauffeur()
        self.assertTrue(('--remote-debugging-port=9222' in likklechauffeur.chrome_options.arguments)
                        or ('--disable-dev-shm-usage' in likklechauffeur.chrome_options.arguments)
                        or('start-maximized' in likklechauffeur.chrome_options.arguments)
                        or('--disable-extensions' in likklechauffeur.chrome_options.arguments)
                        or('--disable-gpu' in likklechauffeur.chrome_options.arguments))


if __name__ == '__main__':
    unittest.main()
