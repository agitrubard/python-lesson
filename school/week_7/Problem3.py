# Yaşı girilen bir kişinin ehliyet alıp alamayacğaını gösteren bir program yazınız.

age = int(input("Yaşınızı Giriniz : "))

if age < 18:
    print("\nYaşınız : {} -> Ehliyet Alamazsınız!".format(age))
else:
    print("\nYaşınız : {} -> Ehliyet Alabilirsiniz!".format(age))
