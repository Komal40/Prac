import mysql.connector
import json

class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost', user='root', password='admin', database='flask_practice')
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print('connection succesfull')
        except:
            print('some error')


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM USERS")
        res=self.cur.fetchall()
        # return json.dumps(res)
        return {"payload":res}
    

    def add_one_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone) VALUES('{data['name']}', '{data['email']}', '{data['phone']}')")
        return {"msg":'User connected successfully'}
    
    def update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}' WHERE id='{data['id']}' ")
        if self.cur.rowcount>0:
            return {"msg":'Updated successfully'}
        else:
            return {"msg":'Nothing to update'}
            


    def delete_model(self, data):
        self.cur.execute(f"DELETE from USERS WHERE id={data} ")
        if self.cur.rowcount>0:
            return {"msg":'Deleted successfully'}
        else:
            return {"msg":'Nothing to delete'}