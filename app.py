from flask import *
app = Flask(__name__)

chore = {"name":"Take out the trash", "recurring":False, "frequency":None}
demochore = {"chores":[
        {"priority":5, "active":True, "user":None, "chore":chore}
        ]}


@app.route('/')
def index():
    return "Chores"

@app.route('/chores.json')
def chores():
    return jsonify(demochore)

if __name__=="__main__":
    app.run(port=5000, debug=True)
