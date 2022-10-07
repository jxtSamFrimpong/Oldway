from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import threading
import os
import chromedriver_autoinstaller
import re
from envvar import number, password


class Chauffeur:
    def __init__(self):
        self.mainTemp = []
        self.chrome_options = Options()

        #self.chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.chrome_options.add_argument("--no-sandbox")
        #self.chrome_options.add_argument("--remote-debugging-port=9222")
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        #self.chrome_options.add_argument("start-maximized")
        #self.chrome_options.add_argument("--disable-extensions")
        #self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=375")
        #print(self.chrome_options.arguments)

        #self.number = os.environ['NUMBER']
        #self.password = os.environ['PASSWORD']
        self.number = number
        self.password = password
        #ChromeDriverManager().install()

        self.driver = webdriver.Chrome(
            # service=Service(executable_path='/Users/ewintil/PycharmProjects/Oldway/chromedriver'),
            service=Service(executable_path=chromedriver_autoinstaller.install()),
            options=self.chrome_options)


        #self.driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=)
    # def initWebDriver(self):
    #     self.driver = webdriver.Chrome(
    #         # service=Service(executable_path='/Users/ewintil/PycharmProjects/Oldway/chromedriver'),
    #         service=Service(executable_path=chromedriver_autoinstaller.install()),
    #         options=self.chrome_options)


    def getSite(self):
        self.driver.get('https://www.betway.com.gh/lobby/livegames/launchgame/Featured/Auto%20Roulette?launchUrlText=%5bPlay+for+real%5d')

        time.sleep(15)

    def loadPage(self):
        self.getSite()
        self.closure()
        self.login()
        self.switchToIframe()
        self.collectData()

    def refresh(self):
        self.driver.refresh()
        #todo --time.sleep(12)

    def closure(self):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.ID, 'LI-Close')))
            self.driver.find_element_by_id('LI-Close').click()

            print('here clicked')
            #todo ++time.sleep(4) if misbehaving
        except:
            print('no here clicked')


    def login(self):
        # LOGIN BUTTON
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.ID, 'LoginModal')))
            #self.driver.find_element_by_id('LoginModal').click()
            print('login present')
            #todo ++time.sleep(4) if misbrhaving
            # save_cookies('betway')
        except:
            print('no login present')

        # MOBILE NUMBER
        try:
            element = WebDriverWait(self.driver, 5, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="menuMobileNumber"]')))
            self.driver.find_element(by=By.XPATH, value='//*[@id="menuMobileNumber"]').send_keys(self.number)
            print('number sent')
            #todo ++time.sleep(2) if misbehaving
        except:
            print('no number sent')

        # PASSWORD
        try:
            element = WebDriverWait(self.driver, 2, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="menuPassword"]')))
            self.driver.find_element(by=By.XPATH, value='//*[@id="menuPassword"]').send_keys(self.password)
            print('pass sent')
            #todo ++time.sleep(2) if misbehaving

        except:
            print('no pass sent')


        # SECOND LOGIN BUTTON
        try:
            element = WebDriverWait(self.driver, 2, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mobileLoginBtn"]')))
            self.driver.find_element(by=By.XPATH, value='//*[@id="mobileLoginBtn"]').click()
            print('inside')
            #todo ++time.sleep(2) if misbehaving
        except:
            print('no inside')


    def switchToIframe(self):

        # LOAD VM
        try:
            element = WebDriverWait(self.driver, 30, poll_frequency=1,
                                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException]).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="lobbyIframe"]')))
            # todo !+! current = self.driver.find_element_by_xpath('//*[@id="lobbyIframe"]')
            # //div/div/div[2]/div/div/div[2]
            # todo !+! print('reading inside')
            # return current
        except:
            print('no reading values')

        try:
            self.driver.switch_to.frame('lobbyIframe')
            print('switched')

        except:
            print('couldn\'t find elements in iframe')


    def collectData(self):
        try:
            self.mainTemp = []
            time.sleep(7)
            try:
                WebDriverWait(self.driver, 2, poll_frequency=1,
                          ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                              NoSuchElementException]).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[3]/div[1]/div/div[2]/div')))
                print('data row present')
            except Exception as e:
                print('except',e)

            try:
                self.driver.find_elements(by=By.CLASS_NAME, value='value--877c6')
                #print()
            except:
                print('driver couldn\'t find numbers')
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            k = soup.findAll('div', {'data-role': 'recent-number'})
            #print(len(k))
            #spanArr = []
            for i in range(len(k)):
                # j = k[i].find('span')
                # print(j)
                self.mainTemp.append(k[i].find('span').get_text())
        except:
            print('could not collect data')
        # print(soup.findAll('path', {'data-bet-spot-id':'from19to36'}))
        #self.driver.f
        # print(soup.find('div', {'data-value':'0.5'}))
        # print(soup.find('div', {'data-value': '2.5'}))
        # print('\ndouble')
        # print(soup.find('li', {'class': 'double--2JCkY'}))
        # print('\nundo')
        # print(soup.find('li', {'class': 'undo--1kC__'}))
        # print('\nbalance')
        # print(soup.find('span', {'data-role': 'balance-label__value'}))
        # print('\ntotal bet or previosly won')
        # print(soup.find('span', {'class':'title--GvCvW'}))
        # print(soup.find('span', {'class':'amount--3BgvQ'}))
        #
        # print('\nstatus text')
        # print(soup.find('div', {'data-role':'status-text'}))


    def click(self, val):
        type = {
            'high':'from19to36',
            'low':'from1to18',
            'even': 'even',
            'odd': 'black',
            'red':'red',
            'black':'odd'
        }
        #val = type(val)
        try:
            self.driver.find_element_by_id(type[val]).click()
            print('succesful bet')
        except:
            print('cant find click button for', val)
        try:
            print('balance is', BeautifulSoup(self.driver.page_source, 'lxml').findAll('span', {'data-role':'balance-value'}))
            #print(self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/div[2]'))
        except:
            print('couldnt find balance')
            #print(self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/div[2]'))


    def end(self):
        self.driver.close()
        self.driver.quit()

# if __name__=='__main__':
#     chauffeur = Chauffeur()
#     try:
#         chauffeur.loadPage()
#     except Exception as e:
#         print(e)
#     finally:
#         chauffeur.end()


