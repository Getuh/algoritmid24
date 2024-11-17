def binary_search(arr, element):
    vasak, parem = 0, len(arr) - 1
    while vasak <= parem:
        mid = vasak + (parem - vasak) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            vasak = mid + 1
        else:
            parem = mid - 1

    return -1

arr = [1, 5, 8, 10, 21, 23, 39, 47, 64]
element = 8

vastus = binary_search(arr, element)
if vastus != -1:
    print("Number leiti indeksil", vastus)
else:
    print("numbrit ei leitud")