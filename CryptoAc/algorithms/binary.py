class Binary:
    @staticmethod
    def getBin(n, pad=False):
        l = ''
        while n > 0:
            l += str(n % 2)
            n //= 2
        l = l[::-1]
        if not pad:
            return l
        if len(l) >= pad:
            pad = len(l)
        return '0' * (pad - len(l)) + l

    @staticmethod
    def binRevers(b):
        n = 0
        for i in range(len(str(int(b)))):
            if int(b[-(i + 1)]) != 0:
                n += 2 ** (i + 1)
        return n // 2

    @staticmethod
    def xor(a, b):
        assert len(a) == len(b)
        
        def __xor__(a, b):
            return '0' if a == b else '1'
        
        x = ''
        for i in range(len(a)):
            x += str(__xor__(a[i], b[i]))
        return x

    @staticmethod
    def xorBytes(a, b):
        def __xor__(a, b):
            ba, bb = Binary.getBin(a, 8), Binary.getBin(b, 8)
            m = Binary.binRevers(Binary.xor(ba, bb))
            return bytes([m])
        
        x = bytes()
        for i in range(len(a)):
            x += __xor__(a[i], b[i])
        return x
