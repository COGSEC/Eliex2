# -*- coding: utf-8 -*-

import utilFile

class Librarian:
    def __init__(self, configMngr):
        self.vault = configMngr.GetPath('Vault')
        self.docLib = configMngr.GetPath('DocLib')
        self.hashLib =  configMngr.GetPath('HashLib')
        self.reportLoc =  configMngr.GetPath('Report')
        self.blocs = []
        self.fiList = []
    def NewPapeCache(self, papeCache):
        self.setBlocs()
        self.Update()
    def NewFiList(self,fiList):
        self.fiList = fiList
        self.Update()
    def Update(self):
        ready = self.searchForHashes()
        self.writeReport()
        self.archive(ready)
    def archive(self,ready):
        self.askForNames(ready)
        for fiObj in ready:
            fiObj.Archive(self.vault,self.docLib,self.hashLib)
    def askForNames(self,ready):
        for fiObj in ready:
            fiObj.ASKforShortTitle()
    def writeReport(self):
        bloctext = ""
        for fiObj in self.fiList:
            bloctext += fiObj.writeReportString() +"\n"
        utilFile.writeOverFile(self.reportLoc, bloctext)
    def setBlocs(self, papeCache):
        self.blocs = papeCache.split("}\n\n")
    def searchForHashes(self):
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