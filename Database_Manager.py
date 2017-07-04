import pymysql

class Dbwork:

    def connect_database_check(self):
        db = pymysql.connect("localhost","cmdd_admin","cmdd@2017","Crazy_Monkey_dev_Db")
        cursor = db.cursor()
        cursor.execute("select * from sys.tables")
        data = cursor.fetchone()
        print("Database Version =%s " % data+"Status= %s"+str(db.server_status))
