import math
ardiusString = raw_input("Enter the radius of your circle:")
radiusInteger = int(ardiusString)
circurmference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)
print "The cirumference is:",circurmference,",and the area is:",area
