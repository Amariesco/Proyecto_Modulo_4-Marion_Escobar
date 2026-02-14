# Tendremos aqui documentacion base, explicacion del programa y procesos en su construccion.
*******************************
 SISTEMA DE GESTION DE CLIENTES
*******************************
Sistema completo para la administración de clientes con diferentes tipos de membresía, desarrollado en Python con programación orientada a objetos.

*******************************
 DESCRIPCIÓN
*******************************
Sistema de gestión que permite crear, editar, eliminar y buscar clientes de tres tipos diferentes: Regulares, VIP y Corporativos. 
Incluye validación de datos, persistencia en archivos JSON y sistema de registro de actividades (logs).

*******************************
 TECNOLOGÍAS UTILIZADAS
*******************************
Lenguaje: Python 3.x
Almacenamiento: JSON (persistencia de datos)
Arquitectura: Programación Orientada a Objetos (POO)
Diagrama: UML (Draw.io)

*******************************
 ARCHIVOS
*******************************
main.py -----------> Menú principal e interfaz de usuario
gestor.py ---------> Logica de gestion de clientes, como agregar, eliminar, modificar, validar etc
modelos.py --------> Clases de clientes (Regular, VIP, Corporativo)
UML.drawio --------> UML / Diagrama de clases
README.md ---------> Información sobre el Código

clientes.json -----> Base de datos (se genera automáticamente)
log.txt -----------> Registro de actividades (se genera automáticamente)

*******************************
 ESTADO DEL PROYECTO
*******************************
Funcionalidades Completadas:
 - Sistema CRUD completo (Crear, Leer, Actualizar, Eliminar)
 - Validación de datos (email, teléfono, empresa, descuento)
 - Tres tipos de clientes con herencia
 - Persistencia en JSON
 - Sistema de logs
 - Búsqueda por ID y Nombre
 - Edición completa de clientes

Funcionalidades Pendientes:
 - Búsqueda por email
 - Campo dirección con validación
 - Mejoras visuales en los menús
 - Implementar confirmacion antes de eliminar

*******************************
 INFORMACION RELEVANTE MIENTRAS SE PROGRAMA:
 (Para saber que funciona del código y que se plantea para agregar a futuro)
*******************************
Simbologia: 

``[Pendiente]``= Por hacer / agregar código
🟢 = Listo y funcionando

_________________________________________________

------ Menu Principal planteado (y sus respectivas funciones) ----------------

1. Crear Clinte: (Se registra en log creacion de nuevo cliente)
    🟢Nombre: 
    🟢Email: (vadidar uso de @ y . despues del @) 
    🟢Fono: (validar cantidad de numeros 11 y que sea numerico) 
    ``Dirección: (Que sea texto + numeracion)`` [pendiente]
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
    🟢Por Nombre:
    ``Por Email:`` [pendiente]

6. 🟢Guardar y Salir
 - Guardado automático en clientes.json
 - Cierre seguro de la aplicación

``* Revisar menus y dejarlos agradables visualmente`` [pendiente]
``* Implementar confirmacion antes de eliminar para evitar errores`` [pendiente]
______________________________________________________________

Tipos de Usuarios (datos/atributos):
    1. Cliente (Nombre, Email, Fono) *No tendra descuentos
    2. Cliente VIP (Nombre, Email, Fono) *Al ingresar cliente vip, se selecciona cantidad de descuento. 
    3. Cliente Corporativo (Nombre, Email, Fono, Empresa) *Tendra otro tipo de descuentos dependiendo de la empresa. (PythonCorp tiene 50% de descuento, otras empresas 10%)
______________________________________________________________

