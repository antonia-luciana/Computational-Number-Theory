from Crypto.Util import number
from Crypto import Random
import time

class multipowerRSA:
    def __init__(self, lg):
        self.length = lg

        self.__p = number.getPrime(self.length, Random.get_random_bytes)
        self.__q = number.getPrime(self.length, Random.get_random_bytes)

        #print "p : ", self.__p
        #print "q: ", self.__q

        n = pow(self.__p, 2) * self.__q
        e = 37
        fi = ( pow(self.__p, 2) - self.__p) * (self.__q - 1)
        d = number.inverse(e, fi)

        self.pk = (e, n)
        self.__sk = (d, n)

    def encrypt(self, x):  # y = n - 1
        n = self.pk[1]
        e = self.pk[0]


        enc = pow(x, e, n)

        return enc

    def decrypt_regular(self, y):
        return pow(y, self.__sk[0], self.__sk[1])

    def decrypt_TCR(self, y):
        x0 =  pow((y % self.__p), self.__sk[0] % (self.__p - 1), self.__p)
        xq =  pow((y % self.__q), self.__sk[0] % (self.__q - 1), self.__q)

        p2 = pow(self.__p, 2)
        E = (( y % p2) - pow(x0, self.pk[0], p2)) % p2

        x1 = ((((E / self.__p) % self.__p) * number.inverse((self.pk[0] * pow(x0, self.pk[0] - 1)), self.__p))) % self.__p

        #print (x1 * self.pk[0] * pow(x0, self.pk[0] - 1 )) % self.__p == E/self.__p % self.__p

        xp2 = x0 + self.__p * x1

        #print xp2 % self.__p == x0 % self.__p

        x = xp2
        alpha = (( xq - x ) * number.inverse(p2, self.__q)) % self.__q

        #print (p2 * alpha) % self.__q == (xq - xp2) % self.__q

        x += alpha * p2

        return x

rsa = multipowerRSA(512)

x = number.getRandomInteger(2048,Random.get_random_bytes) % rsa.pk[1]

#x = 104551955080882336140418422933159191176453426695808065643285180917924804240901291216043275837584812242764642437321833000303198481603996047150237450551071820218170031129764211023631962508051038828186635045242950511067556952962262969475703057705310567511898045631395931195988387782176682153353781546826928124686189047808974443053940922734757518902529064301756443576291947426611510203276003691603026776376755358705560230192370081741984056066609859615410672409221317
#x = 74530711097069834433170333283731930495169964987452028410532077876805061180295057668342890032746172848913913567538612760682120011955377457103607291662189223194092279066233528234493991233093629056795756967566379206483164592243841997417193872352142530558158019322194631391463133100504471296182781751384215952392998245079584033757193058162814281651565253762543399864064725365040451259727897286799342600094978029058194521609274861942386032123245477913756089697573505
print "Mesaj : ", x
enc = rsa.encrypt(x)

print "Criptare: ", enc

#enc  = 939679798529115584792921580786062965030795156661983647532907301059631619755405666427423705186514260316772841790022780331758022441949619400312722705080014014000617776369970608510161096981486713370422187234195899226224689794058063053725022045089050980990135117062160415673685788624464692801522024580108030845319063470111875703658822905673251867557387622005115170212808206714825177689421552437484613765296830794342116119711803585620332007222227537475944889887711627

start = time.time()
dec1 = rsa.decrypt_regular(enc)
exp_time =  time.time() -  start
print "Timp regular : ",exp_time

print "Decriptare: ", dec1

start = time.time()
dec = rsa.decrypt_TCR(enc)
tcr_time = time.time() -  start
print "Timp TCR : ", tcr_time


print "Decriptare: ", dec

print exp_time/tcr_time

print dec  == dec1


def statistica():

    timp_total_regular = 0
    timp_total_TCR = 0
    for i in range(100):
        rsa = multipowerRSA(512)

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

    with open("out_multipower.txt","w") as f:
        f.write("Imbunatatire: "+ str(timp_total_regular / timp_total_TCR ) + "\n")

print
statistica()

