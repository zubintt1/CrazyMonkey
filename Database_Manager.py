import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Users import User
import datetime

class Dbwork:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://cmdd_admin:cmdd@2017@localhost:3306/Crazy_Monkey_dev_Db', echo=True)


    def connect_database_check(self):
        db = pymysql.connect("localhost","cmdd_admin","cmdd@2017","Crazy_Monkey_dev_Db")
        cursor = db.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Database Version =%s " % data+"Status= %s"+str(db.server_status))

    def connect_to_database(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_record = User("Bodhiswattwa","","Tewari",datetime.datetime(year=1993,month=5,day=5),"zubin@indialends.com","9555029279",self.engine)
        new_record.create_the_table_in_db()
        print("Created the Table")
        session.add(new_record)
        session.commit()


