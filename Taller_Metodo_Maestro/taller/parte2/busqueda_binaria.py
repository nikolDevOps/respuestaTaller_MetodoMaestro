def busqueda_binaria_recursiva(arr, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1  
    
    mid = (izquierda + derecha) // 2
    
    if arr[mid] == objetivo:
        return mid
    elif arr[mid] > objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, mid - 1)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, mid + 1, derecha)

# Ejemplo de uso
arr = [3, 8, 15, 20, 25, 30, 35]
objetivo = 8
resultado = busqueda_binaria_recursiva(arr, objetivo, 0, len(arr) - 1)

if resultado != -1:
    print(f"Elemento {objetivo} encontrado en la posición {resultado}")
else:
    print("Elemento no encontrado")
