class RandomGenerator:
    def __init__(self, seed=None):
        if seed is None:
            self.seed = int(str(hash('rand'))[1:])
        else:
            self.seed = seed

    def LCG(self, a=1664525, c=1013904223, m=2**32):
        self.seed = (a * self.seed + c) % m
        return self.seed

    def ranrange(self, start, end, s=False):
        # import random
        # return random.randrange(start, end)
        if not s:
            self.seed = self.LCG()
        
        def park_miller(seed, start, end):
            a = (end - start) / 2147483947
            b = start
            while True:
                seed = (16807 * seed) % 2147483947
                yield a * seed + b

        gen = park_miller(self.seed, start, end)
        if not s:
            self.seed = next(gen) * 214748394734548567561
        return int(next(gen))

