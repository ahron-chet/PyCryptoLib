from algorithms.myrandom import RandomGenerator
from algorithms.primes import Primes      
from algorithms.bytetools import BytesUtils

class Diffie_Hellman:
    def __init__(self):
        self.__rand = RandomGenerator()

    def __publicNum__(self):
        p = Primes().get_prime(512)
        g = self.__rand.ranrange(100, 1000)
        return {
            'p': p,
            'g': g
        }

    def gen_full_key(self):
        public = self.__publicNum__()
        private = self.gen_private_key()
        public = {
            'p': public['p'],
            'g': public['g'],
            'send': (public['g'] ** private % public['p'])
        }
        return {
            'public': public,
            'private': private
        }

    def gen_private_key(self):
        return self.__rand.ranrange(200, 10**4)

    def import_public(self, recv_public, own_private):
        p, g = recv_public['p'], recv_public['g']
        A_B = BytesUtils.myPow(g, own_private, p)
        return {'send': A_B, 'p': p}

    def gen_first_key(self, key):
        while len(str(key)) < 65:
            key += int(str(key)[-2:]) * key
        assert len(str(key)) > 64
        nkey = b''
        while len(nkey) < 64:
            nkey += bytes([key % 255])
            key = int(str(key)[:-1])
        return nkey

    def send_symmetric_key(self, rcv_public, own_private):
        p, A_B = rcv_public['p'], rcv_public['send']
        key = BytesUtils.myPow(A_B, own_private, p)
        return self.gen_first_key(key)