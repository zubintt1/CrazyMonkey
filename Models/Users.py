#from django.db import models
import datetime
#import sqlalchemy
from sqlalchemy import *
#from sqlalchemy import Column, Integer, String, DATETIME,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer,primary_key=True,autoincrement=True)#models.AutoField(primary_key=True)
    first_name = Column(String(100))#models.CharField(max_length=100)
    middle_name = Column(String(100))#models.CharField(max_length=100)
    last_name = Column(String(100))#models.CharField(max_length=100)
    date_of_birth = Column(DATETIME,nullable=True)#models.DateTimeField(auto_now_add=True,blank=True)
    email_id = Column(String(100))#models.CharField(max_length=100)
    mobile_number = Column(String(12))#models.IntegerField()
    user_date_created = Column(DATETIME,default=datetime.datetime.now())#models.DateTimeField(default=datetime.now)
    user_name = Column(String(40),default="")#models.CharField(max_length=40)
    user_password = Column(String(6000),default="")#models.CharField()
    is_password_reset = Column(Boolean,default=False)


    def __init__(self,first_name,middle_name,last_name,date_of_birth,email_id,mobile_number,engine):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email_id = email_id
        self.mobile_number = mobile_number
        self.engine = engine

    def set_username_passwd(self,user_name,password):
        self.user_name = user_name
        self.user_password = password

    def reset_password(self,flag):
        if (flag == True):
            self.is_password_reset = True
        else:
            self.is_password_reset = False

    def create_the_table_in_db(self):
        Base.metadata.create_all(self.engine)
        #meta = MetaData(bind=self.engine)
        #meta.create_all(self)