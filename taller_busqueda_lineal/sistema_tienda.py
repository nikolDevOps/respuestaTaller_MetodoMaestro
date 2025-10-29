


# IMPORTACIÓN DE MÓDULOS

from datos_ejemplo import productos, empleados  # Datos de prueba
from funciones_busqueda import *                 # Funciones de búsqueda lineal



# FUNCIONES DE VISUALIZACIÓN


def mostrar_producto(p):
    """
    Muestra la información completa de un producto en formato legible.

    Args:
        p (dict or None): Diccionario del producto o None si no existe.

    Returns:
        None: Imprime directamente en consola.
    """
    if not p:
        print("Producto no encontrado.")
        return
    
    # Formateo de disponibilidad
    disp = "Sí" if p.get('disponible', False) else "No"
    
    print(f"ID: {p['id']} | {p['nombre']} ({p['marca']}) | "
          f"${p['precio']:.2f} | Stock: {p['stock']} | Disponible: {disp}")


def mostrar_lista_productos(lista):
    """
    Muestra todos los productos de una lista, uno por línea.

    Args:
        lista (list): Lista de diccionarios de productos.

    Returns:
        None: Usa mostrar_producto() internamente.
    """
    if not lista:
        print("No se encontraron productos.")
    else:
        for p in lista:
            mostrar_producto(p)


def mostrar_empleado(e):
    """
    Muestra la información de un empleado.

    Args:
        e (dict or None): Diccionario del empleado o None.

    Returns:
        None
    """
    if not e:
        print("Empleado no encontrado.")
        return
    
    activo = "Sí" if e.get('activo', False) else "No"
    
    print(f"ID: {e['id']} | {e['nombre']} {e['apellido']} | "
          f"{e['departamento']} | ${e['salario']:,} | Activo: {activo}")


def mostrar_lista_empleados(lista):
    """
    Muestra una lista de empleados.

    Args:
        lista (list): Lista de empleados.

    Returns:
        None
    """
    if not lista:
        print("No se encontraron empleados.")
    else:
        for e in lista:
            mostrar_empleado(e)



# MENÚS DE BÚSQUEDA


def menu_productos():
    """
    Menú interactivo para búsqueda de productos.
    Incluye todas las opciones del taller: por nombre, ID, categoría, etc.

    Returns:
        None: Bucle infinito hasta que el usuario elija "Volver".
    """
    while True:
        print("BÚSQUEDA DE PRODUCTOS")
        print("1. Por nombre")
        print("2. Por ID")
        print("3. Por categoría")
        print("4. Disponibles (stock > 0)")
        print("5. Por rango de precios")
        print("6. Por marca")
        print("7. Contar por categoría")
        print("8. Volver al menú principal")

        
        op = input("Seleccione una opción (1-8): ").strip()

        #  OPCIÓN 1: Búsqueda por nombre 
        if op == '1':
            nombre = input("Nombre del producto: ").strip()
            resultado = buscar_producto_por_nombre(productos, nombre)
            mostrar_producto(resultado)

        # OPCIÓN 2: Búsqueda por ID 
        elif op == '2':
            entrada = input("ID del producto: ").strip()
            try:
                id_b = int(entrada)
                resultado = buscar_producto_por_id(productos, id_b)
                mostrar_producto(resultado)
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        # OPCIÓN 3: Búsqueda por categoría 
        elif op == '3':
            cat = input("Categoría: ").strip()
            resultados = buscar_productos_por_categoria(productos, cat)
            mostrar_lista_productos(resultados)

        #  OPCIÓN 4: Productos disponibles 
        elif op == '4':
            resultados = buscar_productos_disponibles(productos)
            print(f"\nProductos disponibles ({len(resultados)}):")
            mostrar_lista_productos(resultados)

        #  OPCIÓN 5: Rango de precios 
        elif op == '5':
            try:
                min_p = float(input("Precio mínimo: "))
                max_p = float(input("Precio máximo: "))
                if min_p > max_p:
                    print("Error: El precio mínimo no puede ser mayor que el máximo.")
                    continue
                resultados = buscar_productos_por_rango_precio(productos, min_p, max_p)
                mostrar_lista_productos(resultados)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        #  OPCIÓN 6: Por marca 
        elif op == '6':
            marca = input("Marca: ").strip()
            resultados = buscar_productos_por_marca(productos, marca)
            mostrar_lista_productos(resultados)

        #  OPCIÓN 7: Contar por categoría 
        elif op == '7':
            cat = input("Categoría a contar: ").strip()
            total = contar_productos_por_categoria(productos, cat)
            print(f"→ Hay {total} producto(s) en la categoría '{cat.title()}'.")

        #  OPCIÓN 8: Volver 
        elif op == '8':
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Por favor, elija entre 1 y 8.")


def menu_empleados():
    """
    Menú interactivo para búsqueda de empleados.

    Returns:
        None
    """
    while True:
        print("BÚSQUEDA DE EMPLEADOS")
        print("1. Por nombre completo")
        print("2. Por departamento")
        print("3. Empleados activos")
        print("4. Volver")
        
        op = input("Seleccione una opción (1-4): ").strip()

        #  OPCIÓN 1: Nombre completo 
        if op == '1':
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            if nombre and apellido:
                resultado = buscar_empleado_por_nombre_completo(empleados, nombre, apellido)
                mostrar_empleado(resultado)
            else:
                print("Debe ingresar tanto nombre como apellido.")

        # OPCIÓN 2: Por departamento 
        elif op == '2':
            depto = input("Departamento: ").strip()
            resultados = buscar_empleados_por_departamento(empleados, depto)
            mostrar_lista_empleados(resultados)

        #  OPCIÓN 3: Activos 
        elif op == '3':
            resultados = buscar_empleados_activos(empleados)
            print(f"\nEmpleados activos ({len(resultados)}):")
            mostrar_lista_empleados(resultados)

        #  OPCIÓN 4: Volver 
        elif op == '4':
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Elija entre 1 y 4.")



# MENÚ PRINCIPAL Y EJECUCIÓN


def main():
    """
    Función principal que inicia el sistema TechStore.
    """

    print("BIENVENIDO AL SISTEMA DE GESTIÓN TECHSTORE")


    while True:
        print(" MENÚ PRINCIPAL ")
        print("1. Gestión de Productos")
        print("2. Gestión de Empleados")
        print("3. Salir del sistema")
        
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == '1':
            menu_productos()
        elif opcion == '2':
            menu_empleados()
        elif opcion == '3':
            print("\nGracias por usar TechStore. ")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


# PUNTO DE ENTRADA


if __name__ == "__main__":
    main()