import sqlite3

# Crear tabla
def crearTablaProductos():
    # Conexion a la base de datos
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    # Creacion de tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Descripcion TEXT,
            Cantidad INTEGER NOT NULL,
            Precio REAL NOT NULL,
            Categoria TEXT
        )
    """)

    # Guardar y cerrar
    conexion.commit()
    conexion.close()

# Agregar registro
def registrarProducto():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre: ")
    descripcion = input("Ingrese descripcion: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    categoria = input("Ingresa la categoría: ")

    # Insertar registro
    cursor.execute("INSERT INTO inventario (Nombre,Descripcion,Cantidad,Precio,Categoria) VALUES (?,?,?,?,?)",(nombre,descripcion,cantidad,precio,categoria))

    conexion.commit()
    conexion.close()

# Obtener registros
def obtenerRegistros():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM inventario")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("No hay nada cargado, aún")
    else:
        for producto in resultados:
            print("ID:",producto[0],"Nombre: ",producto[1],"Descripcion: ",producto[2],"Cantidad: ",producto[3],"Precio: ",producto[4],"Categoría: ",producto[5])
    #for producto in resultados:
        #print("ID:",producto[0],"Nombre: ",producto[1],"Descripcion: ",producto[2],"Cantidad: ",producto[3],"Precio: ",producto[4],"Categoría: ",producto[5])

    conexion.commit()
    conexion.close()

# Actualizar producto
def actualizarProducto():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    id = input("Ingrese el ID del Producto: ")
    nuevaCantidad = int(input("Ingrese la nueva Cantidad: "))
    cursor.execute("UPDATE inventario SET cantidad = ? WHERE id = ?",(nuevaCantidad,id))

    conexion.commit()
    conexion.close()

# Eliminar registro
def eliminarProducto():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    id = int(input("Ingrese el ID del producto: "))
    cursor.execute("DELETE FROM inventario WHERE id = ?",(id,))

    conexion.commit()
    conexion.close()

# Buscar Registro
def buscarRegistro():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    id = int(input("Ingrese el ID a buscar: "))
    cursor.execute("SELECT * FROM inventario WHERE id = ?",(id,))
    resultado = cursor.fetchone()

    if resultado == None:
        print("El id no existe, intente de nuevo")
    else:
        print("ID: ",resultado[0],"Nombre: ",resultado[1],"Descripcion: ",resultado[2],"Cantidad: ",resultado[3],"Precio: ",resultado[4],"Categoría: ",resultado[5])

    conexion.commit()
    conexion.close()

# Reporte bajo stock
def reporteBajoStock():
    conexion = sqlite3.connect("baseDatos.db")
    cursor = conexion.cursor()

    cantidad = int(input("Ingrese limite de Stock a reportar: "))
    cursor.execute("SELECT * FROM inventario WHERE cantidad <= ?",(cantidad,))
    resultados =  cursor.fetchall()

    for producto in resultados:
        print("ID:",producto[0],"Nombre: ",producto[1],"Descripcion: ",producto[2],"Cantidad: ",producto[3],"Precio: ",producto[4],"Categoría: ",producto[5])

    conexion.commit()
    conexion.close()

# Menu Principal
def menu():
    print("------------------------")
    print(">>>>>Menu Principal<<<<<")
    print("---------------------")
    print("1. Registrar Producto")
    print("2. Obtener Registros")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Buscar Producto")
    print("6. Reporte Bajo Stock")
    print("7. Salir del Programa")
    print("------------------------")

def miniMenu():
    print("---------------")
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Cantidad")
    print("4. Precio")
    print("5. Categoría")
    print("---------------")

while True:
    crearTablaProductos()
    menu()

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        registrarProducto()
    elif opcion == 2:
        obtenerRegistros()
    elif opcion == 3:
        actualizarProducto()
    elif opcion == 4:
        eliminarProducto()
    elif opcion == 5:
        buscarRegistro()
    elif opcion == 6:
        reporteBajoStock()
    elif opcion == 7:
        print("Saliendo del programa, gracias")
        break
    else:
        print("Ingrese una opción válida")

