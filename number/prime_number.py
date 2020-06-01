import math

class PrimeNumber:
    def __init__(self, N):
        self.N = N
        self.isP, self.F, self.P = self.compute(N)

    def compute(self, N):
        isP, F, P = [True] * (N + 1), [-1] * (N + 1), []
        for i in range(2, N+1):
            if isP[i]:
                F[i] = i
                P.append(i)
                for j in range(2*i, N+1, i):
                    isP[j] = False
                    F[j] = i
        return isP, F, P

    def factorization(self, x):
        ret, MAX_P = [], int(math.sqrt(x))
        for p in self.P:
            if p > MAX_P: break
            cnt = 0
            while x % p == 0:
                x /= p
                cnt += 1
            ret.append((x, cnt))
        if x > 1: ret.append((x, 1))
        return ret