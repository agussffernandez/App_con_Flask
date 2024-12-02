# flask: es un microframework para construir aplicaciones web en Python
# se instala con pip install Flask

# Importamos Flask desde el paquete flask
from flask import Flask, render_template

# Creamos una instancia de la clase Flask. Esta instancia es la aplicación web.
# Se le pasa como argumento: __name__ 
app = Flask(__name__)

# Define la ruta raíz
@app.route("/")
def principal():
    return render_template("index.html")


@app.route("/lenguajes")
def mostrarLenguajes():
    mis_lenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template("lenguajes.html", lenguajes = mis_lenguajes)


# Define la ruta contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# Ejecuta en un navegador web el resultado
if __name__ == "__main__":
    app.run(debug=True, port=5017) 
