import re

def get_10thousand_primes():
    with open("10000.txt") as f:
        p = f.read()
        p = re.split("[ ]+|\n", p)
        primes = [int(x) for x in p if len(x)>0]
    return primes

