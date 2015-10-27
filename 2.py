def f_1(y,z):
    res = 108 - (815-1500/z)/y
    print (y,z,res)
    return res

x=[]
x.append(4)
x.append(4.25)
for i in range (2,31):
    print('step ',i)
    x.append(f_1(x[i-1],x[i-2])) 
      
    
