# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456

# https://viettuts.vn/bai-tap-python/tinh-giai-thua-trong-python 

# Bai 7
"""
print(abs.__doc__);

def square (num):
    '''
        tra lai gia tri binh phuong cua so duoc nhap vao 
        so nhap vao la so nguyen
    '''
    return num ** 2;

print (square.__doc__);
"""

# Bai 9

import math;
C = 50;
H = 30;

Q = [];

value = input("Nhap day so cac nhau boi dau ',' : ");
value = value.split(',');
print (value);
for D in value :
    Q = str(round(math.sqrt((2*C* float(D))/H)));
    Q = Q+Q;
    print (Q);
#Q = round(math.sqrt((2*C*D)/H));
print (Q);
"""

# Bai 10


