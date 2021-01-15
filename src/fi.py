# -*- coding: utf-8 -*-

from utilFile import makeFile
from utilFile import makeFullPath
from utilFile import getFileName
from utilFile import getExt
from utilHash import getMD5
from utilFile import moveToFolder
from utilFile import renameAndMove
from coms import ASKforShortTitle
from coms import ASKforProject
from coms import NOTIFYforHashHandling

class fileInfo:
    def __init__(self, path):
        # stage 1 items
        self.path = path
        self.filename = getFileName(path)
        self.ext = getExt(path)
        self.hash = getMD5(path)
        # stage 2 items        
        self.bloc = ""
        # stage 3 items
        self.shortTitle = ""
        self.author = ""
        self.year = ""
        self.title = ""
        self.project = "[[MISC]]"
    def SetTitleAuthorYear(self, title,author,year):
        self.author = author
        self.year = year
        self.title = title
    def ASKforShortTitle(self):
        self.shortTitle = ASKforShortTitle(self)
        self.ASKforProject()
    def ASKforProject(self):
        self.project = ASKforProject()
    def NOTIFYforHashHandling(self):
        NOTIFYforHashHandling(self.filename, self.hash)
    def SetBloc(self, bloc):
        self.bloc = bloc
    def GetBloc(self):
        return self.bloc
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
        renameAndMove(self.path,folder,self.shortTitle+self.ext)
    def writeReportString(self):
        rs = ""
        rs += self.hash +", "
        rs += self.filename
        return rs
    def makeHashFile(self,hashLib):
        makeFile(makeFullPath(hashLib,self.hash),"")
    def makeMdFile(self,vault):
        fullbloc = self.bloc
        fullbloc += "\n"+"FILE: ![[docLib/"+self.shortTitle+self.ext+"]]"
        fullbloc += "\n PROJECT: " + self.project
        makeFile(makeFullPath(vault,self.shortTitle+".md"),fullbloc)
    def Archive(self,vault,doclib,hashlib):
        self.makeMdFile(vault)
        self.makeHashFile(hashlib)
        self.RenameAndMove(doclib)
        
        