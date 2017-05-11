from math import ceil, sqrt, floor
import fractions


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def kuttakaSolve(a, c, b):
    A, B, C = abs(a), abs(b), abs(c)
    _gcd = gcd(A, gcd(B, C))
    A, B, C = A / _gcd, B / _gcd, C / _gcd
    quot = []
    rem = 0
    d, s = A, B
    while rem != 1:
        rem = d % s
        quot.append(d // s)
        d, s = s, d % s
    x, y = 0, C
    for i in range(0, len(quot)):
        x, y = y, quot[-(i + 1)] * y + x
    if len(quot) % 2 != 0:
        x, y = B - x, A - y
    if c < 0:
        x, y = B - x, A - y
    if a < 0:
        x, y = -x, y
    if b < 0:
        x, y = x, -y
    q = min(x // B, y // A)
    x, y = x - q * b, y - q * a
    return (x, y)


def bhavna(s, x, y, N):
    if s == -1:
        x, y = 2 * x * y, N * x * x + y * y
        # s=1
    if abs(s) == 2:
        x, y = 2 * x * y, N * x * x + y * y
        # s=4
        x, y = fractions.Fraction(x, 2), fractions.Fraction(y, 2)
        # s=1
    if abs(s) == 4:
        x, y = fractions.Fraction(x, 2), fractions.Fraction(y, 2)
        # s=-1
        if s == -4:
            x, y = 2 * x * y, N * x * x + y * y
            # s=1
    _x, _y = x, y
    while x % 1 != 0 and y % 1 != 0:
        x, y, _x, _y = x * _y + _x * y, N * x * _x + y * _y, x, y
        # s=1
    return (int(x), int(y))


def chakravalaSolve(P):
    s = int(round(sqrt(P)) ** 2 - P)
    r = int(sqrt(s + P))
    q = 1
    while abs(s) != 1 and abs(s) != 2 and abs(s) != 4:
        x, y = kuttakaSolve(q, r, abs(s))
        m = (sqrt(P) - x) / abs(s)
        m1, m2 = int(floor(m)), int(ceil(m))
        m = m1 if abs(P - (x + m1 * abs(s)) ** 2) < abs(P - (x + m2 * abs(s)) ** 2) else m2
        X, Y = x + m * abs(s), y + m * q
        s = (X ** 2 - P) / s
        q = Y
        r = int(sqrt(P * q * q + s))
    return bhavna(s, q, r, P)


# the input format
print("Pq^2 + s = r^2")
# take input
P = int(input("Enter P: "))
s = int(input("Enter s: "))

if int(sqrt(P)) ** 2 == P:
    print("No solution for square P(%d = %d ^ 2)" % (P, int(sqrt(P))))
    exit(0)

q, r = chakravalaSolve(P)
q, r = bhavna(s, q, r, P)
print("%d * %d ^ 2 + 1 = %d = %d = %d ^ 2" % (P, q, P * q * q + 1, r * r, r))
print("Solution is " + str((q, r)))
