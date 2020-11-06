#!/usr/bin/python
#coding: utf-8

import paramiko
from Listas_ip import ListasIp

class StdoutRedirector(object):
    def __init__(self,text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')
        

    
def returnClientSSH(ip_servicio):

    clientssh = paramiko.SSHClient();
    clientssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    clientssh.connect(ip_servicio,username='',password='');
    
    return clientssh

'''Función para la obtención de la Ip Interna Dtic'''
def ip_of_vpn(ip_of_domain):
         
    #Obtenemos la ip privada del servidor
    ip_interna = ListasIp.get(ip_of_domain);
    
    return ip_interna;
