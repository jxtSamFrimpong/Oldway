import unittest
from Models.Chauffeur import Chauffeur
from Utils.envvar import number, password
from Models.Ruletka import Ruletka
from random import randint
import io
import sys
import pytest

roulette = Ruletka()
def roulette_temp_and_buffer_maker(space: int):
    roulette.mainBuffer = []
    roulette.mainTemp = []
    for _ in range(50):
        if _ < 10:
            roulette.mainTemp.append(randint(0, 36))
        roulette.mainBuffer.append(randint(0, 36))

    roulette.mainTemp = roulette.mainTemp[:10-space] + roulette.mainBuffer[:space]

def temp_and_buffer_maker_for_phasers():
    roulette.mainBuffer = [10,12,16,21,33,55]
    roulette.mainTemp = [16,18,20,14,32,34,36,10,12,16]


class TestAnal(unittest.TestCase):
    # ruletka

    def test_temp_and_buffer_before(self):
        roulette_temp_and_buffer_maker(space=3)
        self.assertTrue(len(roulette.mainTemp)==10)
        self.assertTrue(len(roulette.mainBuffer)==50)
        self.assertTrue(len([i for i in roulette.mainBuffer if i > 36 or i<0])==0)
        self.assertTrue(len([i for i in roulette.mainBuffer if i <= 36 or i>=0])==50)

    def test_update_buffer(self):
        roulette_temp_and_buffer_maker(space=3)
        self.assertEqual(roulette.updateBuffer(), 7)

        roulette_temp_and_buffer_maker(space=10)
        self.assertEqual(roulette.updateBuffer(), 0)

        roulette_temp_and_buffer_maker(space=5)
        self.assertEqual(roulette.updateBuffer(), 5)

        roulette_temp_and_buffer_maker(space=6)
        self.assertEqual(roulette.updateBuffer(), 4)

        roulette_temp_and_buffer_maker(space=9)
        self.assertEqual(roulette.updateBuffer(), 1)

        #TODO checkout
        # roulette_temp_and_buffer_maker(space=0)
        # self.assertEqual(roulette.updateBuffer(), 10)

    #TODO
    def test_runner(self):
        pass

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys


    def test_phasers(self):
        temp_and_buffer_maker_for_phasers()
        roulette.phasers() # Call function.
        captured = self.capsys.readouterr()
        print(captured.out)
