# -*- coding: utf-8 -*-
import config
import listener
import librarian



def main():
    configMngr = config.ConfigManager('config.ini')
    listeningPost = listener.Listener(configMngr)
    lib = librarian.Librarian(configMngr)
    while True:
        out = listeningPost.Listen()
        if out == 'pape':
            lib.NewPapeCache(listeningPost.GetPapeCache())
        elif out == 'import':
            lib.NewFiList(listeningPost.GetFiList()) 
    

    
#%%
main()
#%%

"""
if __name__ == "__main__":
    main()
"""