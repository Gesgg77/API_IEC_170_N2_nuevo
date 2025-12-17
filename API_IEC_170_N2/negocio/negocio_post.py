import requests
from prettytable import PrettyTable

def obtener_posts_api(url):
    tabla = PrettyTable(['ID', 'Título', 'Contenido', 'UserID'])
    r = requests.get(url)
    if r.status_code == 200:
        for p in r.json():
            tabla.add_row([p['id'], p['title'], p['body'], p['userId']])
        print(tabla)

def crear_post_api(url):
    post = {
        'userId': input('User ID: '),
        'title': input('Título: '),
        'body': input('Contenido: ')
    }
    r = requests.post(url, data=post)
    print(r.status_code)

def modificar_post_api(url):
    id_post = input('ID Post: ')
    post = {
        'title': input('Título: '),
        'body': input('Contenido: ')
    }
    r = requests.put(f'{url}/{id_post}', data=post)
    print(r.status_code)

def eliminar_post_api(url):
    id_post = input('ID Post: ')
    r = requests.delete(f'{url}/{id_post}')
    print(r.status_code)
