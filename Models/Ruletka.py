from Chauffeur import Chauffeur
import time
from selenium.common.exceptions import WebDriverException

class Ruletka(Chauffeur):
    def __init__(self):
        Chauffeur.__init__(self)

        #audioAlarm.__init__(self)

        self.roulettte_model = {
            '0': ['green', 'none', 'none'],
            '1': ['red', 'low', 'odd'],
            '2': ['black', 'low', 'even'],
            '3': ['red', 'low', 'odd'],
            '4': ['black', 'low', 'even'],
            '5': ['red', 'low', 'odd'],
            '6': ['black', 'low', 'even'],
            '7': ['red', 'low', 'odd'],
            '8': ['black', 'low', 'even'],
            '9': ['red', 'low', 'odd'],
            '10': ['black', 'low', 'even'],
            '11': ['black', 'low', 'odd'],
            '12': ['red', 'low', 'even'],
            '13': ['black', 'low', 'odd'],
            '14': ['red', 'low', 'even'],
            '15': ['black', 'low', 'odd'],
            '16': ['red', 'low', 'even'],
            '17': ['black', 'low', 'odd'],
            '18': ['red', 'low', 'even'],
            '19': ['red', 'high', 'odd'],
            '20': ['black', 'high', 'even'],
            '21': ['red', 'high', 'odd'],
            '22': ['black', 'high', 'even'],
            '23': ['red', 'high', 'odd'],
            '24': ['black', 'high', 'even'],
            '25': ['red', 'high', 'odd'],
            '26': ['black', 'high', 'even'],
            '27': ['red', 'high', 'odd'],
            '28': ['black', 'high', 'even'],
            '29': ['black', 'high', 'odd'],
            '30': ['red', 'high', 'even'],
            '31': ['black', 'high', 'odd'],
            '32': ['red', 'high', 'even'],
            '33': ['black', 'high', 'odd'],
            '34': ['red', 'high', 'even'],
            '35': ['black', 'high', 'odd'],
            '36': ['red', 'high', 'even']

        }
        self.betable_parameters = {
            'col': 0,
            'lov': 1,
            'div': 2
        }
        self.opps = {
            'high': 'low',
            'low': 'high',
            'even': 'odd',
            'odd': 'even',
            'red': 'black',
            'black': 'red',
            'green': 'green',
            'none': 'none'
        }
        self.cycleCount = 0
        self.initialiser = 0
        self.mainBuffer = []
        self.four_toggles = 0
        self.hhlarr = []
        self.hhlEves = [False, 0]
        self.hhlEvesCounter = 0
        self.i_333_conti = [False, 0]
        self.i_4444_conti = [False, 0]
        self.i333num = 0
        self.i4444num = 0

    def updateBuffer(self):
        new_list = self.find_new_sub(self.mainTemp, self.mainBuffer)
        self.mainBuffer = new_list + self.mainBuffer
        if len(new_list)>0:
            #self.toggle_RUN()
            #self.highhighlowcheck()
            self.i_cont()
            #self.highhighlowEves()
        return len(new_list)

    #mkimbiaji
    def runner(self):
        while True:
            if self.cycleCount>=10:
                refreshtime = time.time()
                self.refresh()
                print(time.time()-refreshtime)
                time.sleep(5)
                try:
                    self.switchToIframe()
                    print('switched to iframe after more than 10')
                    time.sleep(5)
                    self.collectData()
                except:
                    print('line collect data')
                self.cycleCount=0
            else:
                self.phasers()
                if self.cycleCount==0:
                    print('running...')
            time.sleep(3)

    def phasers(self):
        if self.initialiser == 0:
            upd = self.updateBuffer()
            self.initialiser+=1
            print(self.mainBuffer)

        else:
            self.collectData()
            update_list = self.updateBuffer()
            self.cycleCount += update_list

            seq_ATO = self.search_seq_ATO(mainBuffer=self.mainBuffer[:50])
            #print(seq_ATO)
            if seq_ATO[0]:
                if update_list>0:
                    print('\n', seq_ATO[2])
                    print(self.mainBuffer[:10])
                    #alarm = audioAlarm(interval=1)
                    #alarm.alarm(num=seq_ATO[1])
                # alert function
            else:
                pass

    def what_to_Bets(self, para, num):
        numprops = self.roulettte_model[num][self.betable_parameters[para]]
        return  self.opps[numprops]

    def search_seq_afa(self, arr, para, ext):
        #res = False
        def chkLst(lst):
            if len(lst) < 0:
                res = True

            res = all(ele == lst[0] for ele in lst)

            if (res):
                return True
            else:
                return False

        retrieved_arr = []
        arrValuesMeans = []
        if self.mainBuffer==[]:
            return False
        else:
            for i in range(ext):
                if i * 2 > len(arr):
                    break
                if i * 2 < len(arr):
                    retrieved_arr.append(arr[i * 2])


            for j in range(len(retrieved_arr)):
                sm = self.roulettte_model[str(retrieved_arr[j])][self.betable_parameters[para]]
                arrValuesMeans.append(sm)

            #print(arrValuesMeans)
            return chkLst(arrValuesMeans)

    def search_seq_ATO(self, mainBuffer):
        for i in [8, 7, 6, 5, 4]:

            for para in self.betable_parameters:

                if self.search_seq_afa(mainBuffer, para, i):
                    #print('checked')
                    if i == 4:
                        return (True, i, str(i) + ' times of ' + str(
                            self.roulettte_model[mainBuffer[0]][self.betable_parameters[para]]) + ' so play ' + str(
                            self.what_to_Bets(para=para, num=mainBuffer[0])), self.what_to_Bets(para=para,
                                                                                                num=mainBuffer[0]))


                    elif i == 5:
                        return (True, i, str(i) + ' times of ' + str(
                            self.roulettte_model[mainBuffer[0]][self.betable_parameters[para]]) + ' so play ' + str(
                            self.what_to_Bets(para=para, num=mainBuffer[0])), self.what_to_Bets(para=para,
                                                                                                num=mainBuffer[0]))


                    elif i == 6:
                        self.alarm(num=8)
                        return (True, i, str(i) + ' times of ' + str(
                            self.roulettte_model[mainBuffer[0]][self.betable_parameters[para]]) + ' so play ' + str(
                            self.what_to_Bets(para=para, num=mainBuffer[0])), self.what_to_Bets(para=para,
                                                                                                num=mainBuffer[0]))



                    elif i == 7:
                        # print('be ready to bet!', para, 'has played', i, 'times')
                        # print('get ready to bet', '\n'+str(self.what_to_Bets(para=para,num=mainBuffer[0])).capitalize())
                        #self.alarm(num=8)
                        return (True, i, str(i) + ' times of ' + str(
                            self.roulettte_model[mainBuffer[0]][self.betable_parameters[para]]) + ' so play ' + str(
                            self.what_to_Bets(para=para, num=mainBuffer[0])), self.what_to_Bets(para=para,
                                                                                                num=mainBuffer[0]))

                    elif i == 8:
                        # print('\nbet now!!!!', para, 'has played', i, 'times')
                        # print('Play', str(self.what_to_Bets(para=para,num=mainBuffer[0])).capitalize(), 'NOW!!!')
                        self.alarm(num=8)
                        return (True, i, str(i) + ' times of ' + str(
                            self.roulettte_model[mainBuffer[0]][self.betable_parameters[para]]) + ' so play ' + str(
                            self.what_to_Bets(para=para, num=mainBuffer[0])), self.what_to_Bets(para=para,
                                                                                                num=mainBuffer[0]))

                    else:
                        continue



        return (False, None)


    def find_sub_list(self,sl, l, toggle_call = False):
        sll = len(sl)
        for ind in (i for i, e in enumerate(l) if e == sl[0]):
            if l[ind:ind + sll] == sl:
                # return ind, ind+sll-1
                # return ind
                if toggle_call:
                    return (True, ind)
                return True
    # def find_sub_list(self,sl, l):
    #     sll = len(sl)
    #     for ind in (i for i, e in enumerate(l) if e == sl[0]):
    #         if l[ind:ind + sll] == sl:
    #             # return ind, ind+sll-1
    #             # return ind
    #             return True


    def find_new_sub(self, sl, l):
        for i in range(len(sl)):
            arr = sl[i:len(sl)]
            # print(arr)
            if l == []:
                return  sl
            elif self.find_sub_list(arr, l) == True:
                # if only one, should not be used
                return sl[0:i]
                # print(i)
                # print(new_arr)
            #return []

    def toggleCheck(self, buffer, para, ext):
         def retrieved(buffer=buffer, ext=ext):
             retrieved_arr = []
             if buffer == []:
                 return retrieved_arr
             else:
                 for i in range(ext):
                     if i * 2 > len(buffer):
                         break
                     if i * 2 < len(buffer):
                         retrieved_arr.append(buffer[i * 2])
                 return retrieved_arr

         def retrieved_VAL(beta_from_buffer=retrieved(), para=para):
             val_arr = []
             for j in range(len(beta_from_buffer)):
                 sm = self.roulettte_model[str(beta_from_buffer[j])][self.betable_parameters[para]]
                 val_arr.append(sm)
             return val_arr

         def retrieved_OPP(beta_VAL=retrieved_VAL()):
             opp_beta_val = []
             for i in range(len(beta_VAL)):
                 if i%2==0:
                     opp_beta_val.append(beta_VAL[i])
                 elif i%2==1:
                     opp_beta_val.append(self.opps[beta_VAL[i]])
             return opp_beta_val

         def chkList(lst=retrieved_OPP()):
             if len(lst) < 0:
                 res = True

             res = all(ele == lst[0] for ele in lst)

             if (res):
                 return True
             else:
                 return False

         return chkList()


    def SUB_toggle_Chk(self, para):
        buffer = self.mainBuffer[2:]
        toggleCount = 2
        while self.toggleCheck(buffer=buffer, para=para, ext=toggleCount):
            toggleCount+=1
            if toggleCount*2>len(buffer):
                break

        buffer = self.mainBuffer
        if not(self.toggleCheck(buffer=buffer, para=para, ext=toggleCount)):
            print(toggleCount-1, para)
            if (toggleCount-1)>=4:
                #TODO
                self.four_toggles+=1
                self.toggleIntSave(toggleInt=self.four_toggles, filename='fourtoggles.txt')
                pass
            self.toggleIntSave(toggleInt=toggleCount-1, filename = 'toggle.txt')
        else:
            print('still toggling', self.roulettte_model[str(buffer[0])][self.betable_parameters[para]])

    def toggle_RUN(self):
        for i in self.betable_parameters:
            self.SUB_toggle_Chk(para=i)

    def toggleIntSave(self, toggleInt, filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write('0')
        try:
            try:
                f_read = f.read()
                if len(f_read) == 0:
                    f_read = '0'
                f_read = int(str(f_read))
            except [ValueError, TypeError, AttributeError, ArithmeticError] as e:
                print(e)
            f.close()
            if toggleInt > f_read:
                f = open(filename, 'w')
                f.write(str(toggleInt))
                f.close()
                # f = open('toggle.txt', 'r')
                # print(f.read())
                # f.close()
            else:
                f.close()
        except [ValueError, TypeError, AttributeError, BaseException] as e:
            print(e)

    def highhighlowcheck(self):
        arr = self.mainBuffer[:3]

        def chkList(lst):
            if len(lst) < 0:
                res = True

            res = all(ele == lst[0] for ele in lst)

            if (res):
                return True
            else:
                return False
        def retrievedArr(arr=arr):
            arrMeans=[]
            for i in arr:
                arrMeans.append(self.roulettte_model[str(i)][1])
            arrMeans[0] = self.opps[arrMeans[0]]
            return arrMeans
        def checkRetArr(arr=retrievedArr()):

            if chkList(lst=arr[1:]+['high']):
                if chkList(lst=arr):
                    return True
                else:
                    return False
            else:
                return None

        def useCheckedArrAgainstHHR():
            triStateBool = checkRetArr()
            if triStateBool == True:
                if len(self.hhlarr) == 0:
                    self.hhlarr.append(True)
                    self.hhlarr.append(1)
                else:
                    if self.hhlarr[0] == True:
                        ok = self.hhlarr[1]
                        ok += 1
                        self.hhlarr[1] = ok
                    else:
                        self.hhlarr[0] = True
                        self.hhlarr[1] = 1

            elif triStateBool == False:
                if len(self.hhlarr) == 0:
                    pass
                else:
                    if self.hhlarr[0] == True:
                        self.hhlarr[0] = False
                        self.hhlarr[1] = 0
                    else:
                        pass
            elif triStateBool == None:
                pass

        def checkWrite():
            useCheckedArrAgainstHHR()
            if len(self.hhlarr)!=0:
                if self.hhlarr[0]:
                    self.toggleIntSave(toggleInt=self.hhlarr[1], filename='highhighlowchech.txt')
        checkWrite()

    def i_cont(self):
        def saveLenght(ext, num):
            name = ''
            for i in range(ext):
                name = name + str(ext)
            name = 'store/cont_' + name + '.txt'
            self.toggleIntSave(num, name)


        def setLenght(num, ext):
            if ext==3:
                if num==0:
                    self.i_333_conti[0]=True
                    self.i_333_conti[1]=0
                elif num==1:
                    self.i_333_conti[0]=False
                    k=self.i_333_conti[1]
                    k+=1
                    self.i_333_conti[1]=k
            elif ext==4:
                if num==0:
                    self.i_4444_conti[0]=True
                    self.i_4444_conti[1]=0
                elif num==1:
                    self.i_4444_conti[0]=False
                    k=self.i_4444_conti[1]
                    k+=1
                    self.i_4444_conti[1]=k
        def chkList(lst):
            if len(lst) < 0:
                res = True

            res = all(ele == lst[0] for ele in lst)

            if (res):
                return True
            else:
                return False
        def cont(ext):
            arr = []
            for i in range(ext+1):
                arr.append(self.mainBuffer[i*2])
            selArr = []
            for i in range(len(arr)):
                selArr.append(self.roulettte_model[str(arr[i])][1])
            #print(selArr)
            if chkList(selArr[1:]):
                #print('from 1 to ' + str(ext) + ' all high')
                if ext == 3:
                    some_array = self.i_333_conti
                elif ext == 4:
                    some_array = self.i_4444_conti

                if chkList(selArr):
                    if ext==3:
                        self.i333num += 1
                        self.toggleIntSave(toggleInt=self.i333num, filename='store/333num.txt')
                    if ext==4:
                        self.i4444num += 1
                        self.toggleIntSave(toggleInt=self.i4444num, filename='store/4444num.txt')
                    #chexk some array status
                    if some_array[0]:
                        pass
                    #if true, save lenght and set to zero
                    else:
                        saveLenght(ext, some_array[1])
                        setLenght(0, ext)
                else:
                    #chexk some array status
                    setLenght(1, ext)
                    #if true, add one to lenght
                    #else set to true and set lenght to 1

            selArr.pop()
            if chkList(selArr):
                self.alarm(num=100)
        def i_333_cont():
            cont(3)
        def i_444_cont():
            cont(4)
            # self.click(val='odd')

        #i_333_cont()
        i_444_cont()

    def highhighlowEves(self):
        def save(num):
            name = 'store/hhlEves.txt'
            self.toggleIntSave(toggleInt=num, filename=name)
        def chkList(lst):
            if len(lst) < 0:
                res = True

            res = all(ele == lst[0] for ele in lst)

            if (res):
                return True
            else:
                return False
        def retrieveMean(lst):
            arr = []
            for i in range(len(lst)):
                arr.append(self.roulettte_model[str(lst[i])][1])
            #print(arr)
            return arr

        arr = []
        for i in range(5):
            arr.append(self.mainBuffer[i*2])
        #print(arr)
        arr = retrieveMean(lst=arr)
        if chkList(lst=arr[1:]):
            if chkList(lst=arr):
                if self.hhlEvesCounter%2==0:
                    self.hhlEves[0]=False
                    k = self.hhlEves[1]
                    k+=1
                    self.hhlEves[1]=k
                    self.hhlEvesCounter+=1
                else:
                    self.hhlEvesCounter+=1
            else:
                if self.hhlEvesCounter%2==0:
                    if self.hhlEves[0]:
                        self.hhlEvesCounter=0
                    else:
                        save(num=self.hhlEves[1])
                        self.hhlEves[0] = True
                        self.hhlEves[1] = 0
                        self.hhlEvesCounter=0
                else:
                    self.hhlEvesCounter+=1



if __name__ == '__main__':
    spin = Ruletka()
    try:
        spin.loadPage()
        spin.runner()
    except WebDriverException as e:
        #spin.alarm(num=100)
        print(e)
    except KeyboardInterrupt as e:
        spin.end()
    except TypeError as e:
        print(e)
        spin.alarm(num=100)
    except ValueError:
        spin.alarm(num=100)
    finally:
        a = time.localtime()
        print('Stopped at', a[3], ':', a[4], ':', a[5])
        print(spin.i4444num)
        spin.end()

    # a = time.time()
    #
    #
    # try:
    #     spin = roulette()
    #     spin.mainBuffer = [10,19,10,10,10,10,10,10,22,10,23,20,25]
    #     spin.i_cont()
    # except KeyboardInterrupt as e:
    #     print(e)
    #
    #
    #
    # finally:
    #     print(time.time()-a)
