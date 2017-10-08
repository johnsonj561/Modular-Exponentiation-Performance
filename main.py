import math

print '\nCalculating Modular Exponentiation modExp = (b^e) % m, where b = 2 and m = 13'
input_exp = raw_input('\nEnter a value for e: ')  
input_exp = int(input_exp)
print 'You entered ', input_exp 

for i in range(1, input_exp + 1):
  print i
  print pow(2, i)