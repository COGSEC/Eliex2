# -*- coding: utf-8 -*-

import utilFile
import blocParser
from utilMisc import checkDict
import coms

class Librarian:
    def __init__(self, configMngr):
        self.vault = configMngr.GetPath('Vault')
        self.docLib = configMngr.GetPath('DocLib')
        self.hashLib =  configMngr.GetPath('HashLib')
        self.reportLoc =  configMngr.GetPath('Report')
        self.blocs = []
        self.fiList = []
        self.parser = blocParser.blocParser()
    def NewPapeCache(self, papeCache):
        self.setBlocs(papeCache)
        self.Update()
    def NewFiList(self,fiList):
        self.fiList = fiList
        self.checkForLocalDuplicates()
        self.Update()
    def Update(self):
        ready = self.searchForHashes()
        self.writeReport()
        self.archive(ready)
        self.notify()
    def notify(self):
        for fiObj in self.fiList:
            fiObj.NOTIFYforHashHandling()
    def archive(self,ready):
        for i in range(len(ready)):
            ready[i] = self.parser.ParseBloc(ready[i])
        self.askForNames(ready)
        for fiObj in ready:
            fiObj.Archive(self.vault,self.docLib,self.hashLib)
    def askForNames(self,ready):
        for fiObj in ready:
            fiObj.ASKforShortTitle()
    def writeReport(self):
        if len(self.fiList) > 0:
            coms.NOTIFYWritingreport()
            bloctext = ""
            for fiObj in self.fiList:
                bloctext += fiObj.writeReportString() + "\n"
            utilFile.writeOverFile(self.reportLoc, bloctext)
    def setBlocs(self, papeCache):
        self.blocs = papeCache.split("}\n\n")
    def searchForHashes(self):
        coms.NOTIFYSearchingForHashes()
        ready = []
        notready = []
        for fiObj in self.fiList:
            t,obj= self.searchForHash(fiObj)
            if t:
                ready.append(obj)
            else:
                notready.append(obj)
        self.fiList = notready
        return ready
    def searchForHash(self,fiObj):
        h = fiObj.GetHash()
        for bloc in self.blocs:
            if h in bloc:
                fiObj.SetBloc(bloc)
                return True, fiObj
        return False, fiObj
    def checkForLocalDuplicates(self):
        register = dict()
        i = 0
        while i < len(self.fiList):
            mark = True
            if checkDict(register,self.fiList[i].GetHash()):
                self.fiList[i].MoveToFolder(self.failLoc)
                del self.fiList[i]
                mark = False
            if mark:
                register[self.fiList[i].GetHash()] = ""
                i+=1