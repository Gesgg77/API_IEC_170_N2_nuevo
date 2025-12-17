# api_menu.py — pega todo esto y guarda
from negocio.negocio_user import (
    obtener_users_api,
    crear_user_api,
    modificar_user_api,
    eliminar_user_api
)

from negocio.negocio_post import (
    obtener_posts_api,
    crear_post_api,
    modificar_post_api,
    eliminar_post_api
)

URL_USERS = 'https://jsonplaceholder.typicode.com/users'
URL_POSTS = 'https://jsonplaceholder.typicode.com/posts'

def menu():
    while True:
        print('''
=== MENÚ API ===
1. Obtener users API -> guardar DB
2. Crear user API
3. Modificar user API
4. Eliminar user API
5. Obtener posts API -> guardar DB
6. Crear post API
7. Modificar post API
8. Eliminar post API
0. Salir
''')
        opcion = input('Opción: ').strip()
        if opcion == '1':
            obtener_users_api(URL_USERS)
        elif opcion == '2':
            crear_user_api(URL_USERS)
        elif opcion == '3':
            id_user = input('ID usuario a modificar: ').strip()
            modificar_user_api(f'{URL_USERS}/{id_user}')
        elif opcion == '4':
            id_user = input('ID usuario a eliminar: ').strip()
            eliminar_user_api(f'{URL_USERS}/{id_user}')
        elif opcion == '5':
            obtener_posts_api(URL_POSTS)
        elif opcion == '6':
            crear_post_api(URL_POSTS)
        elif opcion == '7':
            id_post = input('ID post a modificar: ').strip()
            modificar_post_api(f'{URL_POSTS}/{id_post}')
        elif opcion == '8':
            id_post = input('ID post a eliminar: ').strip()
            eliminar_post_api(f'{URL_POSTS}/{id_post}')
        elif opcion == '0':
            print('Saliendo.')
            break
        else:
            print('Opción inválida. Intenta otra vez.')

if __name__ == '__main__':
    print('>>> INICIO api_menu.py')
    menu()
    print('>>> FIN api_menu.py')
