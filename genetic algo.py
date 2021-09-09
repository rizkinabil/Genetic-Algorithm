import random
import math


def h(x1, x2):
    return math.cos(x1) * math.sin(x2) - (x1 / (x2 * x2 + 1))


LOWER_X1 = -1
UPPER_X1 = 2
LOWER_X2 = -1
UPPER_X2 = 1


class Chromosome:
    def __init__(self):
        self.bit = random.choices([0, 1], k=8)
        self.x1 = self.encoding(UPPER_X1, LOWER_X1, self.bit[:4])
        self.x2 = self.encoding(UPPER_X2, LOWER_X2, self.bit[4:])

    def __repr__(self):
        return '{}, ({}, {})'.format(self.bit, self.x1, self.x2)

    def encoding(self, ra, rb, g):
        tp = [2**-1 for i in range(1, len(g) + 1)]
        return rb + ((ra - rb) / sum(tp) * sum([g[i] * tp[i] for i in range(len(g))]))


'''test = Chromosome()
print(test.bit)
print(test.x1)
print(test.x2)'''


def f(x1, x2):
    return 1 / (h(x1, x2) + 0.01)


populasi = []
while len(populasi) != 50:
    c = Chromosome()

    found = False
    for i in populasi:
        if i.bit == c.bit:
            found = True
            break

        if not found:
            populasi.append(c)


for i in populasi:
    print(i)
