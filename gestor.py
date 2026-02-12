# Aqui tendremos la logica de gestion de usuarios, como agregar, eliminar, modificar, validar etc

import json
import os
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
        pass