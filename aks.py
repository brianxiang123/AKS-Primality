import math
import numpy as np

#O(log^3(n))
def powerCheck(n):
  for b in range(2, int(math.log2(n)) + 1):
    a = n**(1 / b)
    if a == int(a):
      return True
      
  return False

#O(log^8(n))
def defineR(n):
  R = int(math.log2(n)**5)
  for i in range(1, R + 1):
    found = True
    for j in range(1, int(math.log2(n)**2) + 1):
      if powerMod(n, j, i) == 0 or powerMod(n, j, i) == 1:
        found = False
    if found:
      return i
      
  return R

# O(log(base)log(power))
def powerMod(base, power, n):
  result = 1
  while power > 0:
    if power % 2 == 1:
      result = result * base % n
    base = base**2 % n
    power = power // 2
    
  return result


#O(log(power)log^2(base)) the length of base is capped at log^5(n).
# Additionally coefficients can become nontrivial as they go up
# to size n, so runtime is actually O(log(power)log^6(n))
def polySolve(base, power, r):
  coef = np.zeros(r)
  coef[0] = 1
  a = base[0]
  n = power

  while power > 0:
    if power % 2 == 1:
      coef = polyMultiMod(coef, base, n, r)
    base = polyMultiMod(base, base, n, r)
    power = power // 2

  coef[0] = coef[0] - a
  coef[n%r] = coef[n%r] - 1

  return coef

#O(p_1p_2log(n))
def polyMultiMod(p1,p2,n,r):
  coef = np.zeros(r)
  for i in range(len(p1)):
      for j in range(len(p2)):
          coef[(i+j) % r ] = (coef[(i+j) % r ] + p1[i] * p2[j]) % n
        
  return coef

#O(nlog(n))
def eulerPhi(n):
  cnt = 0
  for i in range(1, n + 1):
    if math.gcd(n, i) == 1:
      cnt += 1
  return cnt

#O(log^(21/2)(n))
def aks(n):
  if powerCheck(n):
    return 'Composite'

  r = defineR(n)

  for a in range(2, min(r, n)):
    if math.gcd(a, n) > 1:
      return 'Composite'

  if n <= r:
    return 'Prime'

  for a in range(1, math.floor((eulerPhi(r))**(1 / 2) * math.log2(n))):
    x = polySolve(np.array([a, 1]), n, r)
    if any(x):
      return 'Composite'
  return 'Prime'


# Testing AKS
p = int(input("Enter a number: "))
print(p, " is ", aks(p))
