class Frq_use(object):
    def __init__(self):
        import math
        self.f = math.factorial
        self.solution = open("solution.txt", "w")

    def nCk(self, n, k):
        return int(self.f(n) / self.f(k) / self.f(n - k))

    def nAk(self, n, k):
        return int(self.f(n) / self.f(n - k))



fu = Frq_use()
