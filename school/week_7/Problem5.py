# 1-100 arası 3 ve 5'e tam bölünebilen sayıları bulan bir program yazınız.

max_number = 100
number = 0
while 1 > 0:
    number += 1

    if (number % 3) == 0 | (number % 5) == 0:
        print("{} Sayısı 3'e ve 5'e Tam Bölünebiliyor!".format(number))

    if number >= max_number:
        break
