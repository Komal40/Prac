from app import app
from model.user_model import user_model
from flask import request

obj=user_model()

@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods=['POST'])
def add_one_controller():
    return obj.add_one_model(request.form)

@app.route('/user/update', methods=['PUT'])
def update_controller():
    return obj.update_model(request.form)
