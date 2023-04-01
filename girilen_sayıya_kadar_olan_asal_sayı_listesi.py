sayi=int(input("Kendisine kadar olan asal sayıyı alacak sayıyı giriniz:"))

asal_liste=[]

for i in range(sayi+1):

    if sayi > 1:

        for i in range(2, sayi):
            if (sayi % i) == 0:
                #print(sayi, " Asal Sayı Değildir.")
                break
        else:
            #print(sayi, " Asal Sayıdır.")
            asal_liste.append(sayi)
            #print(asal_liste)


    sayi=sayi-1

print("asal sayılar:",asal_liste)



