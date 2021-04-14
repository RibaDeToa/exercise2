#************************************************************************************************#
#Title :        Newton Raphson's method                                                          #
#Description :  Using python to implement the general Raphson Method on a given equation         #
#Author :       Phindiwe J Ndaba                                                                 #
#Date :         14 April 2021                                                                    #
#************************************************************************************************#

#Given :
  #Newton Raphson's formula : Xnew = X0 -f(x0)/fp(x0)

#Import relevant packages and modules
import numpy as np
import math 

#Variables definition:
  #f = function
  #fp = f prime which is the derivative of x (assuming the derivative of x has been calculated prior)
  #x0 = starting value
  #tol = maximum tolerance (fault value)
  #maxit = maximum number of iterations

def newton(f, fp, x0, tol = 1e -10, maxit = 100):
	#set the current solution to x0
	x = x0
	fx = f(x)
	
	#If the value of the f(x) is less than the tolence, then take x as the solution.	
	if abs(fx) < tol:
		return x
	  
	#Create a loop for to iteration to the maximum stipulated value	
	for i in range(maxit):
	
		#Since f prime is the denominator it should not be zero or approach zero else break the loop
		if abs(fpx) < tol:
	    		break
	  
		#Newton's general equation
		xnew = x - fx/fpx
		fx = f(x) #fx is evaluated to f(x)
	  
		#Checking for fx, if it approaches the tolerance break the loop
		if abs(fx) < tol:
	  		break
	return x
	    
	    
	  
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    	
	
	
