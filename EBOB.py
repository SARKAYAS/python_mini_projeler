print("1:SAYILARIN EBOBUNU BULMA\n2:SAYILARIN EKOKUNU BULMA")
print("YAPILMASINI İSTEDİĞİNİZ İŞLEMİ GİRİNİZ:")

işlem=int(input())


if işlem==1:

    sayi1 = int(input("alınacak birinci sayıyı giriniz."))

    sayi2 = int(input("alınacak ikinci sayıyı giriniz"))

    if sayi1>sayi2:
        kucuk_sayi= sayi2

    elif sayi2>sayi1:
        kucuk_sayi=sayi1

    else:
        print("Aynı sayıyı girdiniz.")

    for i in range(1, kucuk_sayi+1):
        if sayi1%i==0 and sayi2%i==0:
            ebob=i

    print(ebob)


elif işlem==2:
    sayi1 = int(input("alınacak birinci sayıyı giriniz."))

    sayi2 = int(input("alınacak ikinci sayıyı giriniz"))

    if sayi1 > sayi2:
        kucuk_sayi = sayi2

    elif sayi2 > sayi1:
        kucuk_sayi = sayi1

    else:
        print("Aynı sayıyı girdiniz.")

    for i in range(1, kucuk_sayi + 1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ekok = sayi2 * sayi1

    print(ekok)

else:
    print("YANLIŞ SAYI GİRDİNİZ...")


