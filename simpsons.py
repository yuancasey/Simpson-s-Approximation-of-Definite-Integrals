#******************************************************************************
# simpsons.py
#******************************************************************************
# Name: Cheng (Casey) Yuan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#NONE
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math

A = int(input("Enter A: "))
B = int(input("Enter B: "))
N = int(input("Enter N: "))
X = A # x starts at lower bound

e = math.e
pi = math.pi
const_half = 1 / math.sqrt(2*pi) # first half of the equation

sum = 0 # starts from 0, nothing added
coeff = 1 #first term starts at 1, then alternates between 4 and 2
deltaX = (B-A)/N 
out_mult = deltaX / 3 #coefficient for the whole sum

for c in range(0,N+1): # we want the range from 0 to N
  var_half = e ** (- (X**2) / 2) # e^ ( - x^2 / 2)
  entire_calc = const_half * var_half 
  sum = sum + (coeff * entire_calc) # adds current sum to previous sums
  X = X + deltaX # x increases by delta x, all the way to N+1
  if (coeff == 1): # following if/elifs allows alternation between 4 and 2
    coeff = 4
  elif (coeff == 4):
    coeff = 2
  elif (coeff == 2):
    coeff = 4
  if (c == N):
    coeff = 1 #last term must be 1

answer = out_mult * sum
print (answer)


