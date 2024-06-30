class BytesUtils:
    @staticmethod
    def intToBytes(n, length):
        assert(256 ** length > n and 256 ** (length - 1) < n)

        def div(n):
            while n >= 256:
                n //= 256        
            return n

        b = []
        l = length - 1
        m = n
        for i in range(l):
            c = div(n)
            if int(256 ** (l - i) * c) < n:
                n -= int(256 ** (l - i) * c)
                b.append(c)
            else:
                b.append(0)
        b.append(m % 256)
        return b

    @staticmethod
    def bytesToInt(bytesarry):
        c = len(bytesarry) - 1
        n = 0
        for i in range(len(bytesarry)):
            n += 256 ** (c - i) * bytesarry[i]
        return n 

    @staticmethod
    def getBitLen(n):
        c = 1
        while n >= 256:
            n //= 256
            c += 1
        return c
    
    @staticmethod
    def myPow(x, y, z=False):
        def power(x, y):
            n = 1
            for i in range(y):
                n *= x
            return n
        
        if not z:
            return power(x, y)
        
        n = 1
        while y > 0:
            if y % 2 != 0:
                n = n * x % z
            y //= 2
            x = x * x % z
        return n
