import sys
epsil = 1.
while 1.0+epsil!=1.0:
    x=epsil/2
    if 1.0+x != 1.0:
        epsil=epsil/2
    else:
        break
print(str(epsil))
#print(sys.float_info.epsilon)
