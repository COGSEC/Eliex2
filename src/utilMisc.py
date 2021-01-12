# -*- coding: utf-8 -*-

# csvStringToList separates strings into a list
def csvStringToList(String):
    return String.split(", ")

def checkDict(register,key):
    if key in register.keys():
        return True
    return False