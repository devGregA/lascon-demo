# -*- coding: utf-8 -*-
import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import subprocess
report_parser = imp.load_source('out_parse', 'ABSOLUTE_PATH/utils/report_parser.py')
map_wrapper = imp.load_source('map_wrapper', 'ABSOLUTE_PATH/utils/map_wrapper.py')
parser = report_parser.out_parse()
parser.start()
path = "ABSOLUTE_PATH"

class Testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_security(self):
        self.sql_inj_testing()

    def sql_inj_testing(self):
        driver = self.driver
        driver.get(self.base_url )
        parser.parse_suite("SQL Injection")
        driver.get(self.base_url + 'login.jsp')
        test_result = map_wrapper.execute('python %s/sqlmap/sqlmap.py -r %s/utils/search-text.txt -p username password --level=3 --risk=3 --flush-session --batch' % (path, path)  )
        status = True
        if test_result != "Not Found":
            status = False
            parser.parse(status, test_result)
        else:
            pass
        self.assertTrue(status)

    
if __name__ == "__main__":
    unittest.main()
