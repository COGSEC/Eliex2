# -*- coding: utf-8 -*-

import utilFile

class Filter:
    def __init__(self, configMngr):
        self.failLoc = configMngr.GetPath('FailedImport')
        self.hLibLoc =configMngr.GetPath('HashLib')
        self.ignoreList = configMngr.Get('IgnoreList')
        self.blackList = configMngr.Get('BlackList')
    def Scrub(self, fiList):
        pass
    def checkIgnore(self,fiList):
        paths = []
        for item in self.ignoreList:
            for fiObj in fiList:
                if item in fiObj.GetFileName():
                    pass
                else:
                    paths.append(fiObj)
        return paths
    def checkBlack(self,fiList):
        paths = []
        movetoFail = []
        for item in self.blackList:
            for fiObj in fiList:
                if item in fiObj.GetFileName():
                    pass
                else:
                    movetoFail.append(fiObj)
        return paths, movetoFail
    def checkDuplicates(self,fiList):
        paths = []
        duplicates = []
        for fiObj in fiList:
            if utilFile.checkForFile(self.HashLib+"/"+fiObj.GetHash()):
                duplicates.append(fiObj)
            else:
                paths.append(fiObj)
        return paths,duplicates