# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:33:11 2024

@author: Student
"""

print ('========Menu========')
print ('  1.Hu tieu')
print ('  2.Chao long')
print ('  3.Banh canh')
print ('  4.Bun rieu')
print ('  5. Pho bo')
print ('===================')
a = int(input ("Moi nhap lua chon: "))
print ('===================')
if a == 1:
    print('lua chon cua ban la Hu tieu')
elif a == 2:
    print('lua chon cua ban la Chao long')
elif a == 3:
    print('lua chon cua ban la Banh canh')
elif a == 4:
    print('lua chon cua ban la Bun rieu')
elif a == 5:
    print('lua chon cua ban la Pho bo')
else:
    print('khong co lua chon')
