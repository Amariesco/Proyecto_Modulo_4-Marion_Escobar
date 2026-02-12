# Tendra codigo base para el proyecto, como la inicializacion de la aplicacion, configuraciones, etc

from gestor import GestorClientes 
from modelos import Cliente, ClienteVIP, ClienteCorporativo

def main():
    sistema = GestorClientes()

    while True: #Bucle infinito ya que solo se detendra cuando el usuario ingrese la opcion 6 de "Guardar y Salir"
        #Comienza mostrando menú principal con opciones para el usuario.
        print("\n--- MENÚ PARA GESTIÓN DE CLIENTES ---") 
        print("1. Crear Cliente") 
        print("2. Lista de Clientes")
        # print("3. Editar Cliente")
        # print("4. Eliminar Cliente")
        # print("5. Buscar Cliente")
        print("6. Guardar y Salir")
        
        opcion = input("Ingrese una opción: ")