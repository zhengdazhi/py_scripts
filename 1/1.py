#-*-coding:utf-8-*-
import math
#在变量名开头使用类型名
string_radius = raw_input("Enter the radius of your circle:")
int_radius = int(string_radius)

circumference = 2 * math.pi * int_radius
int_area = math.pi * (int_radius ** 2)

#
print "The cirumference is:",circumference,",and the area is:",int_area


