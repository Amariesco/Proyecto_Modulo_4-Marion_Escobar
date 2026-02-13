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
            json.dump(datos_dict, f, indent=4)

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
    
    pass  # Método para buscar clientes por nombre

    pass # Método para buscar clientes por email
    
    @staticmethod # Método estático para validar formato de email usando regex para una validación más robusta.
    def validar_email(email):
        # Valida que contenga '@' y al menos un '.' después de la arroba
        if "@" in email:
            partes = email.split("@")
            if "." in partes[1]:
                return True
        return False
    
    @staticmethod # Método estático para validar formato de teléfono, asegurando que tenga exactamente 11 dígitos y solo números.
    def validar_fono(fono):
        # Verifica que el fono tenga exactamente 11 caracteres y todos sean números
        return fono.isdigit() and len(fono) == 9
    
