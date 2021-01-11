# -*- coding: utf-8 -*-

import os
import ntpath
import io

# Get Extension of file from filepath string 
def getExt(filepath):
    i = filepath.rindex(".")
    return filepath[i:len(filepath)]

"""
print(getExt("testfolder\test.txt"))
"""

# editFilePath edits the filepath of a file at a given filepath
def editFilePath(filepath, newFilepath):
    os.rename(filepath, newFilepath)

"""
renameFile("otherTest.txt", "testfolder\otherTest.pdf")
"""

# makeFile takes a string and creates a file given a filepath
def makeFile(filepath, string):
    with open(filepath,"a") as file:
        file.write(string)

# checkForFile checks if a file exists or not, returns a bool
def checkForFile(filepath):
    return os.path.exists(filepath)

# getFileName gets the base file name from a path
def getFileName(filepath):
    return ntpath.basename(filepath)

# delFile deletes a file at path
def delFile(filepath):
    os.remove(filepath)

# readFile returns the data from a file at a given path
def readFile(filepath):
    f = io.open(filepath, mode="r", encoding="utf-8")
    return f.read()

# makeFullPath returns a fullpath given a directory location and a filepath
def makeFullPath(folder,path):
    if folder[len(folder)-1] != "/" and folder[len(folder)-1] != "\\":
        folder+="\\"
    if path[0] == "\\":
        path = path[1:len(path)]
    return folder+path

    
"""
print(getFileName("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/testfolder/hashLib/9dd4e461268c8034f5c8564e155c67a6"))
"""