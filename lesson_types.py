import math

# calculate square of rectangle
#----------------------------------------------------------------------------------------------------------------------
width = 25
height = 20
rectangle_square = width * height
print ("Площадь прямоугольника при высоте", height, "и ширине", width, "равна", rectangle_square)
print ("Площадь прямоугольника при высоте %d и ширине %d равна %d" % (height, width, rectangle_square))

# calculate hypotenuse
#---------------------------------------------------------------------------------------------------------------------
catheter1 = 7
catheter2 = 4
hypotenuse = math.sqrt(catheter1**2+catheter2**2)
print ("гипотенуза равна", hypotenuse)
print ("гипотенуза при катете1 = %d и катете2 = %d равна = %.3f" % (catheter1, catheter2, hypotenuse))

# calculate square of circle
#------------------------------------------------------------------------------------
radius = 10
circle_square = radius**2 * math.pi
print ("Площадь круга при радиусе = %d см. равна = %.3f кв. см." % (radius, circle_square))


