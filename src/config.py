# -*- coding: utf-8 -*-
import configparser
from utilFile import makeFullPath

# ConfigManager reads in and stores parameters from an .ini file
# It inherits from configparser class
class ConfigManager(configparser.ConfigParser):
    def __init__(self,filepath):
        self.filepath = filepath # store the filepath to enable later update
        configparser.ConfigParser.__init__(self) # call init from parent
        self.readIn() # build dictionary
        self.router = self.buildRouter()
        
    # buildRouter builds a router dictionary based on the lib location
    def buildRouter(self):
        router = dict()
        router['PaperPileCache'] = makeFullPath(self.Get("LibraryLocation"),"PaperPileCache.txt")
        router['Import'] = makeFullPath(self.Get("LibraryLocation"),"Import")
        router['HashLib'] = makeFullPath(self.Get("LibraryLocation"),"HashLib")
        router['FailedImport'] = makeFullPath(self.Get("LibraryLocation"),"FailedImport")
        router['Vault'] = makeFullPath(self.Get("LibraryLocation"),"Vault")
        router['DocLib'] = makeFullPath(self.Get("LibraryLocation"),"Vault\\DocLib")
        return router
    
    # readIn builds the configManager's dictionary
    def readIn(self):
        with open(self.filepath, "r") as configfile:
            self.read_file(configfile)
            
    # update returns a fresh config manager with new readin
    def update(self):
        return ConfigManager(self.filepath) # return copy
    
    # Get takes and attribute string, and returns the attribute
    def Get(self,attributeString):
        return self['DEFAULT'][attributeString]
    
    # GetPath takes a locString and returns a full path
    def GetPath(self, locString):
        return self.router[locString]
            


"""
example usage
config.ini
[DEFAULT]
ListenTick = 5
----------------
cm = ConfigManager('config.ini')    
print(cm.Get('ListenTick'))
print(cm.GetPath('DocLib'))

x = ConfigManager('config.ini')
print(x['DEFAULT']['ListenTick'])  out: 5

x = ConfigManager('config.ini')
print(x.Get("IgnoreList")) out: string
"""