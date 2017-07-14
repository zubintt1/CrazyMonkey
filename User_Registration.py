#! /bin/env python


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import static_components
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql


class User_Registration(BoxLayout):

    def build(self):
        kv_file_path = static_components.View_Path+"\\User_Registration.kv"
        self.load_kv(kv_file_path)


