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

class Master_Control(BoxLayout):
    alpha = 0
    server_port = 0


    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            file_content = stream.read()

        return file_content
        # self.dismiss_popup()

    def upload_file(self, path, filename):
        # print("Path="+str(path)+"\nFile Name="+str(filename))
        content = self.load(path,filename)
        self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()
        self.alpha = self.alpha + 1
        print(self.alpha)

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


    # def show_load(self):
    #     content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
    #     self._popup.open()



    def dismiss_popup(self):
        self._popup.dismiss()
#
#     def work_on_something(self):
#         print("Hello Zubin")
#
#


class FileOperator(App):
    pass


if __name__ == '__main__':
    FileOperator().run()