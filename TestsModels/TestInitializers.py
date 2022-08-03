import unittest
from Models.Chauffeur import Chauffeur
from Utils.envvar import number, password
from Models.Ruletka import Ruletka

likklechauffeur = Chauffeur()
roulette = Ruletka()

class TestInitializers(unittest.TestCase):

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
        #likklechauffeur = Chauffeur()
        self.assertEqual(likklechauffeur.mainTemp, [])
        self.assertTrue(len(likklechauffeur.mainTemp)==0)

    def testChauffeur__init__chrome_options(self):
        #likklechauffeur = Chauffeur()
        self.assertTrue(('--remote-debugging-port=9222' in likklechauffeur.chrome_options.arguments)
                        or ('--disable-dev-shm-usage' in likklechauffeur.chrome_options.arguments)
                        or('start-maximized' in likklechauffeur.chrome_options.arguments)
                        or('--disable-extensions' in likklechauffeur.chrome_options.arguments)
                        or('--disable-gpu' in likklechauffeur.chrome_options.arguments))

    def testChauffeur__init__numpass(self):
        self.assertEqual(likklechauffeur.number, number, 'wrong number')
        self.assertEqual(likklechauffeur.password, password, 'wrong password')

    def testRoulettte_model(self):
        self.assertIsInstance(roulette, Ruletka, 'roulette is not an instance of ruletka')
        self.assertIsInstance(roulette.roulettte_model, dict, 'roulette_model is not a dict')
        self.assertIn('6', roulette.roulettte_model, 'ehm, this is weird')
        self.assertNotIn('37', roulette.roulettte_model, 'again, this is weird')
        self.assertNotIn('-5', roulette.roulettte_model, 'aint this obvious?')
        self.assertNotIn(None, roulette.roulettte_model, 'whew')
        self.assertRaises(TypeError, roulette.roulettte_model+5, 'i dont know what you\'re expecting')


if __name__ == '__main__':
    unittest.main()
