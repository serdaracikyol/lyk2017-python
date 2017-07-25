# İki kullanıcı ile taş kağıt makas oyunu.

def oyna(oyuncu1, oyuncu2):
    if oyuncu1 == "taş" and oyuncu2 == "makas":
        print("Kazanan: 1. oyuncu")
    elif oyuncu1 == "taş" and oyuncu2 == "kağıt":
        print("Kazanan: 2. oyuncu")
    elif oyuncu1 == "taş" and oyuncu2 == "taş":
        print("Berabere.")
    elif oyuncu1 == "kağıt" and oyuncu2 == "makas":
        print("Kazanan: 2. oyuncu")
    elif oyuncu1 == "kağıt" and oyuncu2 == "taş":
        print("Kazanan: 1. oyuncu")
    elif oyuncu1 == "kağıt" and oyuncu2 == "kağıt":
        print("Berabere.")
    elif oyuncu1 == "makas" and oyuncu2 == "kağıt":
        print("Kazanan: 2. oyuncu")
    elif oyuncu1 == "makas" and oyuncu2 == "taş":
        print("Kazanan: 2. oyuncu")
    elif oyuncu1 == "makas" and oyuncu2 == "makas":
        print("Berabere.")
    else:
        print("Geçersiz hamle.")

oyuncu_1 = input("Birinci oyuncunun hamlesi: ")
oyuncu_2 = input("İkinci oyuncunun hamlesi: ")
oyna(oyuncu_1,oyuncu_2)
