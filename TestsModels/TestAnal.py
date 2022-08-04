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

def temp_and_buffer_maker_general(temp, buffer):
    roulette.mainBuffer = buffer
    roulette.mainTemp = temp


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
        out = []
        temp = ''
        for i in captured.out:

            if i.isnumeric():
                temp+=i
            else:
                if temp.isnumeric():
                    out.append(int(temp))
                temp=''

        self.assertEqual([16, 18, 20, 14, 32, 34, 36, 10, 12, 16,21,33,55], out)

        #self.assertEqual([16,18,20,14,32,34,36,10,12,16,21,33,55], captured.out)

    def test_what_to_Bets(self):
        #print(roulette.what_to_Bets(para='col', num=str(25)))
        self.assertEqual(
            roulette.what_to_Bets(num=str(30), para='col'),
            roulette.opps[
                roulette.roulettte_model[str(30)][roulette.betable_parameters['col']]
            ])
        
    def test_search_seq_afa(self):
        temp_and_buffer_maker_general(temp=[], buffer=[])
        self.assertTrue(not roulette.search_seq_afa(arr=roulette.mainBuffer, para='col', ext=4))

        temp_and_buffer_maker_general(temp=[1,2,3,4,5], buffer=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertTrue(roulette.search_seq_afa(arr=roulette.mainBuffer, para='div', ext=4))

        temp_and_buffer_maker_general(temp=[12,19,18,30,1,20,12], buffer=[12,19,18,30,1,20,12,33,16,24,8,29,6,20])
        self.assertTrue(roulette.search_seq_afa(arr=roulette.mainBuffer, para='lov', ext=6))


    def test_search_seq_ATO(self):
        temp_and_buffer_maker_general(temp=[12,19,18,30,1,20,12], buffer=[12,19,18,30,1,20,12,33,16,24,8,29,6,20, 13, 31, 14, 32, 15, 21])
        self.assertTrue(roulette.search_seq_ATO(mainBuffer=roulette.mainBuffer)[0])
        

        temp_and_buffer_maker_general(temp=[12, 19, 18, 31, 2, 21, 12],
                                      buffer=[12, 19, 18, 31, 2, 21, 12,33,34,13,10,11,16,17,18,19,6,35,36])
        self.assertTrue(roulette.search_seq_ATO(mainBuffer=roulette.mainBuffer)[0])

