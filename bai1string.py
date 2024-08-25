# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:43:56 2024

@author: Student
"""
a = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
s1 = a.split(", ")
print("bảng 1")
for b in s1:
    print(b)
print('')
print ("bảng 2")
s2 = a.replace(" P.", " ").replace("Q.", "").replace("Tp.","")
s3 = s2.split(", ")
for c in s3:
    print (c)