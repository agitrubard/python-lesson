while 1 > 0:
    a = int(input("Lütfen Bir Sayı Giriniz (a) : "))
    b = int(input("Lütfen Bir Sayı Giriniz (b) : "))

    if a > b:
        c = a + b
        print("\tAferin! > {0} + {1} = {2}".format(a, b, c))
        break
    else:
        print("\n\tBak Bir Daha Düşün!\n")
