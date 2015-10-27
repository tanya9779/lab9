epsil = 0.000001
while True:
    x=epsil/10
    if 1.0+x == 1.0 and 1.0 + epsil !=1.0:
        print (str(epsil))
        break
    epsil=epsil/10
