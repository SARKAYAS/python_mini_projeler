import math

kenar1=int(input("Üçgenin yatay kenarının uzunluğunu giriniz: "))
kenar2=int(input("Üçgenin dikey kenarının uzunluğunu giriniz:"))

def karesi(sayi):
    return sayi*sayi

kenar1_karesi=karesi(kenar1)
kenar2_karesi=karesi(kenar2)

hipotenüs_karesi=kenar1_karesi+kenar2_karesi

hipotenüs=math.sqrt(hipotenüs_karesi)

print("Hipotenüs:", hipotenüs)
