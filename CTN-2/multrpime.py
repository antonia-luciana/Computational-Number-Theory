from Crypto.Util import number
from Crypto import Random
import time

class multiprimeRSA:
    def __init__(self, lg):
        self.length = lg

        self.__p = number.getPrime(self.length, Random.get_random_bytes)
        self.__q = number.getPrime(self.length, Random.get_random_bytes)
        self.__r = number.getPrime(self.length, Random.get_random_bytes)

        n = self.__p*self.__q*self.__r
        e = 41
        fi = (self.__p - 1) * (self.__q - 1) * (self.__r - 1)
        d = number.inverse(e, fi)

        self.pk = (e, n)
        self.__sk = (d, n)

    def encrypt(self,x):  # y = n - 1
        n = self.pk[1]
        e = self.pk[0]

        enc = pow(x, e, n)
        return enc

    def decrypt_TCR(self,enc):

        xp = pow((enc % self.__p), self.__sk[0] % (self.__p - 1), self.__p)
        xq = pow((enc % self.__q), self.__sk[0] % (self.__q - 1), self.__q)
        xr = pow((enc % self.__r), self.__sk[0] % (self.__r - 1), self.__r)

        x = xp

        alpha = ((xq - x) * number.inverse(self.__p,self.__q)) % self.__q
        x += alpha * self.__p

        pq = self.__p * self.__q
        beta = ((xr - x) * number.inverse(pq, self.__r)) % self.__r
        x += beta * pq

        return x

    def decrypt_regular(self,enc):
        return pow(enc, self.__sk[0], self.__sk[1])

rsa = multiprimeRSA(512)

x = number.getRandomInteger(2048, Random.get_random_bytes) % rsa.pk[1]

#x = rsa.pk[1] - 1

print "Mesaj :", x

enc = rsa.encrypt(x)

print "Criptare :", enc


start = time.time()
dec1 = rsa.decrypt_regular(enc)
exp_time =  time.time() -  start
print "Timp regular", exp_time
print "Dec regular :", dec1


start = time.time()
dec = rsa.decrypt_TCR(enc)
tcr_time = time.time() -  start
print tcr_time
print "Dec TCR :", dec
print "Timp TCR :",tcr_time

print exp_time/tcr_time

print dec == dec1


def statistica():

    timp_total_regular = 0
    timp_total_TCR = 0
    for i in range(100):
        rsa = multiprimeRSA(512)

        x = number.getRandomInteger(2048, Random.get_random_bytes) % rsa.pk[1]
        enc = rsa.encrypt(x)

        start = time.time()
        dec1 = rsa.decrypt_regular(enc)
        exp_time = time.time() - start
        timp_total_regular += exp_time

        start = time.time()
        dec = rsa.decrypt_TCR(enc)
        tcr_time = time.time() - start
        timp_total_TCR += tcr_time

    print "Medie Regular:", timp_total_regular / 100
    print "Medie TCR:", timp_total_TCR / 100
    print "TCR e de", timp_total_regular/timp_total_TCR,"mai rapid"

print
print statistica()







