import time
import pickle # для созранения cookies
from selenium import webdriver 

def sesionCookies(sites, timers): # для получения cookies
    browser = webdriver.Chrome()
    browser.get(sites)
    time.sleep(timers)
    pickle.dump(browser.get_cookies(), open('session', 'wb'))

def addCookies(sites, fileSesion):
    browser = webdriver.Chrome()
    browser.get(sites)
    for cookie in pickle.load(open(fileSesion, "rb")):
        browser.add_cookie(cookie)
    
    print("cookie load")
    browser.refresh