import math as m


def F(x):
   return (m.exp(x))- pow(2,-x)+(2*m.cos(x))-6

def F2(x):
    return (m.exp(x))-pow(2,-x)*pow(m.log(2),2)+(2*m.cos(x))

def FSM(xi,xi_1):
    return xi_1-(xi-xi_1)/(F(xi)-F(xi_1))*F(xi_1)

