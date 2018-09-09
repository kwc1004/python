# -*- coding: utf-8 -*-
import re

txt = """ 
2018-05-12 00:00:01 ABC DEFG log: this is python

2018-05-12 00:00:02 ABC DEFG HI log: this is python

2018-05-12 00:00:03 ABC DEFG HI JKL log: this is python

"""

p = re.compile(r'[A-Z]+.+(?=log:)')
m = p.findall(txt)
#print(temp)

if m:
    print(m)
else:
    print("Not Found")
