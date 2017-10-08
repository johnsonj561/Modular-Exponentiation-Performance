import math
import time

print '\nCalculating Modular Exponentiation modExp = (b^e) % m, where b = 2 and m = 13'
input_exp = raw_input('\nEnter a value for e: ')  
input_exp = int(input_exp)
m = 13
b = 2
print 'You entered ', input_exp 

# Algorithm 1 is at risk of overflow
def modExp1(b, e, m):
  modExp = pow(b, e) % m
  return modExp

# Algorithm 2 uses recursion to limit prevent overflow
def modExp2(b, e, m):
  if(e < 1):
    return b % m
  elif(e % 2 == 0):
    return (modExp2(b, e/2, m) * modExp2(b, e/2, m)) % m
  else:
    return (b * modExp2(b, e/2, m)) % m 

# Algorithm 3 improves running time by reducing total recursion calls (lines 5 - 6)
def modExp3(b, e, m):
  if(e < 1):
    return b % m
  elif(e % 2 == 0):
    tmp = modExp3(b, e/2, m)
    return (tmp * tmp) % m
  else:
    return ((b) * modExp3(b, e/2, m)) % m
  
# Testing modExp1  
t_start = time.clock()
res1 = modExp1(b, input_exp, m)
print '\nmodExp1(' + str(input_exp) + ') completed in ' + str((time.clock() - t_start)*1000) + ' ms'
print 'modExp1(' + str(input_exp) + ') = ' + str(res1)

# Testing modExp2
t_start = time.clock()
res2 = modExp2(b, input_exp, m)
print '\nmodExp2(' + str(input_exp) + ') completed in ' + str((time.clock() - t_start)*1000) + ' ms'
print 'modExp2(' + str(input_exp) + ') = ' + str(res2)

# Testing modExp3
t_start = time.clock()
res3 = modExp3(b, input_exp, m)
print '\nmodExp3(' + str(input_exp) + ') completed in ' + str((time.clock() - t_start)*1000) + ' ms'
print 'modExp3(' + str(input_exp) + ') = ' + str(res3)
