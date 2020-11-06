#!/usr/bin/python

import Tkinter as tk
from Window_Principal import *
from Window_Consulta import *


def main(): 
    root = tk.Tk() 
    app = WindowPrincipal(root)
    
    root.title('Letsencrypt DTIC')
    root.geometry("600x300")
     
    root.mainloop() 

if __name__ == '__main__': 
    main() 