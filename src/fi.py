# -*- coding: utf-8 -*-

from utilFile import makeFile
from utilFile import makeFullPath
from utilFile import getFileName
from utilHash import getMD5
from utilFile import moveToFolder
from utilFile import renameAndMove
from coms import ASKforShortTitle
from coms import NOTIFYforHashHandling

class fileInfo:
    def __init__(self, path):
        # stage 1 items
        self.path = path
        self.filename = getFileName(path)
        self.hash = getMD5(path)
        # stage 2 items        
        self.bloc = ""
        # stage 3 items
        self.shortTitle = ""
    def ASKforShortTitle(self):
        self.shortTitle = ASKforShortTitle(self.filename)
    def NOTIFYforHashHandling(self):
        NOTIFYforHashHandling(self.filename, self.hash)
    def SetBloc(self, bloc):
        self.bloc = bloc
    def GetHash(self):
        return self.hash
    def GetPath(self):
        return self.path
    def GetFileName(self):
        return self.filename
    def GetShortTitle(self):
        return self.shortTitle
    def MoveToFolder(self,folder):
        moveToFolder(self.path,folder)
    def RenameAndMove(self, folder):
        renameAndMove(self.path,folder,self.shortTitle)
    def writeReportString(self):
        rs = ""
        rs += self.hash +", "
        rs += self.filename
        return rs
    def makeHashFile(self,hashLib):
        makeFile(makeFullPath(hashLib,self.hash),"")
    def makeMDFile(self,vault):
        makeFile(makeFullPath(vault,self.shortTitle+".md"),self.bloc)
    def Archive(self,vault,doclib,hashlib):
        self.makeMDfile(vault)
        self.makeHashFile(hashlib)
        self.RenameAndMove(doclib)
        
        