import math

class factors:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def fctrs(self):

        z = ((self.b**2)-(4*self.a*self.c))
        
        if z < 0:
            print('roots are complex roots')
        else:
            x = ((self.b * (-1)) - math.sqrt(z))/2*self.a
            y = ((self.b * (-1)) + math.sqrt(z))/2*self.a
            return x, y


fac = factors(1,10,4)
print(fac.fctrs())