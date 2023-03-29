tamBolenler = []
def tamBolenleriBul(sayi):


    for i in range(2, sayi+1):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

sayi1=int(input("Birinci sayıyı giriniz:"))
print("Birinci sayının tam bölenleri:",tamBolenleriBul(sayi1))

sayi2=int(input("İkinci sayıyı giriniz:"))
print("İkinci sayının tam bölenleri:",tamBolenleriBul(sayi2))


#yeni_liste=tamBolenleriBul(sayi1)+tamBolenleriBul(sayi2)
#print("İkisinin toplam tam bölenleri:", yeni_liste)

#set1=set(yeni_liste)
#print("Ortak bölenlerden bir tanesini çıkartınca:",set1)
print(tamBolenler)

i=0
j=0

while i>=0 or j>=0:
    if tamBolenler[i]==tamBolenler[j]:
        print(tamBolenler[i])
        i=i+1

    else:
        i=i+1






