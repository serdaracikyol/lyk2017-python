# İstenilen sayıda asal sayı üretme

def asal_uret(sayi):
    sayi = int(sayi)
    asal_sayilar = []
    i = 1
    while True:
        bolunurmu = False
        for a in range(2, i):
            if (i%a)==0:
                bolunurmu = True
        if bolunurmu != True:
            asal_sayilar.append(i)
        i+=1
        if len(asal_sayilar) == sayi:
            break
    return asal_sayilar

sayi_al = input("Kaç tane asal sayı üretilsin ? ")
print(asal_uret(sayi_al))