# -*- coding: utf-8 -*-
cProject = "MISC"

def fullBorder():
    print("=========================")
    
def smallBorder():
    print("-----")

def ASKforShortTitle(fiObj):
    fullBorder()
    print("Please input a short title for the following item:")
    print("title: " + fiObj.title)
    print("author: " + fiObj.author)
    print("year: " + fiObj.year)
    smallBorder()
    st = input("ShortTitle: ")
    print("")
    return st

def ASKforProject():
    proj = input("Please input project Callsign, hit Enter if last: ")
    print("")
    global cProject
    if proj == "":
        return "[[" + cProject + "]]"
    else:
        cProject = proj
        return "[[" + proj + "]]"
    
    

def NOTIFYforHashHandling(filename, Hash):
    fullBorder()
    print(filename)
    smallBorder()
    print("Please update paperpile entry for this object with the hash below:\n")
    print(Hash)

def NOTIFYlistening():
    smallBorder()
    print("Listening...")

def NOTIFYduplicateFound(Hash,Name):
    smallBorder()
    print("duplicate found...")
    print("HASH: "+Hash)
    print("Name: "+Name)
    smallBorder()

def NOTIFYSearchingForHashes():
    print("Librarian searching for hash data...")
    
def NOTIFYWritingreport():
    print("Librarian writing report of missing hashes...")
    
def NOTIFYpapecacheChange():
    print("Change to PapeCache Detected...")

def NOTIFYimportListChange():
    print("Change to Import Folder Detected...")
    print("Change to PapeCache Detected...")
    
    