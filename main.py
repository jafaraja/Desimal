#Program mengubah angka desimal menjadi binary, hexa, octal

try:
    dec = int(input('[#] Angka Desimal : '))
    print("\n[x] Hasil dari", dec, "yaitu :\n")
    print("[x] Binary : ", bin(dec))
    print("[x] Hexa : ", hex(dec))
    print("[x] Octal : ", oct(dec))
except:
    print("\n[x] Hanya bisa memasukan angka.")
