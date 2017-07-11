import random

class Solovay_Strassen:

    def __init__(self, precizie=40):
        self.k = precizie

    def set_precision(self,precizie):
        self.k = precizie

    def s(self, a, n):
        if a % 4 == 3 and n % 4 == 3:
            #return 1
            return -1
        if a % 4 == 1 or n % 4 == 1:
            #return 0
            return 1

    def jacobi(self, a, n):
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
            return (self.jacobi(2, n)*self.jacobi(a/2, n))
        rest = a % n
        if  rest != a:
            return self.jacobi(rest, n)
        if a < n:
            return self.s(a, n)*self.jacobi(n, a)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def isPrime(self, n):
        if n == 2 or n == 3:
            return True

        if n%2 == 0:
            return False

        a = random.randint(2,n-2)

        if self.gcd(a,n) != 1:
            return False


        if ( pow(a, (n-1)/2,n)) != self.jacobi(a,n) % n:
            return False

        return True

    def test(self, n):
        iteratii = 0

        while iteratii < self.k:
            if self.isPrime(n) == True:
                iteratii += 1
            else:
                return False
        return True





