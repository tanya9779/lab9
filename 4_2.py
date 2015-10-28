from fractions import Fraction

def f_1(y,z):
    res = 108-Fraction(815-Fraction(1500,z), y)
#    print( float(y), float(z), float(res) )
    return res

x=[]
x.append(Fraction('4'))
x.append(Fraction('4.25'))
for i in range(2,31):
#    print('step ',i)
    x.append(f_1(x[i-1],x[i-2]))
print( x[30],' ~= ', float(x[30]) )
