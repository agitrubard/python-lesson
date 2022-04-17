# SORU : Bu sınıf uygulamasında 3 yıl içinde gerekli peşinatı biriktirmek için paranızın ne kadarını
# biriktirmeniz gerektiğinizi bulunuz. Gecen hafta yaptığınız Pyhton Sınıf Uygulaması 3
# programınızı aşağıdaki şekilde modifiyeli ediniz:
# 1. 6 aylık maaş artışını %7 olarak kabul ediniz.
# 2. Mevduat hesabınızın getirisi %4
# 3. Biriktirmeniz gereken miktar ev fiyatınızın %25’i.
# 4. Evin toplam maliyeti 1 milyon TL
# 3 yıl içinde gereken peşinatı biriktirmeniz için hangi oranda maaşınızdan para ayırmanız
# gerektiğini bulunuz.

# annual_sallary = float(input("Yıllık Maaşınızı Yazınız : ₺"))

# 150000
# 0.4411
# 12 adım
# 300.000 , 0.2206 , 9 adımda bulacak

annual_sallary = float(300000)
total_cost = float(1000000)
six_month_rise = float(0.07)

r = 0.04
portion_down_payment = total_cost * 0.25
current_savings = 0

month = 1
year = 3
total_month = year * 12 + 2
month_saving = portion_down_payment / total_month
while 1 > 0:
    saved = month_saving

    temp_current_saving = current_savings + saved

    additional_saving = temp_current_saving * r / 12

    current_savings = temp_current_saving + additional_saving

    print("{0}. Ay Birikim Miktarı : ₺{1} ".format(month, current_savings))

    if current_savings >= portion_down_payment:
        percent = (month_saving * 100) / (current_savings / month)
        print("\n₺{0} Tutarındaki Evi 3 Yılda Alabilmeniz için Aylık Maaşınızın Yüzde %{1} Kısmını Biriktirmelisiniz.".format((int(total_cost)), (int(percent))))
        break

    if month % 6 == 0:
        annual_sallary = annual_sallary + (annual_sallary * six_month_rise)

    month += 1
