#!/usr/bin/python
#coding: utf-8

import Tkinter as tk
import paramiko
import socket
from General_Functions import returnClientSSH
from General_Functions import ip_of_vpn
from Listas_ip import ListasIp

class WindowQuery:
     
    def __init__(self, master): 
        self.master = master
        self.createWindow()
        
    def createWindow(self):
            
        #Acción de consulta
        def actionConsulta(arg=None):
            
            Dominio = insertDominio.get()
            
            #Obtenemos hacia donde esta apuntando el dominio principal
            ip_of_domain = socket.gethostbyname(Dominio);
            
            #Obtenemos la ip interna para la conexión SSH
            ip_interna = ip_of_vpn(ip_of_domain);
            
            #Obtenemos ip interna
            result = "";
            clientssh = returnClientSSH(ip_interna);
            
            comando='/usr/local/letsencrypt/letsencrypt-auto certificates';
            stdin, stdout, stderr = clientssh.exec_command(comando);
    
            for line in stdout:
                result += line;
                
            clientssh.close()
                    
            boxStdout.config(text=result)
            insertDominio.delete(0, 100)     
        
        #Creación ventana y consulta
        self.frame = tk.Frame(self.master, height="800", width="600")
        
        labelDominio = tk.Label(self.frame, text="Nombre de dominio")
        labelDominio.grid(column=0,row=0, sticky='NS')
        
        insertDominio = tk.Entry(self.frame);
        insertDominio.focus()
        insertDominio.bind("<Return>",actionConsulta)
        insertDominio.grid(column=1,row=0, sticky='NS')
        
        boxStdout = tk.Label(self.frame, text="", height=40, width=50)
        boxStdout.grid(column=0,row=1, sticky='NS')
               
        buttonQuery = tk.Button(self.frame, text="Consultar", width=25, command=actionConsulta)
        buttonQuery.grid(column=1,row=1, sticky='NS')
        
    
        self.frame.pack()
        
    def close_windows(self): 
        self.master.destroy() 
        
    
    
            

    
    
    
    
    
    
    
        