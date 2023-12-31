import mysql.connector

class user_model():

    def __init__(self):
        try:
            con=mysql.connector.connect(host='localhost', user='root', password='admin', database='flask_practice')
            print('connection succesfull')
        except:
            print('some error')

    def user_getall_model(self):
        return 'user_getall_model'
