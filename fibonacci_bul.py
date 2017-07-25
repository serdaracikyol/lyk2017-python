# Kullanıcıdan alınan sayı kadar fibonacci hesalama

def fibo(sayi):
    sayi = int(sayi)
    fib = 0
    for i in range(0, sayi+1):
        fib += i
    return fib

sayi_al = input("Bir sayı giriniz: ")
print(fibo(sayi_al))