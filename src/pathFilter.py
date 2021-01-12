# -*- coding: utf-8 -*-

import utilFile
from utilMisc import csvStringToList
from utilMisc import checkDict
from coms import NOTIFYduplicateFound

class Filter:
    def __init__(self, configMngr):
        self.failLoc = configMngr.GetPath('FailedImport')
        self.hLibLoc =configMngr.GetPath('HashLib')
        self.ignoreList = csvStringToList(configMngr.Get('IgnoreList'))
        self.blackList = csvStringToList(configMngr.Get('BlackList'))
    def Scrub(self, fiList):
        return self.checkLocalDuplicates(self.checkDuplicates(self.checkBlack(self.checkIgnore(fiList))))
    def checkIgnore(self,fiList):
        i = 0
        while i < len(fiList):
            mark = True
            for item in self.ignoreList:
                if item in fiList[i].GetFileName():
                    del fiList[i]
                    mark = False
                    break
            if mark:
                i+=1
        return fiList
    def checkBlack(self,fiList):
        i = 0
        while i < len(fiList):
            mark = True
            for item in self.blackList:
                if item in fiList[i].GetFileName():
                    fiList[i].MoveToFolder(self.failLoc)
                    del fiList[i]
                    mark = False
                    break
            if mark:
                i+=1
        return fiList
    def checkDuplicates(self,fiList):
        i = 0
        while i < len(fiList):
            mark = True
            if utilFile.checkForFile(self.hLibLoc+"/"+fiList[i].GetHash()):
                NOTIFYduplicateFound(fiList[i].GetHash(),fiList[i].GetFileName())
                fiList[i].MoveToFolder(self.failLoc)
                del fiList[i]
                mark = False
            if mark:
                i+=1
        return fiList
    def checkLocalDuplicates(self,fiList):
        register = dict()
        i = 0
        while i < len(fiList):
            mark = True
            if checkDict(register,fiList[i].GetHash()):
                fiList[i].MoveToFolder(self.failLoc)
                NOTIFYduplicateFound(fiList[i].GetHash(),fiList[i].GetFileName())
                del fiList[i]
                mark = False
            if mark:
                register[fiList[i].GetHash()] = ""
                i+=1
        return fiList
