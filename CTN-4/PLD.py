import math
from generare import *
import decimal as dec

class PLD:
    def Shanks(self, p, alpha, beta):
        #print "shanks",p,alpha,beta

        m = int(math.ceil(math.sqrt(p-1)))

        L = [ pow(alpha, j, p) for j in range(0, m) ]

        #L.sort()

        alpha_m = number.inverse( pow( alpha, m, p), p )

        if beta in L:
            return L.index(beta)

        i = 1
        x = (beta * alpha_m) % p

        while x not in L:
            i += 1
            x = (x * alpha_m) % p


        j = L.index(x)

        return i*m + j




'''
dl = PLD()
g = GenPrimeRoot()

p = g.getPrime(32)
alpha = g.genPrimeRoot(p)
beta = random.randint(2, p-1)

print p, alpha, beta
x = dl.Shanks(p, alpha, beta)
print "x = ", x
print "Verificare: ", beta == pow(alpha, x, p)
'''

