import os
from Models.Users import User
import datetime
from Models.User_Data import User_Data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Initialize_Project():

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://cmdd_admin:cmdd@2017@localhost:3306/Crazy_Monkey_dev_Db',
                                    echo=True)
        new_record = User(self.engine)
        new_record.create_the_table_in_db()
        new_user_data_record = User_Data.create_the_table_in_db(self)
        print("Initiation Done")
