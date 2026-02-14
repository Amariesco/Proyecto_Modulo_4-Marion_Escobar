# Tendremos aqui documentacion base, explicacion del programa y procesos en su construccion.

*******************************
Archivos:
main.py -----------> Menú principal, codigo base para el proyecto, como la inicializacion de la aplicacion, configuraciones, etc
gestor.py ---------> Logica de gestion de usuarios, como agregar, eliminar, modificar, validar etc
modelos.py --------> Clases y funciones para gestionar los tipos de clientes y sus atributos
UML.drawio ----> UML / Diagrama de clases

*******************************

Simbologia: 

``[Incompleto]``= Por hacer / agregar código
🟢 = Listo y funcionando

*******************************

------ Menu Principal planteado (y sus respectivas funciones) ----------------

1. Crear Clinte: (Se registra en log creacion de nuevo cliente)
    🟢Nombre: 
    🟢Email: (vadidar uso de @ y . despues del @) 
    🟢Fono: (validar cantidad de numeros 11 y que sea numerico) 
    ``Direccion: (Que sea texto + numeracion)`` [pendiente]
    🟢Tipo de Cliente: 1. Regular | 2. VIP | 3. Corporativo (Si selecciona otro numero se asignara automaticamente como Regular)
        -Si es VIP se debe ingresar el descuento de forma manual (se valida que el numero sea entre 0 a 100)
        -Si es Corporativo se debe ingresar la empresa, se valida si se ingresa texto en el campo empresa.


2. Lista de Clientes: (Solo se muestra ID, Nombre, Tipo de cliente y Descuento)

3. Editar Cliente:
    🟢(seleccionar que dato editar, se valida el tipo de cliente para editar descuento o empresa)

4. Eliminar Cliente: (Se registra en log la eliminacion de nuevo cliente y el error al eliminar)
    🟢Elimina mediante ID único.
    - Al eliminar, el sistema guarda cambios automáticamente en el archivo 'clientes.json'.
    - Incluye manejo de errores si el ID no existe o si se ingresan letras.

5. Buscar Cliente: (Al buscar cliente se muestran todos los datos ingresados)
    🟢Por ID:
    ``Por Nombre:`` [pendiente]
    ``Por Email:`` [pendiente]

6. 🟢Guardar y Salir


****************************

Tipos de Usuarios (datos/atributos):
    1. Cliente (Nombre, Email, Fono) *No tendra descuentos
    2. Cliente VIP (Nombre, Email, Fono) *Al ingresar cliente vip, se selecciona cantidad de descuento. 
    3. Cliente Corporativo (Nombre, Email, Fono, Empresa) *Tendra otro tipo de descuentos dependiendo de la empresa.

**************************

