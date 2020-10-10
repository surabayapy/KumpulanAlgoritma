def linierSearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return False


arr = [1, 3, 6, 7, 10, 90]
ygdicari = 90
hasil = linierSearch(arr, len(arr), ygdicari)
if hasil:
    print("Elemen di temukan di index ke", hasil)
else:
    print("Elemen yang dicari tidak ada dalam array")