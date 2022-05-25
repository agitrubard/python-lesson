# Backpropagation Algorithm

import numpy

x_1 = 0
x_2 = 1
v_0_1 = 0.3
v_1_1 = 0.6
v_1_2 = -0.3
v_2_1 = -0.1
v_2_2 = 0.4
v_0_2 = 0.5
w_0 = -0.2
w_1 = 0.4
w_2 = 0.1

alpha = 0.25
target = 1


def sigmoid_function(a):
    return 1 / (1 + numpy.exp(-a))


def calculate_error(target, y):
    return (target - y) * (y * (1 - y))


print("-> Hedef Değer -> t = {}".format(target))

print("-> Znet Değerlerini Bul")

z_1_net = v_0_1 + x_1 * v_1_1 + x_2 * v_1_2
z_1 = sigmoid_function(z_1_net)

z_2_net = v_0_2 + x_1 * v_1_2 + x_2 * v_2_2
z_2 = sigmoid_function(z_2_net)

print("z_1 = {}\nz_2 = {}".format(z_1, z_2))

print("")
print("-> ynet'i Hesapla")
y_net = w_0 + w_1 * z_1 + w_2 * z_2
y = sigmoid_function(y_net)

print("y = {}".format(y))
print("")

print("-> Hedef ile y Değerini Karşılaştır")
if y == target:
    print("{} = {} yani t = y olduğundan tamamla.".format(target, y))
else:
    print("{} != {} yani t != y olduğundan hatayı hesapla.".format(target, y))
    error = calculate_error(target, y)
    print("error = {}".format(error))
    print("")

    print("-> Ara Katman ve Çıkış Katmanı Arasındaki Ağırlıkları Güncelle")
    a_w_1 = alpha * error * z_1
    a_w_2 = alpha * error * z_2
    a_w_0 = alpha * error
    print("a_w_1 = {}\na_w_2 = {}\na_w_0 = {}".format(a_w_1, a_w_2, a_w_0))
    print("")

    print("-> Ara Katman ve Çıkış Katmanı Arasındaki Hataları Hesapla")
    net_error_1 = error * w_1
    net_error_2 = error * w_2

    print("")

    error_1 = net_error_1 * (z_1 * (1 - z_1))
    error_2 = net_error_2 * (z_2 * (1 - z_2))
    print("error_1 = {}\nerror_2 = {}".format(error_1, error_2))
    print("")

    print("-> Giriş Katmanı ve Ara Katman Arasındaki Ağırlıkları Güncelle")
    a_v_1_1 = alpha * error_1 * x_1
    a_v_2_1 = alpha * error_1 * x_2
    a_v_0_1 = alpha * error_1
    print("a_v_1_1 = {}\na_v_2_1 = {}\na_v_0_1 = {}".format(a_v_1_1, a_v_2_1, a_v_0_1))

    print("")

    a_v_1_2 = alpha * error_2 * x_1
    a_v_2_2 = alpha * error_2 * x_2
    a_v_0_2 = alpha * error_2
    print("a_v_1_2 = {}\na_v_2_2 = {}\na_v_0_1 = {}".format(a_v_1_2, a_v_2_2, a_v_0_2))

    print("\n")

    print("-> Yeni Ağırlıkları Hesapla")

    v_1_1_new = v_1_1 + a_v_1_1
    v_1_2_new = v_1_2 + a_v_1_2
    v_2_2_new = v_2_2 + a_v_2_2

    w_0_new = w_0 + a_w_0
    w_1_new = w_1 + a_w_1
    w_2_new = w_2 + a_w_2

    v_0_1_new = v_0_1 + a_v_0_1
    v_0_2_new = v_0_2 + a_v_0_2

    print("v_1_1_new = {}\nv_1_2_new = {}\nv_2_2_new = {}".format(v_1_1_new, v_1_2_new, v_2_2_new))
    print("")
    print("w_0_new = {}\nw_1_new = {}\nw_2_new = {}".format(w_0_new, w_1_new, w_2_new))
    print("")
    print("v_0_1_new = {}\nv_0_2_new = {}".format(v_0_1_new, v_0_2_new))
