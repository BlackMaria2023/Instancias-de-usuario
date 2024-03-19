import json

instancias_usuarios = []

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.genero = genero

def crear_instancia_usuario(datos):
    try:
        datos_usuario = json.loads(datos)
        usuario = Usuario(datos_usuario['nombre'], datos_usuario['apellido'], datos_usuario['email'], datos_usuario['genero'])
        return usuario
    except Exception as e:
        with open("error.log", "a") as error_file:
            error_file.write(f"Error al crear instancia de usuario: {str(e)}\n")
        return None

with open("usuarios.txt") as usuarios_file:
    for linea in usuarios_file:
        usuario = crear_instancia_usuario(linea.strip())
        if usuario:
            instancias_usuarios.append(usuario)

print(instancias_usuarios)