
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User_Data(Base):
    __tablename__ = 'User_Data'
    file_id = Column(Integer, primary_key=True, autoincrement=True)  # models.AutoField(primary_key=True)
    user_id = Column(Integer,ForeignKey('user_id'))
    file_name = Column(String(100))
    file_date_created = Column(DATETIME, default=datetime.datetime.now())
    file_location = Column(VARCHAR(None))

    def __init__(self,user_id,file_name,file_location,engine):
        self.user_id = user_id
        self.file_name = file_name
        self.file_location = file_location
        self.engine = engine

    def create_the_table_in_db(self):
        Base.metadata.create_all(self.engine)


