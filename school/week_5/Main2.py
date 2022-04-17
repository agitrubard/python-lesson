def add(a, b):
    print(f"ADDDING {a} + {b}")
    return a + b


def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} x {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions\n")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"\nAge : {age}\nHeight : {height}\nWeight : {weight}\nIQ : {iq}")

print("\n\nHere is a puzzle\n")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print(f"\nThat becomes {what}, Can you do it by hand?")
