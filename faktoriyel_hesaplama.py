# Kullanıcıdan alınan sayının faktöriyelini hesaplama.
def fakt(sayi):
    sayi = int(sayi)
    faktoriyel = 1
    while(0<sayi):
        faktoriyel*=sayi
        sayi=sayi-1
    return faktoriyel

sayi_al = input("Sayı girin: ")
print("Faktöriyeli: ", fakt(sayi_al))

#recursive
def asd(sayi):
    sayi = int(sayi)
    if sayi == 0:
        return 1
    else:
        return sayi * asd(sayi-1)

print("-----------",asd(sayi_al))