import numpy

# Inputs
x = [4, 15]
x1 = x[0]
x2 = x[1]

# Weights
w = [0, 1]
w1 = w[0]
w2 = w[1]

# Bias
b = 0


def sigmoid_function(a):
    print("Sigmoid Fonksiyonu = 1 / (1 + np.exp(-{}))".format(a))
    return 1 / (1 + numpy.exp(-a))


f = b + w1 * x1 + w2 * x2

print("fnet = {}".format(f))

y = sigmoid_function(f)

print("Sonuç = {}".format(y))
