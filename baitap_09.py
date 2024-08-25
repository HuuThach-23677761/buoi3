# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:04:22 2024

@author: Student
"""


a = float(input('nhap so a: '))
b = float(input("nhap so b: "))
T = ((a**(1/2)-b**(a/2))/(a**(1/4)-b**(1/4)))-((a**(1/2)+(a*b)**(1/4))/(a**(1/4)+b**(1/4)))
print('ket qua',T)
