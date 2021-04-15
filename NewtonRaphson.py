#***********************************************************************#
#Title:             Newton Raphson method approximator                  #
#Description:       Algorithm to find root of a real-valued function    #
#Author:            Ntombi                                              #
#Original Date:     14 April 2021                                       #
#***********************************************************************#



def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None
y = lambda x: x**3 - x**2 - 5
Dy = lambda x: 3*x**2 - 2*x
approx = newton(y,Dy,1,1e-5,10)
print(approx)
