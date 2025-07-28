from flask import Flask, render_template
from app.utils.helpers import cargar_trabajadores

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/trabajadores")
def trabajadores():
    lista = cargar_trabajadores()
    return render_template("trabajadores.html", trabajadores=lista)

if __name__ == "__main__":
    app.run(debug=True)
