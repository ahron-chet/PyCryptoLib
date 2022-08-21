from PrimeNumbers import Prime
import random
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
    
    def public(self,fullKey):
        return fullKey['public']
    
    def private(self,fullKey):
        return fullKey['private']
    
    
if __name__=='__main__':
    import time
    from ast import literal_eval
    el=ElGamalEncryption()
    while True:
        a=input('''-------Elgamal Encryption--------
        1 To generate new key.
        2 To upload private key.
        3 To upload public key.
        4 To encrypt text.
        5 To decrypt text.\n'''.replace(' '*3,''))
        if a == '1':
            nbit=int(input('please enter bit size: '))
            key = el.genKey(nbit)
            private = key['private']
            public = key['public']
            print('\nThis will be your private key:\n'+str(private))
            time.sleep(1)
            print('\nThis will be your public key:\n'+str(public))
            
            
        elif a=='2':
            private = input('Enter private key: ')
            private = literal_eval(private)
            
        elif a == '3':
            public = input('Enter public key: ')
            public = literal_eval(public)

        elif a=='4':
            try:
                type(public)==dict
            except:
                public = input('Please enter public key')
                public = literal_eval(public)
            m = input('please enter text to encrypt: ')
            enc = el.encrypt(public,m.encode())
            print(base64.b64encode(enc).decode())
            
        elif a=='5':
            try:
                type(private)==dict
            except:
                private = input('Please enter public key')
                private = literal_eval(private)
            m = input('please enter text to decrypt: ')
            m = base64.b64decode(m.encode())
            dec = el.decrypt(private,m)
            print(str(dec)[2:-1])
        time.sleep(1)

