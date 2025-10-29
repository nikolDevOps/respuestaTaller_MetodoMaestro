
# BÚSQUEDA LINEAL BÁSICA
def busqueda_lineal_simple(lista, elemento):
    """
    Realiza una búsqueda lineal (secuencial) en una lista de elementos.

    Recorre la lista índice por índice hasta encontrar el elemento buscado
    o llegar al final.

    Args:
        lista (list): Lista de elementos a buscar (puede ser de cualquier tipo).
        elemento (any): Valor a buscar en la lista.

    Returns:
        int: Índice del elemento si se encuentra, o -1 si no está presente.

    Ejemplo:
        >>> busqueda_lineal_simple([10, 20, 30], 20)
        1
        >>> busqueda_lineal_simple([1, 2, 3], 5)
        -1
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Elemento encontrado
    return -1  # No encontrado

# BÚSQUEDA EN PRODUCTOS
def buscar_producto_por_nombre(productos, nombre):
    """
    Busca un producto por su nombre exacto (insensible a mayúsculas).

    Args:
        productos (list): Lista de diccionarios con información de productos.
        nombre (str): Nombre del producto a buscar.

    Returns:
        dict or None: Diccionario del producto si se encuentra, None si no.

    Nota:
        La comparación es case-insensitive (ej. "iPhone" == "IPHONE").
    """
    for p in productos:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None


def buscar_producto_por_id(productos, id_buscado):
    """
    Busca un producto por su ID único.

    Args:
        productos (list): Lista de productos.
        id_buscado (int): ID del producto a localizar.

    Returns:
        dict or None: Producto encontrado o None.
    """
    for p in productos:
        if p['id'] == id_buscado:
            return p
    return None


def buscar_productos_por_categoria(productos, categoria):
    """
    Retorna todos los productos que pertenecen a una categoría específica.

    Args:
        productos (list): Lista de productos.
        categoria (str): Nombre de la categoría (ej. "Smartphone").

    Returns:
        list: Lista de productos que coinciden con la categoría.
              Lista vacía si no hay coincidencias.
    """
    return [p for p in productos if p['categoria'].lower() == categoria.lower()]


def buscar_productos_disponibles(productos):
    """
    Filtra productos con stock mayor a cero (disponibles para venta).

    Args:
        productos (list): Lista de productos.

    Returns:
        list: Productos con stock > 0.
    """
    return [p for p in productos if p['stock'] > 0]


def buscar_productos_por_rango_precio(productos, min_p, max_p):
    """
    Busca productos cuyo precio esté dentro de un rango dado.

    Args:
        productos (list): Lista de productos.
        min_p (float): Precio mínimo (incluyente).
        max_p (float): Precio máximo (incluyente).

    Returns:
        list: Productos en el rango de precios.
    """
    return [p for p in productos if min_p <= p['precio'] <= max_p]


def buscar_productos_por_marca(productos, marca):
    """
    Encuentra todos los productos de una marca específica.

    Args:
        productos (list): Lista de productos.
        marca (str): Nombre de la marca (ej. "Apple").

    Returns:
        list: Productos de la marca indicada.
    """
    return [p for p in productos if p['marca'].lower() == marca.lower()]


def contar_productos_por_categoria(productos, categoria):
    """
    Cuenta cuántos productos hay en una categoría dada.

    Args:
        productos (list): Lista de productos.
        categoria (str): Categoría a contar.

    Returns:
        int: Número de productos en esa categoría.
    """
    return sum(1 for p in productos if p['categoria'].lower() == categoria.lower())

# BÚSQUEDA EN EMPLEADOS
def buscar_empleado_por_nombre_completo(empleados, nombre, apellido):
    """
    Busca un empleado por su nombre y apellido completo.

    Args:
        empleados (list): Lista de diccionarios de empleados.
        nombre (str): Nombre del empleado.
        apellido (str): Apellido del empleado.

    Returns:
        dict or None: Empleado encontrado o None.
    """
    for e in empleados:
        if (e['nombre'].lower() == nombre.lower() and 
            e['apellido'].lower() == apellido.lower()):
            return e
    return None


def buscar_empleados_por_departamento(empleados, departamento):
    """
    Retorna todos los empleados de un departamento específico.

    Args:
        empleados (list): Lista de empleados.
        departamento (str): Nombre del departamento.

    Returns:
        list: Lista de empleados en ese departamento.
    """
    return [e for e in empleados if e['departamento'].lower() == departamento.lower()]


def buscar_empleados_activos(empleados):
    """
    Filtra empleados que están actualmente activos en la empresa.

    Args:
        empleados (list): Lista de empleados.

    Returns:
        list: Empleados con 'activo' == True.
    """

    return [e for e in empleados if e['activo']]
