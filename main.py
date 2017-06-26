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


class Master_Control(BoxLayout):
    alpha = 0

    def upload_file(self):
        self.alpha = self.alpha + 1
        print(self.alpha)

    def download_file(self):
        self.alpha = self.alpha - 1
        print(self.alpha)

    def start_ftp_server(self):
        a = Ftp_Control.random_port_gen(self)
        print("Ftp Server Running On 127.0.0.1 port=" + str(a))
        Ftp_Control.start_ftp_server(self,a)
        print("Ftp server started")


    # def show_load(self):
    #     content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
    #     self._popup.open()

#     def load(self, path, filename):
#         with open(os.path.join(path, filename[0])) as stream:
#             self.text_input.text = stream.read()
#         self.dismiss_popup()
#
#     def dismiss_popup(self):
#         self._popup.dismiss()
#
#     def work_on_something(self):
#         print("Hello Zubin")
#
#
# class LoadDialog(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)

class FileOperator(App):
    pass


if __name__ == '__main__':
    FileOperator().run()