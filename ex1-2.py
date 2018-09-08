import re
jumin = """
kim chul-su 901212-1234567
Lee jung-hee 761020-2312126
Park chan-ho 980415-1123456
"""
p = re.compile(r'(?P<ju>\w+\s+\d{6}[-])\d{7}')
m = p.sub('\g<ju>*******',jumin)
if m:
    print(m)
else:
    print("Not found")
    
