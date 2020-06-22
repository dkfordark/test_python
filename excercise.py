# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456

# https://viettuts.vn/bai-tap-python/tinh-giai-thua-trong-python 

# bai 1: 
'''
j = [];

for i in range(2000, 3200):
<<<<<<< HEAD
    if ((i%7)==0)
=======
    if (i%7==0) and (i%5!=0):
        j.append(str(i));

print (','.join(j));


# bai 2:

x = int(input("Nhập số cần tính giai thừa : "));
def fact(x):
    if x == 0:
        return 1;
    return (x * fact(x - 1))
print (fact(x));


def tinhgiaithua(n):
    giaithua = 1;
    if (n==0 or n==1):
        return giaithua;
    else:
        for i in range (2, n+1):
            giaithua = giaithua * i;
        return giaithua;

n = int(input("so can tinh giai thua : "));
print (tinhgiaithua(n));


# Bai 3

d = {};
n = int(input("nhap vao so nguyen  n : "));
for i in range (1, n+1):
    d[i] = i * i;
print (d);


# Bai 4

dayso = input("hay nhap cac so, cach nhau boi dau ',': ");
l = dayso.split(',');
print(l);
ltuple = tuple(l);
print(ltuple);


# Bai 5:

class InOutString:
    def __init__(self):
        self.s = "";
    
    def getString (self):
        self.s = input("nhap chuoi: ");

    def printString (self):
        print (self.s.upper());
    
strObj = InOutString();
strObj.getString();
strObj.printString();


# Bai 6

def tinhbinhphuong(n):
    return n**2;

numb = int(input("nhap so can binh phuong : "));
print(tinhbinhphuong(numb));
'''

# Bai 7
print("abc");

def square (num):
    '''
        tra lai gia tri binh phuong cua so duoc nhap vao 
        so nhap vao la so nguyen
    '''
    return num ** 2;

print (square.__doc__);



>>>>>>> 42a4fa36991f01c7af812f834debf760fc4c49f0
