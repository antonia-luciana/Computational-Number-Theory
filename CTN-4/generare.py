from Crypto.Util import number
from Crypto import Random
from Solovay import *
import random

n_length = 64

class GenPrimeRoot:
    def isPrime(self, n):
        if n == 2 or n == 3:
            return True

        if n % 2 == 0:
            return False

        a = random.randint(2, n - 2)

        if self.gcd(a, n) != 1:
            return False

        if (pow(a, (n - 1) / 2)) % n != self.jacobi(a, n) % n:
            return False

        return True

    def s(self, a, n):
        if a % 4 == 3 and n % 4 == 3:
            # return 1
            return -1
        if a % 4 == 1 or n % 4 == 1:
            # return 0
            return 1

    def gcd(self, a, b):
        '''if b == 0:
            return a
        else:
            return self.gcd(b, a % b)'''
        while b:
            a, b = a, a % b
        return abs(a)

    def jacobi(self, a, n):
        #print a, n
        if self.gcd(a,n) != 1:
            return 0
        if n % 2 == 0:
            return "n este par!"
        if a == 1:
            return 1
        if a == 2:
            if n % 8 == 1 or n % 8 == 7:
                return 1
            else:
                return -1
        if a % 2 == 0:
            return (self.jacobi(2, n) * self.jacobi(a / 2, n))
        rest = a % n
        if rest != a:
            return self.jacobi(rest, n)
        if a < n:
            return self.s(a, n) * self.jacobi(n, a)

    def getPrime(self,n_length):
        #pi = []

        if n_length <= 2:
            raise Exception("Alege o lungime mai mare!")

        q = number.getPrime(n_length, Random.get_random_bytes)

        while q == 2 or q == 3:
            q = number.getPrime(n_length, Random.get_random_bytes)

        p = 2 * q + 1

        #if not self.isPrime(p):
            #return self.getPrime(n_length)
        test = Solovay_Strassen()

        if test.test(p) == False:
            return self.getPrime(n_length)

        return p

    def getPi(self, n_length):
        pi = []
        lg = 0
        nr = 1
        while lg < n_length:
            p = number.getPrime(25, Random.get_random_bytes)
            putere = random.randint(1, 5)
            lg *= putere * 25
            nr *= pow(p, putere)
            pi.append((p, putere))

        return nr, pi


    def genPrimeRoot(self, p):
        alpha = random.randint(2, (p-2))

        if self.jacobi(alpha, p) == 1:
            alpha = p-alpha

        return alpha







