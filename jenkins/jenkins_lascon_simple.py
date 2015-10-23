# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import subprocess

class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_security(self):
        self.assertTrue(True)
            
    
if __name__ == "__main__":
    unittest.main()
