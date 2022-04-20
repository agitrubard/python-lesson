# Kullanıcının bilgisayarın tuttuğu sayıyı tahmin ettiği bir Python programını yazınız

import random

computer_number = random.randint(1, 100)

print("Bilgisayarın Tuttuğu Sayı : {}".format(computer_number))

count = 1
while 1 > 0:
    user_number = int(input("\nBir Sayı Giriniz : "))

    if user_number == 0:
        print("\nProgram Durduruldu!")
        break

    if user_number == computer_number:
        print("Sayıyı {} Adımda Buldunuz, Tebrikler!".format(count))
        break
    elif user_number > computer_number:
        print("Daha KÜÇÜK Bir Sayı Giriniz!")
    else:
        print("Daha BÜYÜK Bir Sayı Giriniz!")

    count += 1
