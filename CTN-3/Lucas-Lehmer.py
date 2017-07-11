import math
import time

class Lucas_Lehmer:

    def isPrime(self, p):
        for i in range(2, int(math.sqrt(p))):
            if p % i == 0:
                return False
        return True

    def test(self, p):  # este 2^p-1 prim?

        if self.isPrime(p) == False:
            return False
        if p <= 1:
            return False

        s = 4
        M = pow(2, p) - 1

        for i in range(p-2):
            s  = pow((s % M),2, M) - 2

        return (s == 0)

    def test1(self, p):  # este 2^p-1 prim?

        if self.isPrime(p) == False:
            return False
        if p <= 1:
            return False
        s = 4
        M = pow(2, p) - 1

        for i in range(p-2):
            s = ( pow(s, 2) - 2) % M
        #print "aici", (s == s2)
        return (s == 0)

    def test2(self, p):  # este 2^p-1 prim?

        if self.isPrime(p) == False:
            return False
        if p <= 1:
            return False

        s = 4
        M = pow(2, p) - 1

        for i in range(p-2):
            x = pow(s, 2)
            s = (x >> p) + (x & M)
            if s >= M:
                s -= M
            s -= 2
        return (s == 0)


test = Lucas_Lehmer()

start = time.time()
test.test(12007)
print time.time()-start

start = time.time()
test.test1(12007)
print time.time()-start

start = time.time()
print test.test2(12007)
print time.time()-start

