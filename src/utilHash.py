# -*- coding: utf-8 -*-

import hashlib
import os

# getMD5 returns an MD5 hash of a file, will return "" on error.
def getMD5(filepath):
    try:
        with open(filepath, 'rb') as file:
            data = file.read()
        return hashlib.md5(data).hexdigest()
    except PermissionError:
        print("Received PermissionError!")
        cmd = input("Type close to close program, or hit enter to try again")
        if cmd == "close":
            os.exit(1)
        else:
            getMD5(filepath)
    
def createMD5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()
"""
x = getMD5('config.ini') out: de88ec9491a8b87697751db5cc5b2fd1
"""
