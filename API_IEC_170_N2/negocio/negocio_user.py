import requests
from prettytable import PrettyTable

from modelos.modelos import User
from datos.datos import insertar_objeto, obtener_user_name


# =========================
# API
# =========================

def obtener_users_api(url):
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data Users...")
        usuarios = respuesta.json()

        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Usuario", "Email"]

        for user in usuarios:
            tabla.add_row([
                user["id"],
                user["name"],
                user["username"],
                user["email"]
            ])

            crear_user_db(
                user["name"],
                user["username"],
                user["email"],
                user["phone"],
                user["website"]
            )

        print(tabla)

    elif respuesta.status_code == 204:
        print("Consulta correcta, pero sin datos.")
    else:
        print(f"Error API: {respuesta.status_code}")


def crear_user_api(url):
    user = {
        "name": input("Nombre: "),
        "username": input("Usuario: "),
        "email": input("Email: "),
        "phone": input("Teléfono: "),
        "website": input("Website: ")
    }

    r = requests.post(url, data=user)
    print(r.status_code, r.text)


def modificar_user_api(url):
    id_user = input("ID usuario: ")

    user = {
        "name": input("Nombre: "),
        "username": input("Usuario: "),
        "email": input("Email: "),
        "phone": input("Teléfono: "),
        "website": input("Website: ")
    }

    r = requests.put(f"{url}/{id_user}", data=user)
    print(r.status_code)


def eliminar_user_api(url):
    id_user = input("ID usuario: ")
    r = requests.delete(f"{url}/{id_user}")
    print(r.status_code)


# =========================
# DB
# =========================

def crear_user_db(nombre, username, email, phone, website):
    if obtener_user_name(nombre):
        print("Usuario ya existe, no se agrega.")
        return

    user = User(
        None,
        nombre,
        username,
        email,
        phone,
        website
    )

    insertar_objeto(user)
