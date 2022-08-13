class ElGamalEncryption(object):
    
    def genKey(self,nbit):
        p = Primes().get_prime(nbit)
        g = random.randint(10,p-1)
        a = random.randint(10,p-1)
        A = pow(g,a,p)
        public = {'p':p,'g':g,'A':A}
        private = {'p':p,'a':a,'g':g}
        return {'public':public,'private':private}
    
    def __encrypt__(self,g, p, A, m):
        k = random.randint(2,p-1)
        c1 = pow(g,k,p)
        c2 = (m*pow(A,k,p))%p
        return c1,c2
    
    def __decrypt__(self,a,p,c1,c2):
        x1 = pow(c1,a,p)
        _,x2,_ = Euclids().gcdx(x1,p)
        return c2*x2%p
    
    def __intToBytes__(self,n):
        p = (n.bit_length()+7)//8
        b = n.to_bytes(p, 'big')
        return b
    
    
    def __intFromBytes__(self,_bytes):
        return int.from_bytes(_bytes, 'big')
        
    def encrypt(self,pbk,msg):
        g, p, A = pbk['g'],pbk['p'],pbk['A']
        m = self.__intFromBytes__(msg)
        if m.bit_length()>p.bit_length():
            raise Exception('Data must be smaller than '+str(p.bit_length()//8))
        c1,c2=self.__encrypt__(g, p, A, m)
        enc=[]
        for i in[c1,c2]:
            enc.append(i.to_bytes(p.bit_length()//8,'big'))
        return b''.join(i for i in enc)
    
    def decrypt(self,private,msg):
        a,p = private['a'],private['p']
        c1 = self.__intFromBytes__(msg[:len(msg)//2])
        c2 = self.__intFromBytes__(msg[len(msg)//2:])
        return self.__intToBytes__(self.__decrypt__(a,p,c1,c2))
        
