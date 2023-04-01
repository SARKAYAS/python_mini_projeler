while True:

    print("(Döngüden çıkmak için çıkış yazınız.)")
    print("Asal olup olmadığı sorgulanacak sayı:")
    sayi1 = input()


    if sayi1=="çıkış":
        print("Döngüden çıkılıyor...")
        break

    sayi=int(sayi1)

    if sayi > 1:

        for i in range(2, sayi):
            if (sayi % i) == 0:
                print(sayi, " Asal Sayı Değildir.")
                break
        else:
            print(sayi, " Asal Sayıdır.")
            # print(asal_liste)

    sayi = sayi -1



