# Aqui tendremos la logica de gestion de clientes, como agregar, eliminar, modificar, validar etc

import json
import os
from datetime import datetime # Para obtener la fecha actual
from modelos import Cliente, ClienteVIP, ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.archivo = "clientes.json"
        self.archivo_log = "log.txt" # Archivo de texto para el log
        self.lista_clientes = []
        self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo): # Si el archivo no existe, se crean algunos clientes por defecto para tener datos iniciales en el sistema.
            self.crear_clientes_por_defecto()
        else:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for d in datos:
                    if d["tipo"] == "VIP":
                        c = ClienteVIP(d["id"], d["nombre"], d["email"], d["fono"], d["descuento"])
                    elif d["tipo"] == "Corporativo":
                        c = ClienteCorporativo(d["id"], d["nombre"], d["email"], d["fono"], d["empresa"])
                    else:
                        c = Cliente(d["id"], d["nombre"], d["email"], d["fono"])
                    self.lista_clientes.append(c)
    def guardar_datos(self):
        datos_dict = [c.a_diccionario() for c in self.lista_clientes]
        with open(self.archivo, "w") as f:
            json.dump(datos_dict, f, indent=4) # indent=4 para que el JSON se vea más legible

    def generar_id(self):
        if not self.lista_clientes: return 1
        return max(c.id_cliente for c in self.lista_clientes) + 1
    
    def crear_clientes_por_defecto(self): # Crea 3 clientes por defecto si no existe el archivo JSON.
        c1 = Cliente(1, "Ana Perez", "ana@mail.com", "511223344")
        c2 = ClienteVIP(2, "Luis Soto", "luis@vip.com", "955667788", 25)
        c3 = ClienteCorporativo(3, "Marta Diaz", "marta@empresa.com", "999001122", "PythonCorp")
        
        self.lista_clientes = [c1, c2, c3]
        self.guardar_datos()

    def registrar_log(self, mensaje): # Método para registrar eventos importantes en un archivo de log con fecha y hora.
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Obtiene la fecha y hora actual en formato legible
        linea_completa = f"[{fecha_hora}] {mensaje}\n" # Formatea la línea con la fecha y el mensaje

        with open(self.archivo_log, "a", encoding="utf-8") as archivo: # 'with' para asegurar que el archivo se cierre solo al terminar
            archivo.write(linea_completa)
                

    # Método para eliminar clientes.
    def eliminar_cliente(self, id_cliente):
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.id_cliente == id_cliente:
                # Si se encuentra el ID, cliente se elimina de la lista
                nombre_eliminado = cliente.nombre
                self.lista_clientes.pop(i)
                self.registrar_log(f"INFO - Eliminacion de Cliente: ID {id_cliente}, Nombre: {nombre_eliminado}") # Para registrar el éxito
                self.guardar_datos()  # Guardamos los cambios después de eliminar

                return True # Cliente eliminado exitosamente
         
        self.registrar_log(f"WARNING - FALLO ELIMINACIÓN: No se pudo eliminar cliente con ID {id_cliente} no existe") #para registrar el fallo (Se usa warning para diferenciarlo de los logs exitosos)
        return False # ID no encontrado se encontró
    
    # Método para buscar clientes por ID
    def buscar_por_id(self, id_cliente):
        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_cliente:
                return cliente  # Retorna el cliente si lo encuentra
        return None  # Retorna None si no encuentra el cliente
    
    # Método para buscar clientes por nombre
    def buscar_por_nombre(self, nombre):
        resultados = []
        nombre_buscado = nombre.lower() # Se convierte la búsqueda a minúsculas
        
        for cliente in self.lista_clientes: # Para verificar si lo que el usuario escribió está contenido en el nombre del cliente
            if nombre_buscado in cliente.nombre.lower(): # .lower() para que ignore mayúsculas y minúsculas, ya que convierte el nombre del cliente a minúsculas
                resultados.append(cliente) # append para agregar el cliente a la lista de resultados si coincide con la búsqueda (si el nombre buscado está contenido en el nombre del cliente, se agrega a la lista de resultados)
                
        return resultados # Retorna una lista (puede estar vacía o tener varios clientes)

    pass # Método para buscar clientes por email
    
    # Método para editar cliente
    def editar_cliente(self, id_cliente, campo, nuevo_valor): 
        cliente = self.buscar_por_id(id_cliente) 
        
        if not cliente: # Primero buscamos el cliente por su ID para asegurarnos de que existe antes de intentar editarlo. Si no se encuentra, retornamos False para indicar que la edición no fue posible.
            return False  # Cliente no encontrado
        
        valor_anterior = None # Guardamos el valor anterior para el log
        
        if campo == "nombre":
            valor_anterior = cliente.nombre
            cliente.nombre = nuevo_valor

        elif campo == "email":
            if not self.validar_email(nuevo_valor): # Se usa 'not' para negar la validación, si el nuevo valor no es un fono válido, se retorna False para indicar que la edición no fue posible.
                return False  # Email inválido
            
            valor_anterior = cliente.email
            cliente.email = nuevo_valor

        elif campo == "fono":
            if not self.validar_fono(nuevo_valor): 
                return False  # Fono inválido
            
            valor_anterior = cliente.fono
            cliente.fono = nuevo_valor

        elif campo == "descuento": # Solo para ClienteVIP y ClienteCorporativo
            if hasattr(cliente, 'descuento'): #hasattr verifica si el cliente tiene el atributo 'descuento', lo que indica que es un ClienteVIP o ClienteCorporativo. Si el cliente no tiene este atributo, se retorna False para indicar que no se puede editar el descuento.
                valor_anterior = cliente.descuento
                cliente.descuento = int(nuevo_valor)
            else:
                return False  # El cliente no tiene descuento
            
        elif campo == "empresa": # Solo para ClienteCorporativo
            if hasattr(cliente, 'empresa'):
                if not self.validar_empresa(nuevo_valor): # Si el nuevo valor no es una empresa válida, se retorna False para indicar que la edición no fue posible.
                    return False # Empresa inválida

                valor_anterior = cliente.empresa
                cliente.empresa = nuevo_valor

                if cliente.empresa.lower() == "pythoncorp": # Actualizar descuento ueva empresa es PythonCorp, se le asigna un descuento del 50%, de lo contrario, se le asigna un descuento del 10%.
                    cliente.descuento = 50
                else:
                    cliente.descuento = 10
            else:
                return False  # El cliente no tiene empresa
        else:
            return False  # Campo no válido
        
        self.registrar_log(f"INFO - Edición de Cliente ID {id_cliente}: Campo '{campo}' cambiado de '{valor_anterior}' a '{nuevo_valor}'") # Para registrar la edición en el log
        self.guardar_datos()  # Guardar cambios
        return True


    @staticmethod # Método estático para validar formato de email.
    def validar_email(email):
        # Valida que contenga '@' y al menos un '.' después de la arroba
        if "@" in email:
            partes = email.split("@") # Divide el email en dos partes: antes y después de la arroba
            if "." in partes[1]: # Verifica que haya un punto en la parte del dominio (después de la arroba)
                return True
        return False
    
    @staticmethod # Método estático para validar formato de teléfono, asegurando que tenga exactamente 11 dígitos y solo números.
    def validar_fono(fono):
        return fono.isdigit() and len(fono) == 9 # Verifica que el fono tenga exactamente 11 caracteres y todos sean números

    @staticmethod
    def validar_empresa(empresa): # Valida que el nombre de la empresa no esté vacío ni compuesto solo de espacios
        return len(empresa.strip()) > 0 # El método .strip() elimina los espacios al principio y al final, si después de limpiarlo queda algún caracter, es válido (True)
    
