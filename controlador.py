from conexion import obtener_conexion

def insertar_usuarios(nom, ape, email, nickname, password, ed, alt, peso):
	conexion = obtener_conexion()
	with conexion.cursor() as cursor:
		cursor.execute("INSERT INTO usuarios(nombre, apellido, email, nickname, password, edad, peso, altura) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (nom, ape, email, nickname, password, ed, alt, peso))
	conexion.commit()
	conexion.close()

# def buscar_usuario(nick, passw):
# 	conexion = obtener_conexion()
# 	with conexion.cursor() as cursor:
# 		cursor.execute("SELECT * FROM usuarios WHERE nickname = %s AND password = %s", (nick, passw))
# 		user = cursor.fetchone()
# 		if user:
# 			session['nickname'] = user['nickname']
# 		conexion.close()

def login_usuario():
	conexion = obtener_conexion()
	usuario = []
	with conexion.cursor() as cursor:
		cursor.execute("SELECT nickname, password, nombre FROM usuarios")
		usuario = cursor.fetchall()
	conexion.close()
	return usuario

