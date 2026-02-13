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
        print("4. Eliminar Cliente")
        # print("5. Buscar Cliente")
        print("6. Guardar y Salir")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1": # Si el usuario elige la opción 1, se le solicitará ingresar los datos del cliente y se creará un nuevo cliente según el tipo seleccionado.
            nom = input("\nNombre: ")
            
            while True: # Validación de Email utilizando el método estático del gestor para asegurar que el formato sea correcto antes de continuar con la creación del cliente.
                ema = input("\nEmail (ejemplo@dominio.com): ")
                if sistema.validar_email(ema):
                    break
                print("Error: Verifique el email, este debe contener '@' y un '.' después de la arroba para ser válido.")
            
            while True: # Validación de Fono utilizando el método estático del gestor para asegurar que el número tenga exactamente 11 dígitos y solo contenga números antes de continuar con la creación del cliente.
                fon = input("\nFono (ingresar 11 dígitos numéricos, ej: 56912345678): ")
                if sistema.validar_fono(fon):
                    break
                print("Error: Verifique el fono, este debe tener exactamente 11 números (sin espacios ni signos).")
            
            print("\nTipos de clientes: 1. Regular | 2. VIP | 3. Corporativo \n *(Si selecciona otro numero se asignara automaticamente como Regular)*\n") 
            tipo = input("\nIngrese una opcion: ")
            nuevo_id = sistema.generar_id()

            if tipo == "2": # Si el usuario selecciona VIP, se le solicitará ingresar el porcentaje de descuento y se creará un cliente VIP con ese descuento.
                desc = int(input("% Descuento: "))
                nuevo = ClienteVIP(nuevo_id, nom, ema, fon, desc)
            elif tipo == "3":
                empresa = input("Nombre de la Empresa: ")
                nuevo = ClienteCorporativo(nuevo_id, nom, ema, fon, empresa)
            else:
                nuevo = Cliente(nuevo_id, nom, ema, fon)


            sistema.lista_clientes.append(nuevo) # Agrega el nuevo cliente a la lista de clientes del sistema
            sistema.guardar_datos() 
            sistema.registrar_log(f"INFO - Se crea nuevo cliente: ID {nuevo_id}, Nombre: {nom}, Tipo: {nuevo.tipo}") # Registra en el log la creación del nuevo cliente con su ID, nombre y tipo
            print("\nCliente guardado con éxito!!")

        elif opcion == "2": # Si el usuario elige la opción 2, se mostrará una lista de todos los clientes registrados en el sistema, mostrando su ID, nombre y tipo de cliente.
            for c in sistema.lista_clientes:
                print(c)

        elif opcion == "4": # Si el usuario elige la opción 4, se le solicitará ingresar el ID del cliente que desea eliminar y se procederá a eliminarlo del sistema.
            try: # Se intenta convertir el ID ingresado a un número entero, si el usuario ingresa un valor no numérico se captura la excepción y se muestra un mensaje de error.
                id_a_eliminar = int(input("Ingrese el ID del cliente que desea eliminar: "))
                
                # Ejecutamos la eliminación en gestor.py
                if sistema.eliminar_cliente(id_a_eliminar):
                    sistema.guardar_datos()  # Guardamos los cambios después de eliminar
                    print(f"\n Cliente con ID {id_a_eliminar} ha sido eliminado correctamente.")
                else:
                    print("\n¡Error! No existe ningún cliente con ese ID.")
            except ValueError:
                print("\nPor favor, ingrese un número de ID válido.")

        elif opcion == "6": # Si el usuario elige la opción 6, se guardarán los datos de los clientes en un archivo JSON y se cerrará la aplicación.
            print("\nGuardando datos y saliendo del sistema...")
            print("¡Hasta luego!")
            sistema.guardar_datos() 
            break
        else:
            print("La opción no es válida, intente nuevamente:")
            break

if __name__ == "__main__":
    main()