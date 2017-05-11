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
    # resolving c
    if c < 0:
        x, y = B - x, A - y
    # resolving a
    if a < 0:
        x, y = -x, y
    # resolving b
    if b < 0:
        x, y = x, -y
    q = min(x // B, y // A)
    x, y = x - q * b, y - q * a
    return (x, y)
    
# the input format
print("ax + c = by")
# take input
a = int(input("Enter a: "))
c = int(input("Enter c: "))
b = int(input("Enter b: "))

if abs(c) % gcd(abs(a), abs(b)) != 0:
    print("No solution possible, gcd(%d) of a(%d) and b(%d) doesn't divide c(%d)" % (gcd(a, b), a, b, c))
else:
    soln = kuttakaSolve(a, c, b)
    print("%d * %d + %d = %d = %d = %d * %d" % (a, soln[0], c, a * soln[0] + c, b * soln[1], b, soln[1]))
    print("Solution is " + str(soln))
