from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Chores"

if __name__=="__main__":
    app.run()
