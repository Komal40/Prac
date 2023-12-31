import mysql.connector
import json

class user_model():

    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost', user='root', password='admin', database='flask_practice')
            self.cur=self.con.cursor(dictionary=True)
            print('connection succesfull')
        except:
            print('some error')

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM USERS")
        res=self.cur.fetchall()
        return json.dumps(res)
