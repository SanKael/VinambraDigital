import json

def cargar_trabajadores():
    with open("data/trabajadores.json", encoding="utf-8") as f:
        return json.load(f)

