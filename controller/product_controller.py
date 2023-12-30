from app import app

@app.route('/product/app')
def product():
    return 'product operation'