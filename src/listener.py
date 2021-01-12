# -*- coding: utf-8 -*-

from time import sleep
#import config
#import utilMisc
import utilFile
import utilHash
import fi
import pathFilter
import coms

#ignoreList = ["desktop.ini", ".crdownload"]

class Listener:
    def __init__(self,configMngr):
        self.tick = int(configMngr.Get('ListenTick'))
        self.importLoc = configMngr.GetPath('Import')
        self.ppLoc = configMngr.GetPath('PaperPileCache')
        self.importHash = "" # last import folder hash
        self.ppHash = "" # last paperpilecache hash
        self.filter = pathFilter.Filter(configMngr)
        self.fiList = []
        self.papeCache = ""
    def Listen(self):
        coms.NOTIFYlistening()
        while True:
            if self.listenToPapeCache():
                return "pape"
            if self.listenToImport():
                return "import"
            sleep(self.tick)
    def listenToPapeCache(self):
        self.readInPapeCache()
        if self.checkPapeCacheHash():
            return True
        return False
    def listenToImport(self):
        self.getPathsFromImport()
        if self.checkImportHash():
            return True
        return False
    def readInPapeCache(self):
        self.papeCache = utilFile.readFile(self.ppLoc)
    def checkPapeCacheHash(self):
        cPapeHash = utilHash.createMD5(self.papeCache)
        if self.ppHash != cPapeHash:
            self.ppHash = cPapeHash
            coms.NOTIFYpapecacheChange()
            return True
        return False
    def getPathsFromImport(self):
        paths = utilFile.getPathsFromFolder(self.importLoc,pathType = 'full')
        fiList = []
        # convert raw paths into fileinfo Objects list
        for path in paths:
            fiList.append(fi.fileInfo(path))
        # scrub the list of duplicated, ignored, and blacklisted items
        self.fiList = self.filter.Scrub(fiList)
    # getHashOfList makes a hash from the hashes of items in import
    def getHashOfList(self,fiList):
        masterhash = ""
        for fiObj in fiList:
            masterhash += fiObj.GetHash()
        return utilHash.createMD5(masterhash)
    # checkImportHash checks if hash has changed, returns true if it has
    def checkImportHash(self):
        cHash = self.getHashOfList(self.fiList)
        if cHash != self.importHash:
            coms.NOTIFYimportListChange()
            self.importHash = cHash
            return True
        return False
    def GetPapeCache(self):
        return self.papeCache
    def GetFiList(self):
        return self.fiList

"""
import config

cm = config.ConfigManager('config.ini')
post = Listener(cm)
x = post.Listen()
x = post.Listen()
"""                                                          