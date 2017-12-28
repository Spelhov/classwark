import cmath
def power(base, exp):
    print("power func")
    return base**exp

def print_delimiter(symbol="+", num_repeat=40):
    print(symbol * num_repeat)

def pretty_print(value):
    print_delimiter()
    print("value:", value)
    print_delimiter("~", 50)

result1 = power(5, 3)
print(result1)


def rectangle_square(width, heigth):
    result = width * heigth
    return result


result2 = rectangle_square(10, 20)
pretty_print(result2)
my_pi = cmath.pi

def circle_square(radius):
    result = power(radius, 2) * my_pi
    return result

result3 = circle_square(10)
pretty_print(result3)
def calculate_sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result
result4, result5 = calculate_sum_and_product(2, 3)
pretty_print(result4)
pretty_print(result5)


def fareh2celc(degrees):
    return (degrees - 32) / 1.8


def celc2fareh(degrees):
    return degrees * 1.8 + 32
print(celc2fareh(36.6))
print(fareh2celc(90))



