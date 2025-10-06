def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr =  [
    12, 45, 7, 89, 34, 23, 56, 78, 90, 11,
    3, 67, 54, 29, 81, 15, 62, 40, 95, 8,
    25, 13, 50, 72, 36, 91, 18, 6, 88, 30,
    14, 77, 42, 27, 60, 9, 20, 85, 33, 5,
    100, 73, 2, 38, 44, 21, 97, 70, 17, 4,
    35, 64, 10, 28, 83, 41, 53, 16, 75, 19,
    31, 68, 22, 84, 46, 32, 99, 24, 57, 1,
    26, 80, 39, 61, 52, 48, 37, 71, 55, 65,
    47, 59, 93, 49, 98, 66, 63, 87, 92, 82,
    76, 74, 96, 43, 94, 58, 79, 86, 51, 69
]
print("Arreglo ordenado:", merge_sort(arr))


