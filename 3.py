from decimal import Decimal, getcontext
getcontext().prec = 2
S=int(input())
x=float(input())
y=int(input())

N=y*12
P=x/100/12

D=S*(P+(P/((1+P)**N-1)))

print ('Ануитетный платеж: ' , D)
print ('Переплата:', D*N-S)

print ('месяц|','остаток|','платеж|','погашение%|','погашение осн. долга')
Ost=S
for i in range (N):
    pay_proc=Ost(P
    pay_dolg=D-pay_proc
    print (i+1, Ost, D, pay_proc, pay_dolg)
    Ost-=D-pay_proc
