# -*- coding: utf-8 -*-
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class out_parse (object):
    def __init__(self):
        self.count = 1 

    def start(self):
        print bcolors.OKBLUE + 'Running Security Test Suited \n==========================' + bcolors.ENDC

    def parse_suite(self, name):
        print bcolors.HEADER + "Testing: " + bcolors.WARNING + name + bcolors.ENDC

    def parse(self, status, payload):
        if status: 
           print  bcolors.OKGREEN + '✔ ' + bcolors.ENDC + payload
        else:
           print bcolors.FAIL + '✘ ' + bcolors.ENDC + payload
        return status

