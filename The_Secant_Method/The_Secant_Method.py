import math as m


def F(x):
   return (m.exp(x))- pow(2,-x)+(2*m.cos(x))-6

def F2(x):
    return (m.exp(x))-pow(2,-x)*pow(m.log(2),2)+(2*m.cos(x))

def FSM(xi,xi_1):
    return xi_1-(xi-xi_1)/(F(xi)-F(xi_1))*F(xi_1)

E=1e-3
a=1
b=2
xi=0
xi_1=0

E=1e-3
a=1
b=2


xi=0
xi_1=0

if(F(a)*F2(a)>0):
    xi=a
    xi_1=b
elif(F(b)*F2(b)>0):
    xi=b
    xi_1=a

xk=FSM(xi,xi_1)
while(abs(xk-xi_1)>E):
    xi_1=xk
    xk=FSM(xi,xi_1)



print(xk)

