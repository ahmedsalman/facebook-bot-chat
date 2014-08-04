import os
import urllib2
import time

from django.conf import settings

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




class Movie_Link_Crawler():

    # intializing the database
    def __init__(self):
        self.base_url = "https://www.facebook.com/"
        return None


    def get_webpage(self, url):
        try:
            print url
            c = urllib2.urlopen(url)
            return c
        except Exception, e:
            print "error is ",e
            print "could not open url",url
            return None


    def open_facebook( self ):

        usr = "yourusername"
        pwd = "yourpassword"

        driver = webdriver.Firefox()
        # or you can use Chrome(executable_path="/usr/bin/chromedriver")
        driver.get("http://www.facebook.com")
        driver.maximize_window()

        elem = driver.find_element_by_id("email")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

#        elem = driver.find_element_by_css_selector(".input.textInput")
#        elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
#        elem = driver.find_element_by_css_selector(".selected")
#        elem.click()
        time.sleep(10) # delays for 10 seconds
#        driver.close()

        friends_chat_list = driver.find_elements_by_css_selector("._55ln")
        for friend in friends_chat_list:
            friend.click()
            time.sleep(2) # delays for 2 seconds

            chatbox = driver.find_element_by_css_selector(".uiTextareaAutogrow._552m")
            chatbox.send_keys("Posted using Python's Selenium WebDriver bindings! testing please ignore this message it is computer generated and is only for learning purpose")
            chatbox.send_keys(Keys.RETURN)


            time.sleep(2) # delays for 2 seconds
            chatboxclose = driver.find_element_by_css_selector(".close.button")
            chatboxclose.click()





    def open_friend_page( self ):

        driver = webdriver.Firefox()
        # or you can use Chrome(executable_path="/usr/bin/chromedriver")
        driver.get("https://www.facebook.com/messages/therehman")

        usr = "yourusername"
        pwd = "yourpassword"

        elem = driver.find_element_by_id("email")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        elem = driver.find_elements_by_css_selector(".uiTextareaNoResize.uiTextareaAutogrow")
        elem.send_keys("Posted using Python's Selenium WebDriver bindings! testing please ignore this message it is computer generated and is only for learning purpose")
#        elem = driver.find_element_by_css_selector(".selected")
        elem.send_keys(Keys.RETURN)
#        time.sleep(10) # delays for 5 seconds
#        driver.close()


crawler = Movie_Link_Crawler()
crawler.open_facebook()
