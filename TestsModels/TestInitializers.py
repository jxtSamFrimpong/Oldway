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
        #self.assertRaises(TypeError, roulette.roulettte_model+5, 'i dont know what you\'re expecting')

    def testBetable_parameters(self):
        self.assertIsInstance(roulette.betable_parameters, dict, 'betable_parameters is a dictionary')
        self.assertIn('col', roulette.betable_parameters)
        self.assertIn('lov', roulette.betable_parameters)
        self.assertIn('div', roulette.betable_parameters)
        self.assertNotIn('red', roulette.betable_parameters)
        self.assertNotIn('1', roulette.betable_parameters)
        #self.assertRaises(TypeError, roulette.betable_parameters**2, 'this too')

    def testOpps(self):
        self.assertIs(len(roulette.opps), 8, '8 keys here')
        self.assertNotIn('col', roulette.opps)
        self.assertIsNotNone(roulette.opps)
        #self.assertRaises(KeyError, roulette.opps['High'])
        self.assertIn('high', roulette.opps)
        self.assertIn('black', roulette.opps)
        self.assertEqual(roulette.opps['high'], 'low')
        self.assertEqual(roulette.opps['low'], 'high')
        self.assertEqual(roulette.opps['black'], 'red')
        self.assertEqual(roulette.opps['red'], 'black')
        self.assertEqual(roulette.opps['even'], 'odd')
        self.assertEqual(roulette.opps['odd'], 'even')
        self.assertEqual(roulette.opps['green'], 'green')
        self.assertEqual(roulette.opps['none'], 'none')

    def test_Counts_and_Temps(self):
        def trials(val1, val2, operator):
            if operator:
                try:
                    val1 + val2
                except Exception as e:
                    pass
            else:
                try:
                    val1/val2
                except Exception as e:
                    pass
        self.assertEqual(roulette.cycleCount, 0)
        #self.assertRaises(ZeroDivisionError, trials(roulette.cycleCount, 0, 0))
        self.assertEqual(roulette.cycleCount, roulette.initialiser)
        self.assertEqual(roulette.mainBuffer, [])
        self.assertIsInstance(roulette.mainBuffer, list)
        self.assertTrue(len(roulette.mainBuffer)==0)
        self.assertEqual(roulette.four_toggles, roulette.initialiser)
        self.assertEqual(roulette.hhlEvesCounter, 0)
        self.assertEqual(roulette.i333num, 0)
        self.assertEqual(roulette.i4444num, 0)
        self.assertEqual(roulette.hhlarr, [])
        self.assertIsInstance(roulette.hhlarr, list)
        self.assertTrue(len(roulette.hhlarr) == 0)
        self.assertIsInstance(roulette.hhlEves, list)
        self.assertIn(0, roulette.hhlEves)
        self.assertTrue(not roulette.hhlEves[0])
        self.assertEqual(len(roulette.hhlEves), 2)
        self.assertEqual(roulette.hhlEves[0], roulette.hhlEves[1])
        self.assertIsInstance(roulette.hhlEves[1], int)
        self.assertNotEqual(type(roulette.hhlEves[0]), type(roulette.hhlEves[1]))
        self.assertIsInstance(roulette.i_333_conti, list)
        self.assertIn(0, roulette.i_333_conti)
        self.assertTrue(not roulette.i_333_conti[0])
        self.assertEqual(len(roulette.i_333_conti), 2)
        self.assertEqual(roulette.i_333_conti[0], roulette.i_333_conti[1])
        self.assertIsInstance(roulette.i_333_conti[1], int)
        self.assertNotEqual(type(roulette.i_333_conti[0]), type(roulette.i_333_conti[1]))
        self.assertIsInstance(roulette.i_4444_conti, list)
        self.assertIn(0, roulette.i_4444_conti)
        self.assertTrue(not roulette.i_4444_conti[0])
        self.assertEqual(len(roulette.i_4444_conti), 2)
        self.assertEqual(roulette.i_4444_conti[0], roulette.i_4444_conti[1])
        self.assertIsInstance(roulette.i_4444_conti[1], int)
        self.assertNotEqual(type(roulette.i_4444_conti[0]), type(roulette.i_4444_conti[1]))


if __name__ == '__main__':
    unittest.main()
