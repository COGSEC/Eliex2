# -*- coding: utf-8 -*-
from utilParse import removeConsecutiveSpaces
from utilParse import removeControlCharacters
from utilParse import findStrangeDatum
from utilParse import findSubstring

class blocParser:
    def __init__(self):
        self.bloc = ""
        self.author = ""
        self.year = ""
        self.title = ""
    def ParseBloc(self,fiObj):
        self.bloc = fiObj.GetBloc()
        fiObj.SetTitleAuthorYear(self.getTitle(), self.getAuthor(),self.getYear())
        return fiObj
    def getAuthor(self):
        return removeConsecutiveSpaces(removeControlCharacters(findStrangeDatum(self.bloc,"= \"","\",", startIndexAt=findSubstring(self.bloc,"  author"))))
    def getYear(self):
        return removeConsecutiveSpaces(removeControlCharacters(findStrangeDatum(self.bloc,"=  ", ",", startIndexAt=findSubstring(self.bloc,"  year"))))
    def getTitle(self):
        return removeConsecutiveSpaces(removeControlCharacters(findStrangeDatum(self.bloc,"= \"","\",", startIndexAt=findSubstring(self.bloc,"  title"))))



"""
import config
import listener
import librarian

cm = config.ConfigManager('config.ini')
post = listener.Listener(cm)
post.listenToPapeCache()
pcache = post.GetPapeCache()
lib = librarian.Librarian(cm)
lib.setBlocs(pcache)

bp = blocParser(lib.blocs[1])
print(bp.getAuthor())
print(bp.getYear())
print(bp.getTitle())



from utilParse import removeConsecutiveSpaces
from utilParse import removeControlCharacters
from utilParse import findStrangeDatum
x = lib.blocs[1]
y = utilParse.findSubstring(x,"  author")
z = removeConsecutiveSpaces(removeControlCharacters(findStrangeDatum(x,"= ","\",",startIndexAt=y)))
"""