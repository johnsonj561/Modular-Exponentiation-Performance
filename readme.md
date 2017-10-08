-----
## Modular Exponentiation Performance Considerations
-----

A type of exponentiation performed over a modulus. One common use case is in field of cryptography.

Calculates the remainder when an integer b (base) raised to the eth power (exponent) is divided by a positive integer m (the modulus)

modExp = (b^e) % m

-----

### Memory Constraints
Depending on size of int, b^e will overflow relatively quickly

In Python, integers have arbitrary precision, allowing us to represent an arbitrarily large range of integers that is only limited by available memory. In other languages, like C or C++, overflow requires more attention.

We can avoid potential overflow and improve memory efficiency through use of following equivalency:
if c = a * b
then c mod m = (a * b) mod m = [(a mod m) * (b mod m)] mod m

-----

### Algorithm Analysis

#### Alg1
Alg1(b, e, m):  
  b is multiplied by itself e times  

b and m are constant length; e will grow towards infinity  
Assuming e is encoded in binary, then length of e is lge  
Alg1 running time is approximately 2e = O(e)  
Since |e| = lge and RT = O(e), Alg1 is exponential  
If e was encoded in unary, then |e| = e and Alg1 is linear  

#### Alg2 (Recursion)
Alg2(b, e, m):  
  if e <= 1 return b mod m  
  else if e % 2 == 1 return (b * Alg2(b, e/2, m)) mod m  
  else return [Alg2(b, e/2, m) *  Alg2(b, e/2, m)] mod m  
  
Through recursion we are able to half e each iteration, producing O(lge) run time  

#### Alg3 (Alg2 Improved)
Alg3(b, e, m):  
  if e <= 1 return b mod m  
  else if e % 2 == 1 return (b * Alg2(b, e/2, m)) mod m  
  else:  
    tmp = Alg3(b, e/2, m)    
    return tmp * tmp  
    
In the 3rd branch of Alg2, we are calling on Alg2 twice, doubling the number of recursions  
In Alg3 we assign the result of the recursion to a tmp variable, and then multiply by itself  





