# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import imp
import unittest, time, re
report_parser = imp.load_source('out_parse', 'utils/report_parser.py')
map_wrapper = imp.load_source('map_wrapper', 'utils/map_wrapper.py')
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
        self.sql_inj_testing()
            
    def xss_testing(self):
        driver = self.driver
        driver.get(self.base_url )
        parser.parse_suite("Cross Site Scripting /search.jsp")
        with open('demo_xss.txt') as f:
            mylist = f.read().splitlines()
            payloads = []
            for elem in mylist:
                payloads.append(elem) 
        for p in payloads:
            driver.find_element_by_link_text("Search").click()
            driver.find_element_by_name("q").clear()
            driver.find_element_by_name("q").send_keys(p)
            driver.find_element_by_css_selector("input[type=\"submit\"]").click()
            try:
                    alert = driver.switch_to_alert()
                    msg = alert.text
                    if msg in elem:
                        parser.parse(False, p)
                    else:
                        parser.parse(True, p)
                    alert.accept()
            except:
                    parser.parse(True, p)
                    pass

    def sql_inj_testing(self):
        driver = self.driver
        driver.get(self.base_url )
        parser.parse_suite("SQL Injection /login.jsp")
        driver.get(self.base_url + 'login.jsp')
        test_result = map_wrapper.execute('python sqlmap/sqlmap.py -r utils/search-text.txt -p username password --level=3 --risk=3 --flush-session --batch' )
        if test_result != "Not Found":
            match_obj_one = re.search(r'username=(.+)&', test_result)
            print match_obj_one.group(1)
            match_obj_two = re.search(r'password=(.+)', test_result)
            print match_obj_two.group(1)
            driver.find_element_by_link_text("Login").click()
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys(match_obj_one.group(1))
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(match_obj_two.group(1))
            driver.find_element_by_id("submit").click()
            parser.parse(False, test_result)
        else:
            parser.parse(True, 'None Found')
    
if __name__ == "__main__":
    unittest.main()
