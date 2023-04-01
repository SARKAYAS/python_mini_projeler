
def harfler(notu):
    if notu >= 85 and notu < 101:
        print("AA")


    elif notu >= 80 and notu < 85:
        print("BA")


    elif notu >= 75 and notu < 80:
        print("BB")


    elif notu >= 70 and notu < 75:
        print("CB")


    elif notu >= 60 and notu < 70:
        print("CC")


    elif notu >= 55 and notu < 60:
        print("DC")


    elif notu >= 50 and notu < 55:
        print("DD")


    elif notu >= 40 and notu < 50:
        print("FD")


    elif notu >= 0 and notu < 40:
        print("FF")

print("1:SADECE FİNAL VE VİZE NOTUNUZ VARSA")
print("2:FİNAL VE VİZE İLE ÖDEV NOTUNUZ DA VARSA")
islem=int(input("YAPACAĞINIZ İŞLEMİ SEÇİNİZ:"))

while islem>2:
    print("LÜTFEN DOĞRU SAYI GİRİNİZ")
    print("1:SADECE FİNAL VE VİZE NOTUNUZ VARSA")
    print("2:FİNAL VE VİZE İLE ÖDEV NOTUNUZ DA VARSA")
    islem = int(input("YAPACAĞINIZ İŞLEMİ SEÇİNİZ:"))


if islem==1:

    vize1=float(input("Vize notunu giriniz:"))

    final1=float(input("Final notunu giriniz:"))

    vize=40*vize1/100
    final=60*final1/100
    ödev=0
    notu=vize+final+ödev
    print(harfler(notu))



elif islem==2:
    vize1 = float(input("Vize notunu giriniz:"))
    final1 = float(input("Final notunu giriniz:"))
    ödev1 = float(input("Ödev notunuzu giriniz:"))

    vize = 30 * vize1 / 100
    ödev = 20 * ödev1 / 100
    final = 50 * final1 / 100
    notu=vize+final+ödev
    print(harfler(notu))





