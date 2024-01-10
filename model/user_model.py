import mysql.connector
import json
from flask import make_response

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
        if len(res)>0:
            return make_response({"payload":res}, 200)
        else:
            return make_response({"msg":"No Data Found"}, 204)

    

    def add_one_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone) VALUES('{data['name']}', '{data['email']}', '{data['phone']}')")
        return make_response({"msg":'User connected successfully'}, 201)
    
    
    def update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}' WHERE id='{data['id']}' ")
        if self.cur.rowcount>0:
            return make_response({"msg":'Updated successfully'}, 201)
        else:
            return make_response({"msg":'Nothing to update'}, 202)
            


    def delete_model(self, data):
        self.cur.execute(f"DELETE from USERS WHERE id={data} ")
        if self.cur.rowcount>0:
            return make_response({"msg":'Deleted successfully'},200)
        else:
            return make_response({"msg":'Nothing to delete'},202)
        



