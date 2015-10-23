#!/usr/bin/python
import subprocess
import re

def execute(command):
    output = subprocess.check_output(command, shell=True)
    if 'is vulnerable' in output:
        match_obj = re.search('Payload\:(.*)', output)
        if match_obj:
            return 'Payload: '+ match_obj.group(1)
    else:
        return 'Not Found'
