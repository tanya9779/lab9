from decimal import *

def f_1(y,z):
    res = Decimal(108)-(Decimal(815)-Decimal(1500)/z)/y
    print(y,z,res)
    return res

getcontext().prec=42 # Its a max precision in Decimal

x=[]
x.append(Decimal(4))
x.append(Decimal(4.25))
for i in range(2,30):
    print('step ',i)
    x.append(f_1(x[i-1],x[i-2]))
