#!/usr/bin/python
#coding: utf-8

import Tkinter as tk
from Window_QueryCert import *
from Window_NewCert import *

class WindowPrincipal: 
    def __init__(self, master):
        self.master = master 
        self.frame = tk.Frame(self.master) 
        
        #Buttons
        self.buttonNewCertificate = tk.Button(self.frame, text = 'Nuevo Certificado', width = 25, command = self.new_cert) 
        self.buttonNewCertificate.grid(column=0,row=0)
        
        self.buttonRenewCertificate = tk.Button(self.frame, text = 'Renovar Certificado', width = 25)
        self.buttonRenewCertificate.grid(column=0,row=1)

        self.buttonQueryCertificate = tk.Button(self.frame, text = 'Consulta Certificado', width = 25, command = self.new_query)
        self.buttonQueryCertificate.grid(column=0,row=2) 
        
        #Create Frame    
        self.frame.pack()


    def new_cert(self): 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = WindowNewCert(self.newWindow)
        
    
    def new_query(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowQuery(self.newWindow)
        
        
    