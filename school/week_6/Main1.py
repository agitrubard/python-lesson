# Bir Dikdörtgenin Alanını Hesaplayan Python Programını yazınız

def calculate_rectangle_area(rectangle_height, rectangle_weight):
    return rectangle_height * rectangle_weight


height = int(input("Enter Rectangle Height : "))
weight = int(input("Enter Rectangle Weight : "))

rectangle_area = calculate_rectangle_area(height, weight)

print("\nRectangle Area Result = {}".format(rectangle_area))
