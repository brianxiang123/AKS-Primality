# AKS-Primality

This is an implementation of the AKS Primality test that serves as a companion demo for presenting AKS Primality testing in Math 058: Number Theory with Professor Whitehead.

# Algorithm

- Step 1: If $n = a^b$ for $a \in \mathbb{N}$ and $b > 1$, then output composite
- Step 2: Find the smallest $r \in \mathbb{N}$ such that $ord_{r}(n) > \log^2(n)$
- Step 3: If $1 < gcd(a, n) < n$ for some $a \leq r$, then output composite
- Step 4: If $n \leq r$, then output prime
- Step 5: For $a = 1$ to $\lfloor \sqrt{\phi(r)}\log(n) \rfloor$ do
  <p align="center">
    If $(X + a)^n \neq X^n + a \mod{X^r - 1, n})$, then output composite
  </p>
- Step 6: Output prime

# Runtime

**powerCheck($n$)**:

It is important to note that the purpose of AKS is to detect large primes where other forms of primality testing may be computationally infeasible. This means that the storage size of $n$ is nontrivial. Accessing a number of the size $n$ is an $O(\log(n))$ operation. For these reasons **powerCheck** has a run time of $O(\log^3(n))$ because we check at most $log(n)$ values and must simultaneously access two values of size $n$ ($n$ and $b$).

**powerMod($base,power,n$)**:

We loop through all powers of two up to the number and each operation using $base$ is nontrivial so the run time of **powerMod** is $O(\log(base)\log(power))$.

**defineR($n$)**:

We run a loop of size $\log^5(n)$ and another of size $\log^2(n)$. In addition, computing $n$ to a power and modding is an $\log(n)$ operation. Note that since $j$ is bounded by $\log^2(n)$, $\log(power)$ in **powerMod** becomes insignificant. Therefore the run time of **defineR** is $O(\log^8(n))$.

**polyMultiMod($p_1,p_2,n,r$)**:

Looping through all combinations of $a$ and $b$ is $O(ab)$ and each iteration calls $n$ meaning the run time of this function is $O(p_1p_2\log(n))$.

**polySolve($base,power,r$)**:

As seen before, looping through all powers of two requires $\log(power)$ iterations and computing the product of two polynomials is $O(\log(base)r\log(power))$. So the run time of this function is $O(\log(base)\log^2(power)r)$.

**eulerPhi($r$)**:

We loop through all values up to $r$ and find the gcd between $r$ and an integer less than $r$. So the run time of this function is $O(r\log(r))$.

**aks($n$)**:

Bringing everything together we can determine the run time of the aks function. Determining perfect powers is $O(\log^3(n))$. Finding $r$ is $O(\log^8(n)$. $r$ is less than $n$ for large $n$ and the maximum value of $r$ is $\log^5(n)$ so checking the primality of numbers up to $r$ is $O(\log^6(n))$. Finding the Euler's totient is $O(\log^5(n))$. Looping through all values from 1 to $\lfloor \sqrt{\phi(r)}\log{n} \rfloor$ is $O(\log^{\frac{7}{2}}(n))$ and multiplying polynomials of maximum length $r$ is $O(\log^7(n))$. So altogether step $5$ is $O(\log^{\frac{21}{2}}(n))$. Therefore the AKS Primality Test has a run time of $O(\log^{\frac{21}{2}}(n))$.
