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


class StageOneOperator(BoxLayout):
    alpha = 0

    def upload_file(self):
        self.alpha = self.alpha + 1
        print(self.alpha)

    def download_file(self):
        self.alpha = self.alpha - 1
        print(self.alpha)

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class FileOperator(App):
    pass


if __name__ == '__main__':
    FileOperator().run()