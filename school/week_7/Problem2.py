# Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini hesaplayınız.
# Eğer indeks 25 ile 30 aralığındaysa kilolu, 30 veya daha yüksekse obez,
# 35 veya daha fazlaysa ciddi obez olarak durumu yazdırınız.

height = float(input("Boy Değerinizi Giriniz (M) : "))
weight = float(input("Ağırlık Değerinizi Giriniz (KG) : "))

vki = weight / (height * height)
print("\nVücut Kitle İndeksi = {}".format(vki))
if vki <= 25:
    print("\nNORMAL!")
elif vki > 25:
    print("\nKİLOLU!")
elif vki > 30:
    print("\nOBEZ!")
else:
    print("\nCİDDİ OBEZ!")
