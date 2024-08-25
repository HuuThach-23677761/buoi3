# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:58:07 2024

@author: Student
"""

a = int(input('nhap so duong co 2 chu so: '))
if 10 <= a <= 99:    
    b = a//10
    c = a%10
    print("ket qua: ", b+c)