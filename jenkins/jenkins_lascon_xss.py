# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import subprocess
import imp
report_parser = imp.load_source('out_parse', 'ABSOLUTE_PATH/utils/report_parser.py')
parser = report_parser.out_parse()
parser.start()


class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_security(self):
        self.xss_testing()
            
    def xss_testing(self):
        driver = self.driver
        driver.get(self.base_url )
        parser.parse_suite("Cross Site Scripting")
        with open('ABSOLUTE_PATH/demo_xss.txt') as f:
            mylist = f.read().splitlines()
            for elem in mylist:
                driver.find_element_by_link_text("Search").click()
                driver.find_element_by_name("q").clear()
                driver.find_element_by_name("q").send_keys(elem)
                driver.find_element_by_css_selector("input[type=\"submit\"]").click()
                status = True
                try:
                        alert = driver.switch_to_alert()
                        alert.accept()
                        status = False
                        parser.parse(status, elem)
                except:
                        parser.parse(True, elem)
                        pass
                self.assertTrue(status)
    
if __name__ == "__main__":
    unittest.main()
