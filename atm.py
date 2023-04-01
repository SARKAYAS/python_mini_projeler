#1-para çekme
#2-para yatırma
#3-kart bilgileri
#4-kart iade

bakiye = 2000

while True:
    print("1:PARA ÇEKME")
    print("2:PARA YATIRMA")
    print("3:KART BİLGİLERİ")
    print("4:KART İADE")

    işlem=int(input("YAPACAĞINIZ İŞLEMİ GİRİNİZ:"))


    if işlem==1:
        print("\n*******************\n")

        çekilecek_tutar=int(input("Çekilecek tutarı giriniz:"))

        if çekilecek_tutar<=bakiye:

            bakiye=bakiye-çekilecek_tutar

            print("Mevcut bakiyeniz:",bakiye)

        else:
            print("Yetersiz bakiye...")

    elif işlem==2:

        print("\n*******************\n")

        yatırılacak_tutar=int(input("Yatırılacak tutarı giriniz:"))

        bakiye=bakiye+yatırılacak_tutar

        print("Mevcut bakiyeniz:",bakiye)

    elif işlem==3:

        print("\n*******************\n")

        print("Hesap sahibi:Ayşegül SARIKAYA")
        print("Hesap IBAN:TR21 0001 0090 1002 2035 6050 01 ")
        print("Mevcut bakiyeniz: ", bakiye)

    elif işlem==4:

        print("\n*******************\n")

        print("Kartınız iade ediliyor...")
        break

    else:
        print("\nYanlış sayı girdiniz, tekrar tuşlayınız....\n")







