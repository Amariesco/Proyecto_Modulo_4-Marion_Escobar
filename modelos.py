# Tendra clases y funciones para gestionar los tipos de clientes y sus atributos

""" Tipos de Usuarios (datos/atributos):
    1. Cliente (Nombre, Email, Fono) *No tendra descuentos
    2. Cliente VIP (Nombre, Email, Fono) *Tendra descuento estandar en compras.
    3. Cliente Corporativo (Nombre, Email, Fono, Empresa) *Tendra otro tipo de descuentos dependiendo de la empresa."""

class Cliente: # Cliente regular sin descuentos
    def __init__(self, id_cliente, nombre, email, fono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.fono = fono
        self.tipo = "Regular"

    def __str__(self):
        return f"[ID: {self.id_cliente}] {self.nombre} ({self.tipo})"

    def a_diccionario(self):
        return {
            "id": self.id_cliente, "nombre": self.nombre,
            "email": self.email, "fono": self.fono, "tipo": self.tipo
        }

class ClienteVIP(Cliente): # Cliente VIP tiene un descuento fijo del 20% en todas las compras
    def __init__(self, id_cliente, nombre, email, fono, descuento): # El descuento se puede configurar al crear el cliente VIP
        super().__init__(id_cliente, nombre, email, fono)
        self.descuento = descuento
        self.tipo = "VIP"

    def __str__(self):
        return f"[ID: {self.id_cliente}] {self.nombre} (VIP - {self.descuento}% desc)"

    def a_diccionario(self):
        d = super().a_diccionario()
        d["descuento"] = self.descuento
        return d

class ClienteCorporativo(Cliente): #Cliente Corporativo si es de empresa PythonCorp tiene 50% de descuento, otras empresas 10%
    def __init__(self, id_cliente, nombre, email, fono, empresa):
        super().__init__(id_cliente, nombre, email, fono) 
        self.empresa = empresa
        self.tipo = "Corporativo"
        # Lógica de descuento según empresa
        if self.empresa.lower() == "pythoncorp":
            self.descuento = 50
        else:
            self.descuento = 10

    def __str__(self): 
        return f"[ID: {self.id_cliente}] {self.nombre} (Empresa: {self.empresa} - Desc: {self.descuento}%)"

    def a_diccionario(self): # Sobrescribimos el método para incluir empresa y descuento
        d = super().a_diccionario()
        d["empresa"] = self.empresa
        d["descuento"] = self.descuento
        return d