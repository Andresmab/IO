#Andres Mauricio Ariza Bustos
#202020113
#Metodo Grafico

from gekko import GEKKO

## Definicion variables

m = GEKKO()

p1 = m.Var(value=25,lb=18,ub=30)
p2 = m.Var(value=25,lb=14,ub=25)


x1= m.Var(value=0, lb=0)
x2= m.Var(value=0, lb=0)
x3= m.Var(value=0, lb=0)
x4= m.Var(value=0, lb=0)


m.Equations([p1 == 4.5*x1 + 4.0*x2, \
             p2 == 3.2*x3 + 2.0*x4,\
             p1 + p2 == 50,\
             x2 + x4 <= 5])

m.Minimize(x1+x3)

m.options.IMODE = 2
m.solve()