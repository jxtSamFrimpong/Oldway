from Ruletka import *
#from selenium.common.exceptions import WebDriverException

if __name__ == '__main__':
    spin = Ruletka()
    try:
        #spin.initWebDriver()
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
