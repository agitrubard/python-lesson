import numpy

# Inputs
x = [4, 15]
# Weights
w = [0, 1]
# Bias
b = 0


def sigmoid_function(a):
    print("Sigmoid Fonksiyonu = 1 / (1 + np.exp(-{}))".format(a))
    return 1 / (1 + numpy.exp(-a))


f = b
i = 0
for i in range(len(x)):
    f += w[i] * x[i]

print("fnet = {}".format(f))

y = sigmoid_function(f)

print("Sonuç = {}".format(y))
