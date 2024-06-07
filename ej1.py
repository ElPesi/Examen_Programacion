import requests
import json
import os

def obtener_publicaciones(cantidad):
    api_url = f'https://jsonplaceholder.typicode.com/posts?_limit={cantidad}'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos de la API.")
        return None


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def guardar_datos(data, filename):
    with open(filename, 'w') as archivo:
        json.dump(archivo, ident =  4)
    
def main():
    contador_uso_api = 1
    
    while True:
        
        cantidad = int(input("¿Cuantas publicaciones quieres?"))
        if cantidad <= 0 or cantidad > 100:
            return ValueError
        print("Por favor, introduce un numero valido entre 1 y 100")
        break

    publicaciones = obtener_publicaciones(cantidad)
        
    if publicaciones is None:
        return
            
    post_primos = {}
    post_no_primos = {}
        
    for post in publicaciones:  
        post_id = post['id']
        if es_primo(post_id):
            post_primos[post_id] = post
        else:
            post_no_primos[post_id] = post
            
    if not os.path.exists('Downloads'):
        os.makedirs('Downloads')
        
    filename_primos = f'Downloads/dlXPrimes_.json'
    filename_no_primos = f'Downloads/dlXNotPrimes.json'

    guardar_datos(post_primos, filename_primos)
    guardar_datos(post_no_primos, filename_no_primos)

    print(f"Datos guardados en {filename_primos} y {filename_no_primos}")

                        