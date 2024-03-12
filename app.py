from flask import Flask, render_template

app = Flask(__name__)

#def calcular ():functions outside of route
from producto import Producto

@app.route('/')
def homepage():
    return "Home page AQUI. <a href='agur'>Pinchar aqui</a> para ir al agur page"# a href='/' for homepage

@app.route("/agur")

def agur():
    #calcular()
    return "<h1> AGUR </h1>"
    app.run()

@app.route("/lambda")
def calcularlamba():
    posneg = lambda x: "Positivo" if x>0 else "negativo"
    return posneg(10) 

@app.route("/pagina1")
def pagina1():
    return app.send_static_file("pagina1.html")

# @app.route("/pagina2")
# def pagina2():
#     return app.send_static_file


@app.route("/dinamica1")
def dinamica1():
    nombre = " Jon"
    edad = 25
    frutas = ["kiwi", "PLATANO" ,"fresas", "PERA", "manzanas",  "mango"]
    return render_template("pagina1.html", nombre=nombre, edad=edad, frutas=frutas)

if __name__ == "__main__": 
    app.run(debug=True, port=5000)


@app.route("/productos")
def productos():
        p1 = Producto(1, "Raqueta", 5.99, ".")
        p2 = Producto(2, "Balon", 9.99, ".")
        p3 = Producto(3, "Lavadora", 19.99,".")
        listaProductos = [p1, p2, p3]

        
        return render_template("productos.html", listaProductos=listaProductos)