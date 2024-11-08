from flask import Flask,render_template,request
app=Flask(__name__)
#server web- codice per restituire la homepage
@app.route("/")
def homepage():
    return render_template("index.html")

#server API
@app.route("/calcola",methods=[post])
def calcola():
    dati = request.get_json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)