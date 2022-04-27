# Girilen sayının pozitif, negatif veya 0 olduğunu bulan bir programı yazınız.

number = int(input("Bir sayı giriniz : "))

if number == 0:
    print("{} Sayısı 0'a Eşittir.".format(number))
elif number > 0:
    print("{} Sayısı POZİTİF Bir Sayıdır.".format(number))
else:
    print("{} Sayısı NEGATİF Bir Sayıdır.".format(number))
