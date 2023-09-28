
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #crear una URL ppal
#cuando ingrese a mi pagina principal, el usuaio que va a hacer?
def home ():
    return render_template('home.html') #'Home Page'

@app.route('/about')

def about ():
    return render_template('about.html') #'About Page'

@app.route('/glosario')

def glosario ():
    return render_template('glosario.html') #'glosario Page'

# para que escuche el server nuestro navegador
if __name__ == '__main__':
    app.run(debug=True)


 