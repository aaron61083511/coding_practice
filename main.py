from math import ceil
def karatsuba(x, y):
  sx = str(x)
  sy = str(y)
  n = max(len(sx), len(sy))
  if len(sx) == 1 and len(sy) == 1:
    return x*y
  m = ceil(n/2)
  a = int(x // (10**m))
  b = int(x % (10**m))
  c = int(y // (10**m))
  d = int(y % (10**m))
  ac = karatsuba(int(a), int(c))
  bd = karatsuba(int(b), int(d))
  adbc = karatsuba(int(a) + int(b), int(c) + int(d)) - ac - bd
  return int(str(ac) + '0' * 2 * m) + int(str(adbc) + '0' * m) + bd
karatsuba(200, 500)
