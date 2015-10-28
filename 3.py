from decimal import *
import matplotlib.pyplot as plt
import numpy as np

S=int(input()) # сумма
x=float(input()) # годовая ставка %
y=int(input()) # на сколько лет

N=y*12 # на сколько месяцев
P=Decimal(x/100/12).quantize(Decimal('.000001')) # ставка % в месяц в виде дроби (поделено на 100)

D=S*(P+(P/((1+P)**N-1))) # к уплате каждый месяц
D=Decimal(D).quantize(Decimal('.01')) # округлим до копеек

print('Аннуитетный платеж: ',D)
print('Переплата: ',Decimal(D*N-S).quantize(Decimal('.01')))

print('месяц|','остаток|','платеж|','погашение%|','погашение осн. долга')
Ost=Decimal(S).quantize(Decimal('.01'))
sum1=sum2=0
A=[] # остаток по месяцам
a_proc=[] # выплата процентов по месяцам
a_dolg=[] # выплата основного долга по месяцам
for i in range(N+1): # из-за расчетов в целых копейках накапливается остаток на еще один платеж (мааааленький)
    pay_proc=Decimal(Ost*P).quantize(Decimal('.01'))
    if Ost+pay_proc<=D:
        D=Ost+pay_proc
        pay_dolg=Ost
    else:
        pay_dolg=D-pay_proc
    print(i+1, '|',Ost, '|',D, '|',pay_proc,'|',pay_dolg)
    sum1+=pay_proc
    sum2+=pay_dolg
    A.append(Ost)# собираем в массив остаток
    a_proc.append(pay_proc)
    a_dolg.append(pay_dolg)
    Ost-=D-pay_proc
print('накоплено проц:',sum1,' накоплено осн долг: ',sum2)

# нарисуем график остатка
y_pos=np.arange(len(A))
plt.bar(y_pos, A, align='center')
# plt.xticks(y_pos, x1)
plt.ylabel('RUB')
plt.title('Credit Balance by month')
plt.show()

# нарисуем графики сумм в погашение проц и основ долга
width = 0.35       # the width of the bars

fig,ax = plt.subplots()
rects1 = ax.bar(y_pos, a_proc, width, color='r')

rects2 = ax.bar(y_pos+width, a_dolg, width, color='y')

ax.set_xlabel('Month')
ax.set_ylabel('RUB')

ax.set_title('Payment of principal vs Payment of interest')
ax.set_xticks(y_pos+width)

ax.legend( (rects1[0], rects2[0]), ('Payment of interest', 'payment of principal') )

plt.show()