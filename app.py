from flask import Flask

app = Flask(__name__)

   
@app.route('/')
def homepage():
    return "Home page AQUI. <a href='agur'>Pinchar aqui</a> para ir al agur page"# a href='/' for homepage

@app.route("/agur")

def agur():
    return "<h1> AGUR </h1>"
    app.run()

if __name__ == "__main__":
    app.run()