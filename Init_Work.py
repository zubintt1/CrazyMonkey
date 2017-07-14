import os
from Models.Users import User
import datetime
from Models.User_Data import User_Data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql


class Initialize_Project():

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://cmdd_admin:cmdd@2017@localhost:3306/Crazy_Monkey_dev_Db',
                                    echo=True)
        db = pymysql.connect("localhost", "cmdd_admin", "cmdd@2017", "Crazy_Monkey_dev_Db")
        cursor_one = db.cursor()
        new_record = User(self.engine)
        cursor_one.execute("SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Crazy_Monkey_dev_Db') AND (TABLE_NAME = '"+new_record.__tablename__+"')")
        result_one = cursor_one.fetchone()
        print("User Table Created Status="+str(result_one[0]))
        if result_one[0] < 1:
            new_record.create_the_table_in_db()

        new_user_data_record = User_Data(self.engine)
        cursor_two = db.cursor()
        cursor_two.execute("SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Crazy_Monkey_dev_Db') AND (TABLE_NAME = '"+new_user_data_record.__tablename__+"')")
        result_two = cursor_two.fetchone()
        print("User Data Table Created Status=" + str(result_two[0]))
        if result_two[0] < 1:
            new_user_data_record.create_the_table_in_db()
        print("Initiation Done")
