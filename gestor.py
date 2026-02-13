# Aqui tendremos la logica de gestion de clientes, como agregar, eliminar, modificar, validar etc

import json
import os
import re  # Importamos para validaciones complejas
from modelos import Cliente, ClienteVIP, ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.archivo = "clientes.json"
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
    
    def crear_clientes_por_defecto(self):
        """Si al ingrsar a lista y no hay datos se crean 3 clientes iniciales y los guarda."""
        c1 = Cliente(1, "Ana Perez", "ana@mail.com", "11223344")
        c2 = ClienteVIP(2, "Luis Soto", "luis@vip.com", "55667788", 25)
        c3 = ClienteCorporativo(3, "Marta Diaz", "marta@empresa.com", "99001122", "PythonCorp")
        
        self.lista_clientes = [c1, c2, c3]
        self.guardar_datos()

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
        return fono.isdigit() and len(fono) == 11
    
    #Se agrega método eliminar clientes.
    def eliminar_cliente(self, id_cliente):
        """Busca un cliente por ID y lo elimina de la lista interna."""
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.id_cliente == id_cliente:
                # Si se encuentra el ID, se elimina de la lista
                self.lista_clientes.pop(i)
                self.guardar_datos()  # Guardamos los cambios después de eliminar
                return True # Éxito
        return False # ID no encontrado se encontró