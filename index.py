from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ventajas')
def ventajas():
    return render_template('ventajas.html')

@app.route('/desventajas')
def desventajas():
    return render_template('desventajas.html')

@app.route('/empresas')
def empresas():
    return render_template('empresas.html')

@app.route('/formularioC')
def formularioC():
    return render_template('formularioC.html')

@app.route('/formularioR')
def formularioR():
    return render_template('formularioR.html')

@app.route('/formularioE')
def formularioE():
    return render_template('formularioE.html')

if __name__ == '__main__':
    app.run(debug=True)
