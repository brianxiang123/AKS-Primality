# AKS-Primality

This is an implementation of the AKS Primality test that serves as a companion demo for presenting AKS Primality testing in Math 058: Number Theory with Professor Whitehead.

# Algorithm

- Step 1: If $n = a^b$ for $a \in \mathbb{N}$ and $b > 1$, then output composite
- Step 2: Find the smallest $r \in \mathbb{N}$ such that $ord_{r}(n) > \log^2(n)
- Step 3: If $1 < gcd(a, n) < n$ for some $a \leq r$, then output composite
- Step 4: If $n \leq r$, then output prime
- Step 5: For $a = 1$ to $\lfloor \sqrt{\phi(r)}\log(n) \rfloor$ do
  <p align="center">
    If $(X + a)^n \neq X^n + a \mod{X^r - 1, n})$, then output composite
  </p>
- Step 6: Output prime
