from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "home route"

# api endpoint

@app.route("/test", methods=["POST"])
def about():
    data = request.json
    print(data)
    return "about route abc"

@app.route("/update", methods=["PUT"])
def updateNote():
    return "Note Update Success"

@app.route("/remove", methods=["DELETE"])
def delet():
    return "Note update delete"


#server on
app.run(debug=True)