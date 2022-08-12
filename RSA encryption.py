import random
from hashlib import sha256

class Primes(object):

    def __div2__(self,n):
        e = n-1
        m = 0
        while e % 2 == 0:
            e //= 2
            m += 1
        return e, m

    def __iterat__(self, a, e, m, n):
        if pow(a, e, n) == 1:
            return True

        for i in range(m):
            if pow(a,2**i*e,n)==n-1:
                return True
        return False

    def milerRabin(self,n):
        e, m = self.__div2__(n)
        for i in range(20):
            a = random.randrange(2, n)
            if self.__iterat__(a,e,m,n):
                continue
            else:
                return False
        return True

    def __randomBit__(self,n):
        return(random.randrange(2**(n-1)+1, 2**n-1))

    def isprime(self,num):
        primes=[2,3,5]
        if num==0:
            return False
        if num==1:
            return False
        if num in primes:
            return True
        elif num < 5:
            return False

        if num%(num//2)==0:
            return False

        else:
             for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
        return True


    def get_prime(self,n):
        primes=[]
        for i in range(1000):
            if self.isprime(i):
                primes.append(i)
        while True:
            p = self.__randomBit__(n)
            c=0
            for i in primes:
                if p%i==0:
                    c=1
                    break
            if c==0:
                if self.milerRabin(p):
                    return p     

class Euclids(object):
        
    def gcd(self,a,b):
        while True:
            if a==0 or b==0:
                break
            a,b = a % b, b % a
            r = b + a
        return r
    
    def gcdx(self,a,b):
        if a==0:
            return b,0,1
        r = b % a
        r,x1,y1= self.gcdx(r,a)
        x = y1 - (b//a) * x1
        y = x1
        return r,x,y

class RSA(object):
    
    def __init__(self):
        self.prime = Primes()
        self.nBit=1024
        
  
    def genKey(self,nBit):
        self.nBit=nBit
        e = 65537
        p = self.prime.get_prime(nBit)
        q = self.prime.get_prime(nBit)
        n = p*q
        phi = (p-1)*(q-1)
        _,x,_ = Euclids().gcdx(e,phi)
        assert (e*(phi+x)%phi==1)
        d = phi+x
        private = {'d':d,'n':n,'e':e,'p':p,'q':q}
        public = {'n':n,'e':e}
        return {"private":private,'public':public}
    
    def __intToBytes__(self,n):
        p = (n.bit_length()+7)//8
        b = n.to_bytes(p, 'big')
        return b
    
    
    def __intFromBytes__(self,_bytes):
        return int.from_bytes(_bytes, 'big')
    
    def __encrypt__(self,m,e,n):
        return pow(m,e,n)
    
    def __decrypt__(self,m,d,n):
        return pow(m,d,n)
    
    def __getNbit__(n):
        c=3
        while True:
            if (2**c) // n > 0:
                return 2**c
            c+=1
            
    def encrypt(self,public,message):
        n = public['n']
        message = self.__intFromBytes__(message)
        if message >= n:
            raise 'Data must be < '+str(self.__getNbit__(n)/8)
        e = public['e']
        return self.__intToBytes__(self.__encrypt__(message,e,n))
    
    def decrypt(self,private,message):
        d=key['private']['d']
        n=key['private']['n']
        e=key['private']['e']
        m = self.__intFromBytes__(message)
        return self.__intToBytes__(self.__decrypt__(m,d,n))
    
    def signature(self,private,message):
        h = sha256(message).digest()
        hs= self.__intFromBytes__(h)
        d = private['d']
        n = private['n']
        return self.__intToBytes__(pow(hs,d,n))
    
    def verify_signature(self,public,signature,message):
        h = sha256(message).digest()
        e,n = public['e'],public['n']
        if self.__intToBytes__(pow(self.__intFromBytes__(signature),e,n))==h:
            return True
        return False
        
        
        
