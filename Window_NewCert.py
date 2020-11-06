#!/usr/bin/python
#coding: utf-8
import Tkinter as tk
from macpath import split
from Tkinter import IntVar


class WindowNewCert:
    
    def __init__(self, master):
        self.master = master
        self.createWindow()
        
    def createWindow(self):
        
        def actionNewCertificate():
            
            principaldomain = insertPrincipalDomain.get();
            
            domainsofinsert = insertListaDominios.get();
            
            domains = domainsofinsert.split(',');
            
            pathWeb = insertPathWeb.get();
            
            check1 = checkVar1.get();
            
            check2 = checkVar2.get();
            
            check3 = checkVar3.get();
            
            print principaldomain, domainsofinsert, domains, pathWeb, check1, check2, check3
        
        
        self.frame = tk.Frame(self.master, height=800, width=600)
        
        #Formulario
        labelPrincipalDomain = tk.Label(self.frame, text="Dominio Principal")
        labelPrincipalDomain.grid(column=0,row=0,sticky='NS');
        
        insertPrincipalDomain = tk.Entry(self.frame)
        insertPrincipalDomain.grid(column=1,row=0,sticky='NS')
        
        labelListaDominios = tk.Label(self.frame, text="Lista de Dominios")
        labelListaDominios.grid(column=0,row=1,sticky='NS')
        
        insertListaDominios = tk.Entry(self.frame)
        insertListaDominios.grid(column=1,row=1,sticky='NS')
        
        labelPathWeb = tk.Label(self.frame, text="Path de la web")
        labelPathWeb.grid(column=0,row=2,sticky='NS')
        
        insertPathWeb = tk.Entry(self.frame)
        insertPathWeb.grid(column=1,row=2,sticky='NS')
        
        #Valores check 1 encencido - 0 apagado
        checkVar1 = IntVar();
        checkVar2 = IntVar();
        checkVar3 = IntVar();

        
        checkManual = tk.Checkbutton(self.frame, text="Manual", variable = checkVar1, onvalue=1, offvalue=0)
        checkManual.grid(column=0, row=3)
        
        checkHttp   = tk.Checkbutton(self.frame, text="Http", variable = checkVar2, onvalue=1, offvalue=0)
        checkHttp.grid(column=1, row=3)
        
        checkWebroot = tk.Checkbutton(self.frame, text="Webroot", variable = checkVar3, onvalue=1, offvalue=0)
        checkWebroot.grid(column=2,row=3)
        
        #Boton Acción
        buttonNewCert = tk.Button(self.frame, text="Crear Certificado",command=actionNewCertificate)
        buttonNewCert.grid(column=0,row=4,sticky='NS')
        
        self.frame.pack()
        
        
            
            
            
                   
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        