# annual_sallary = float(input("Yıllık Maaşınızı Yazınız : ₺"))
# total_cost = float(input("Hayalinizdeki Evin Değerini Giriniz : ₺"))
# portion_saved = float(input("Maaşınızın Ne Kadarlık Kısmını Biriktireceksiniz : "))
# six_month_rise = float(input("6 Ayda Bir Ne Kadar Zam Alıyor Olacaksınız : "))

annual_sallary = float(120000)
total_cost = float(500000)
portion_saved = float(0.05)
six_month_rise = float(0.03)

r = 0.04
portion_down_payment = total_cost * 0.25
current_savings = 0

month = 1
while 1 > 0:
    saved = (annual_sallary / 12) * portion_saved

    temp_current_saving = current_savings + saved

    additional_saving = temp_current_saving * r / 12

    current_savings = temp_current_saving + additional_saving

    if month % 6 == 0:
        annual_sallary = annual_sallary + (annual_sallary * six_month_rise)

    print("{0}. Ay Birikim Miktarı : ₺{1} ".format(month, current_savings))

    if current_savings >= portion_down_payment:
        print("\nBu Evi Alabilmeniz İçin {} Ay Para Biriktirmelisiniz.".format(month))
        year = month / 12
        print("Bu Evi Alabilmeniz İçin {} Yıl Para Biriktirmelisiniz.".format(year))
        break

    month += 1
