print("1:AKIM DEĞERİNİ BULMA")
print("2:GERİLİM DEĞERİNİ BULMA")
print("3:DİRENÇ DEĞERİNİ BULMA")


islem=int(input("YAPACAĞINIZ İŞLEMİ GİRİNİZ:"))

while islem>4:
    islem = int(input("YANLIŞ SAYI GİRDİNİZ, YAPACAĞINIZ İŞLEMİ TEKRAR GİRİNİZ:"))

if islem==1:

    gerilim=float(input("Gerilim değerini giriniz:"))
    direnç=float(input("Direnç değerini giriniz:"))

        #v=i.r
        #i=v/r
    while True:
        if direnç==0:
            print("Direnç 0 olamaz, tekrar giriniz:")
            direnç = float(input("Direnç değerini giriniz:"))
        else:
            break

    akım=gerilim/direnç

    print("Akım değeri:",akım)

elif islem==2:

    akım = float(input("Akım değerini giriniz:"))
    direnç = float(input("Direnç değerini giriniz:"))

    # v=i.r

    gerilim = akım * direnç

    print("Gerilim değeri:", gerilim)

elif islem == 3:

    gerilim = float(input("Gerilim değerini giriniz:"))
    akım = float(input("Akım değerini giriniz:"))

    # v=i.r
    # r=v/i
    while True:
        if akım == 0:
            print("Akım 0 olamaz, tekrar giriniz:")
            akım = float(input("Akım değerini giriniz:"))
        else:
            break

    direnç = gerilim / akım

    print("Direnç değeri:", direnç)

