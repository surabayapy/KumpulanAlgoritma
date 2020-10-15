def swap(a,b):
    c = b
    b = a
    a = c
    return(a,b)

awal = input("masukkan iputan awal : ")
akhir = input("masukkan inputan akhir : ")

print ("\ninputan awal : ", awal)
print ("inputan akhir : ", akhir)

awal, akhir = swap(b=akhir, a=awal)

print("\ninputan setelah swap : ")
print("nilai awal : ",awal, "\nnilai akhir : ",akhir)

