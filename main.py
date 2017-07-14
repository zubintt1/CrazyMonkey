#! /bin/env python

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooser
from kivy.uix.filechooser import FileChooserIconView
import os
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from ftp_module import Ftp_Control
import threading
from ftplib import FTP
import sys
import re
from Database_Manager import Dbwork
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from Init_Work import Initialize_Project
import static_components


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Master_Control(BoxLayout):
    alpha = 0
    server_port = 0
    text_input = ObjectProperty(None)


    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0]),encoding="utf8") as stream:
            self.text_input.text = stream.read()

        #return file_content
        self.dismiss_popup()

    def get_file_to_upload(self,path,filename):
        with open(os.path.join(path, filename[0]),encoding="utf8",mode='r') as stream:
            self.text_input.text = stream.read()




    def upload_file(self, path, filename):
        file_to_upload = open(os.path.join(path, filename[0]),'rb')
        host = '127.0.0.1'
        port = self.server_port
        ftp_connection = FTP()
        try:
            ftp_connection.connect(host,port)
            message = ftp_connection.login('user', '12345')
            print(message)
            temp_file_name = filename[0]
            temp_file_names = temp_file_name.split('\\')
            ftp_connection.storbinary('STOR '+temp_file_names[1],file_to_upload)
            file_to_upload.close()
            ftp_connection.quit()
            print("File Upload Done")
        except:
            print(sys.exc_info())
            print("File Upload Not Done")

        self.alpha = self.alpha + 1
        print(self.alpha)

    def check_database(self):
        db_work = Dbwork()
        db_work.check_tables()
        print("Database Connectivity Check Done")

    def download_file(self):
        self.alpha = self.alpha - 1
        print(self.alpha)

    def ftp_connection_check(self):
        host = '127.0.0.1'
        port = self.server_port

        ftp_connection = FTP()
        try:
            ftp_connection.connect(host,port)
            message = ftp_connection.login('user','12345')
            print(message)
        except:
            print(sys.exc_info()[0])
        print("Login Check Done")

    def start_ftp_server(self):
        a = Ftp_Control.random_port_gen(self)
        self.server_port = a
        print("Ftp Server Running On 127.0.0.1 port=" + str(a))
        ftp_thread = threading.Thread(name='ftp_thread',target=Ftp_Control.start_ftp_server,args=(self,a))
        ftp_thread.setDaemon(True)
        ftp_thread.start()
        print("Ftp server started")


class FileOperator(App):
    i_p = Initialize_Project()
    pass

    def build(self):
        kv_file_path = static_components.View_Path+"\\FileOperator.kv"
        self.load_kv(kv_file_path)


if __name__ == '__main__':
    FileOperator().run()