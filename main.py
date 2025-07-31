from flask import Flask, render_template, request, redirect, url_for, flash
import os
from app.utils.helpers import cargar_trabajadores

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = "vinambra-secreta-123"  # Puedes cambiar esto por algo más bonito

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
            flash("✅ Trabajador añadido correctamente")
            return redirect(url_for("trabajadores"))
        else:
            flash("⚠️ Por favor completa todos los campos.")
            return redirect(url_for("añadir_trabajador"))


    return render_template("añadir_trabajador.html")
@app.route("/editar-trabajador/<int:indice>", methods=["GET", "POST"])
def editar_trabajador(indice):
    trabajadores = cargar_trabajadores()

    # Validar que el índice existe
    if indice < 0 or indice >= len(trabajadores):
        flash("⚠️ Trabajador no encontrado.")
        return redirect(url_for("trabajadores"))

    if request.method == "POST":
        nombre = request.form.get("nombre")
        rol = request.form.get("rol")

        if nombre and rol:
            trabajadores[indice]["nombre"] = nombre
            trabajadores[indice]["rol"] = rol

            # Guardar cambios
            with open("data/trabajadores.json", "w", encoding="utf-8") as f:
                import json
                json.dump(trabajadores, f, indent=4, ensure_ascii=False)

            flash("✅ Trabajador actualizado correctamente")
            return redirect(url_for("trabajadores"))
        else:
            flash("⚠️ Por favor completa todos los campos.")
            return redirect(url_for("editar_trabajador", indice=indice))

    # GET: mostrar el formulario con datos ya cargados
    trabajador = trabajadores[indice]
    return render_template("editar_trabajador.html", trabajador=trabajador, indice=indice)

if __name__ == "__main__":
    app.run(debug=True)
