
import math

N = 100   # Maximum number of looping
tolarance= 1e-10
x1=3 

for i in range(N):
   p = x1
   # Evaluate the function and its derivative
   f = 4*p - math.cos(p)
   dfdx = 4 + math.sin(p)
   # The Newton-Raphson 
   x1 = p - f/dfdx
   # Check for convergence and quit if complete
   if math.fabs(p-x1) < tolarance:
      print("NR converged after", i, "iterations")
      print("Root is", x1, "to within", tolarance)
      math.exit(0)

print("Failed to converge after", N, "iterations.")
math.exit(1)
