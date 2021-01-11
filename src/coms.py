# -*- coding: utf-8 -*-


def fullBorder():
    print("=========================")
    
def smallBorder():
    print("-----")

def ASKforShortTitle(filename):
    fullBorder()
    print("Please input a short title for the following item:")
    print(filename)
    smallBorder
    return input("ShortTitle:")

def NOTIFYforHashHandling(filename, Hash):
    fullBorder()
    print(filename)
    smallBorder()
    print("Please update paperpile entry for this object with the hash below:\n")
    print(Hash)

