def quick_sort_iterativo(arr):
    
    stack = [(0, len(arr) - 1)]
    
    while stack:
        inicio, fin = stack.pop()
        if inicio < fin:
            pivote_index = particion(arr, inicio, fin)
            stack.append((inicio, pivote_index - 1))
            stack.append((pivote_index + 1, fin))

def particion(arr, inicio, fin):
    pivote = arr[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1


arr = [46, 5, 4, 12, 1,9, 7, 17, 6]
quick_sort_iterativo(arr)
print("Arreglo ordenado:", arr)
