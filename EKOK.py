birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1, kucuksayi + 1):
    if (birinciSayi % i == 0) and (ikinciSayi % i == 0):
        ebob = i
        ekok = (birinciSayi * ikinciSayi) // ebob

print("EBOB:", ebob)
print("EKOK:", ekok)