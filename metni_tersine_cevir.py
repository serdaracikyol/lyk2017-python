# Kullanıcıdan alınan bir metni tersine çevirme.
def ters_cevir(metin):
    yeni_metin = ""
    for m in metin:
        yeni_metin= m+yeni_metin
    return yeni_metin

metin_al = input("Bir şeyler yaz. ")
print(ters_cevir(metin_al))