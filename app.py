from flask import Flask, render_template
from flask import request
import controlador


app = Flask(__name__)

@app.route("/")
def incio():
	return render_template("index.html")

@app.route("/iniciar_sesion")
def iniciarSesion():
	return render_template("iniciar_sesion.html")

@app.route("/registrar")
def registrar():
	return render_template("registrarme.html")

@app.route("/guardar", methods=['POST'])
def guardar():
	nombre = request.form['nombre']
	apellido = request.form['apellido']
	email = request.form['email']
	nickname = request.form['nickname']
	password = request.form['password']
	edad = request.form['edad']
	peso = request.form['peso']
	altura = request.form['altura']
	controlador.insertar_usuarios(nombre, apellido, email, nickname, password, edad, peso, altura)
	registro = "Gracias por formar parte de nuestra base de datos!"
	return render_template("principal.html", registro = registro)


@app.route("/login", methods=['POST'])
def login():
	nickname = ""
	password = ""
	nickname = request.form['nickname']
	password = request.form['password']
	usuario = controlador.login_usuario()
	for usuario in usuario:
		if usuario[0].lower() == nickname.lower() and usuario[1] == password:
			iniciado = "Has iniciado sesión correctamente!"
			return render_template("principal.html", iniciado = iniciado)
	else:
		mensaje = "Usuario o contraseña incorrecto!!"
		return render_template("iniciar_sesion.html", mensaje = mensaje)


if __name__ == '__main__':
	app.run(debug = True)