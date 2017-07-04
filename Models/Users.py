#from django.db import models
import datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String, DATETIME



class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer,primary_key=True,autoincrement=True)#models.AutoField(primary_key=True)
    first_name = Column(String(100))#models.CharField(max_length=100)
    middle_name = Column(String(100))#models.CharField(max_length=100)
    last_name = Column(String(100))#models.CharField(max_length=100)
    date_of_birth = Column(DATETIME,nullable=True)#models.DateTimeField(auto_now_add=True,blank=True)
    email_id = Column(String(100))#models.CharField(max_length=100)
    mobile_number = Column(Integer)#models.IntegerField()
    user_date_created = Column(DATETIME,default=datetime.datetime.now())#models.DateTimeField(default=datetime.now)
    user_name = Column(String(40))#models.CharField(max_length=40)
    user_password = Column(String)#models.CharField()

    class Meta:
        db_table = "Users"
