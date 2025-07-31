from flask import Flask, render_template, request, redirect, url_for
import os
from app.utils.helpers import cargar_trabajadores

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/trabajadores")
def trabajadores():
    lista = cargar_trabajadores()
    return render_template("trabajadores.html", trabajadores=lista)

@app.route("/añadir-trabajador", methods=["GET", "POST"])
def añadir_trabajador():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        rol = request.form.get("rol")

        if nombre and rol:
            trabajadores = cargar_trabajadores()
            nuevo = {"nombre": nombre, "rol": rol}
            trabajadores.append(nuevo)

            # Guardar en el JSON
            with open("data/trabajadores.json", "w", encoding="utf-8") as f:
                import json
                json.dump(trabajadores, f, indent=4, ensure_ascii=False)

            return redirect(url_for("trabajadores"))
        else:
            return "Faltan datos, por favor completa todos los campos."

    return render_template("añadir_trabajador.html")

if __name__ == "__main__":
    app.run(debug=True)
