from application import app

@app.route('/')
def home():
    return "Welcome to BlogLite!"
