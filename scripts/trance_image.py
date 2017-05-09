#!/usr/bin/env python
#coding:utf-8

from PIL import Image
from pytesser import *

#打开图片，初始化实例im
im = Image.open('images/number1.jpg')
#对实例进行转换黑白图片,L表示1像素/8bit，黑白
imgry = im.convert('L')
#将转换后的图片保存，测试查看
#imgry.save('images/number1.png','png')

#把图片中的噪声去掉，背景就是噪声，背景颜色像素位是140，把大于140的设置为1
threshod = 140
table = []
for i in range(256):
	if i < threshod:
		table.append(0)
	else:
		table.append(1)
out = imgry.point(table,'1')
#保存图片查看测试
#out.save('images/number1.png','png')

text = image_to_string(out)
print text


