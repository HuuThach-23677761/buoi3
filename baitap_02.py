# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:42:08 2024

@author: Student
"""

#bai 2
a = int(input('nhap so: '))
b = int(input('nhap so: '))
t = a+b
if a>b:
    h = a-b
else:
    h = b-a
ti = a*b
th = a/b
ch = a//b
print ('tinh tong: ', t)
print ('tinh hieu: ', h)
print ('tinh tich: ', ti)
print ('tinh thuong:', round(th,3))
print ('chia het: ', ch)
