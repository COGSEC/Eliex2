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
        d =  self.Get("LibraryLocation")
        router['PaperPileCache'] = makeFullPath(d,"PaperPileCache.txt")
        router['Import'] = makeFullPath(d,"Import")
        router['HashLib'] = makeFullPath(d,"HashLib")
        router['FailedImport'] = makeFullPath(d,"FailedImport")
        router['Vault'] = makeFullPath(d,"Vault")
        router['DocLib'] = makeFullPath(d,"Vault\\DocLib")
        router['Report'] = makeFullPath(d,"Report.csv")
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