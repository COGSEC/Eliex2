# -*- coding: utf-8 -*-

import hashlib

# getMD5 returns an MD5 hash of a file, will return "" on error.
def getMD5(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
    return hashlib.md5(data).hexdigest()
    
def createMD5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()
"""
x = getMD5('config.ini') out: de88ec9491a8b87697751db5cc5b2fd1
"""
