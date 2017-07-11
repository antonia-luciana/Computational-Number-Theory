from PLD import *
from Crypto.Util import number
from Crypto import Random
import time

class Silver_Pohlig_Hellman:
     def __init__(self):
         self.log = PLD()

     def getBis(self,p, alpha, beta, pi):
         xis = []
         bis = []
         for i in range(len(pi)):
             exp = (p - 1)/(pi[i][0])
             #print "exp", exp
             b0 = self.log.Shanks(p, pow(alpha, exp, p), pow(beta, exp, p))
             #print "b0", b0
             b = [b0]
             # j = 1
             sj = b0
             xi = b0 * pow(pi[i][0], pi[i][1] - 1, p)
             for j in range(1, pi[i][1]):
                 exp = (p - 1) / (pi[i][0])
                 #print "exp", exp, "pi", pi[i][1]
                 bj = self.log.Shanks(p, pow(alpha, exp, p),
                                      #pow(beta * pow(number.inverse(alpha, p), sj, p), (exp / pow(pi[i][0], j, p)) % p,
                                      pow(beta * pow(number.inverse(alpha, p), sj, p), (exp *number.inverse(pow(pi[i][0], j, p), p)) % p,
                                          p)
                                      )
                 #print "bj", bj
                 # xi = bj * pow(pi[i][0], pi[i][1] - 1 - i, p)

                 # print "xi", xi
                 b.append(bj)
                 sj += bj
             # b.reverse()
             bis.append(b)
             # xis.append(xi)
         return bis

     def logD(self, p, alpha, beta, pi):
         bis = self.getBis(p,alpha, beta, pi)
         #print "s-au obtinut lista bis", bis
         xis = self.getXis(bis, pi)
         #print "s-au obtinut lista xis", xis

         return self.garner(xis, [pow(p[0],p[1]) for p in pi])

     def getXis(self, reprezentari, pi):

         xis = []
         for i in range(len(reprezentari)):
             baza = pi[i][0]
             xi = 0
             p = 1

             for cifra in reprezentari[i]:

                 xi += cifra * p
                 p *= baza

             xis.append(xi)

         return xis

     def garner(self, bis, mis):
         x = bis[0]

         produs = 1
         for m in mis:
             produs *= m

         prod_m = mis[0]

         for i in range(1,len(bis)):
             alpha = ((bis[i] - x) * number.inverse(prod_m, mis[i])) % mis[i]
             if alpha < 0:
                 alpha = mis[i] + alpha


             x += (alpha * prod_m)
             prod_m = (prod_m * mis[i])

         return x




g = GenPrimeRoot()
sph = Silver_Pohlig_Hellman()

isp = Solovay_Strassen()
#print isp.isPrime(nr)

print "rezultat : ", sph.logD( 13, 2, 10, [(2,2),(3,1)])


