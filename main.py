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
        print("3. Editar Cliente")
        print("4. Eliminar Cliente")
        print("5. Buscar Cliente")
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
                fon = input("\nFono (ingresar 9 dígitos numéricos, ej: 912345678): ")
                if sistema.validar_fono(fon):
                    break
                print("Error: Verifique el fono, este debe tener exactamente 9 números (sin espacios ni signos).")
            
            print("\nTipos de clientes: 1. Regular | 2. VIP | 3. Corporativo \n *(Si selecciona otro numero se asignara automaticamente como Regular)*\n") 
            tipo = input("\nIngrese una opcion: ")
            nuevo_id = sistema.generar_id()

            if tipo == "2": # Si el usuario selecciona VIP, se le solicitará ingresar el porcentaje de descuento y se creará un cliente VIP con ese descuento.
                while True: # Bucle para validar el descuento
                    try:
                        desc = int(input("% Descuento (0-100): "))
                        if 0 <= desc <= 100:
                            nuevo = ClienteVIP(nuevo_id, nom, ema, fon, desc)
                            break # Sale del bucle cuando el descuento es válido
                        else:
                            print("Error: El descuento debe estar entre 0 y 100.")
                    except ValueError:
                        print("Error: Debe ingresar un número válido.")  

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

        elif opcion == "3": # Si el usuario elige la opción 3, podrá editar los datos de un cliente existente
            try:
                id_editar = int(input("\nIngrese el ID del cliente que desea editar: "))
                cliente = sistema.buscar_por_id(id_editar)
                
                if not cliente:
                    print(f"\n¡Error! No existe ningún cliente con ID {id_editar}")
                else:
                    # Mostrar datos actuales del cliente
                    print("\nDatos actuales del cliente: ")
                    print(f"\nID: {cliente.id_cliente}")
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Email: {cliente.email}")
                    print(f"Fono: {cliente.fono}")
                    print(f"Tipo: {cliente.tipo}")
                    
                    if hasattr(cliente, 'descuento'): # Se usa hasattr para comprobar si un objeto tiene un atributo o método específico antes de intentar acceder a él, devolviendo True si existe y False si no
                        print(f"Descuento: {cliente.descuento}%")
                    if hasattr(cliente, 'empresa'):
                        print(f"Empresa: {cliente.empresa}")

                    print(f"\n***¿Que información de {cliente.nombre} desea editar?***") # Menu para seleccionar qué campo del cliente se desea editar, mostrando solo las opciones relevantes según el tipo de cliente (Regular, VIP o Corporativo).
                    print("1. Nombre")
                    print("2. Email")
                    print("3. Fono")
                    # If sencillos para mostrar opciones adicionales según el tipo de cliente
                    if hasattr(cliente, 'descuento'): 
                        print("4. Descuento")
                    if hasattr(cliente, 'empresa'):
                        print("5. Empresa")
                    
                    opcion_editar = input("\nIngrese una opción: ")                  
                        
                    if opcion_editar == "1": # Editar Nombre
                        nuevo_nombre = input("\nIngrese el nuevo nombre: ")
                        if sistema.editar_cliente(id_editar, "nombre", nuevo_nombre): # Llama al método editar_cliente del sistema para actualizar el nombre del cliente con el nuevo valor ingresado por el usuario.
                            print(f"\nNombre de cliente con ID {id_editar} se ha actualizado con éxito")
                        else:
                            print("\n¡Error al actualizar el nombre!")
                    
                    elif opcion_editar == "2": #Editar Email y comprobar que nuevo email sea valido.
                        while True:
                            nuevo_email = input("\nIngrese el nuevo email: ")
                            if sistema.validar_email(nuevo_email):
                                if sistema.editar_cliente(id_editar, "email", nuevo_email):
                                    print(f"\nEmail de cliente con ID {id_editar} se ha actualizado con éxito")
                                    break
                                else:
                                    print("\n¡Error al actualizar el email!")
                                    break
                            else:
                                print("Error: Verifique el email, este debe contener '@' y un '.' después de la arroba.")

                    elif opcion_editar == "3": #Editar Fono y comprobar que nuevo fono sea valido.
                        while True: # Ciclo while para validar ingreso de Fono.
                            nuevo_fono = input("\nIngrese el nuevo fono (9 dígitos): ")
                            if sistema.validar_fono(nuevo_fono):
                                if sistema.editar_cliente(id_editar, "fono", nuevo_fono):
                                    print(f"\nFono de cliente con ID {id_editar} se ha actualizado con éxito")
                                    break
                                else:
                                    print(f"\n¡Error al actualizar el fono del cliente con ID {id_editar}!")
                                    break
                            else:
                                print("Error: El fono debe tener exactamente 9 números.")

                    elif opcion_editar == "4" and hasattr(cliente, 'descuento'):
                        try:
                            nuevo_descuento = int(input("\nIngrese el nuevo porcentaje de descuento: "))
                            if 0 <= nuevo_descuento <= 100:
                                if sistema.editar_cliente(id_editar, "descuento", nuevo_descuento):
                                    print(f"\n¡El porcentaje de descuento del cliente con ID {id_editar} se ha actualizado con éxito!")
                                else:
                                    print("\n¡Error al actualizar el descuento!")
                            else:
                                print("\n¡Error! El descuento debe estar entre 0 y 100%")
                        except ValueError:
                            print("\n¡Error! Debe ingresar un número válido")
                    
                    elif opcion_editar == "5" and hasattr(cliente, 'empresa'):
                        nueva_empresa = input("\nIngrese el nuevo nombre de la empresa: ")
                        if sistema.editar_cliente(id_editar, "empresa", nueva_empresa):
                            print("\n¡Empresa actualizada con éxito!")
                            print(f"Nuevo descuento: {cliente.descuento}%")
                        else:
                            print("\n¡Error al actualizar la empresa!")

                    else:
                        print("\nLa opcion ingresada no es válida.")

                    sistema.guardar_datos() # Guardamos los cambios realizados al cliente editado
                    sistema.registrar_log(f"INFO - Se edita cliente con ID {cliente.id_cliente}") # Registra en el log la edición del cliente con su ID

            except ValueError:
                print("\nPor favor, ingrese un número de ID válido.")

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

        elif opcion == "5": # Si el usuario elige la opción 5, podrá buscar clientes por ID, Nombre o Email
            print("\n Buscar cliente por ID ")
            # ----> por completar en futuras actualizaciones para agregar búsqueda por nombre y email
            #print("1. Buscar por ID") 
            #print("2. Buscar por Nombre")
            #print("3. Buscar por Email")
            
            #tipo_busqueda = input("\nSeleccione tipo de búsqueda: ")
            
            #if tipo_busqueda == "1": # Buscara Cliente registrado por ID
            try:
                id_buscar = int(input("Ingrese el ID del cliente: "))
                resultado = sistema.buscar_por_id(id_buscar)
                    
                if resultado:
                    print(f"\nCliente con ID {id_buscar} a sido encontrado")
                        
                    print(f"\nNombre: {resultado.nombre}")
                    print(f"Email: {resultado.email}")
                    print(f"Fono: {resultado.fono}")
                    print(f"Tipo de cliente: {resultado.tipo}")
                        
                    # Mostrar descuento si es VIP o Corporativo
                    if hasattr(resultado, 'descuento'):
                        print(f"Descuento: {resultado.descuento}%")
                    # Mostrar empresa si es Corporativo
                    if hasattr(resultado, 'empresa'):
                        print(f"Empresa: {resultado.empresa}")
                else:
                    print(f"\nNo se encontró ningún cliente con ID {id_buscar}")
                        
            except ValueError:
                print("\nError: Debe ingresar un número válido de ID")

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