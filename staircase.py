# Python program to count 
# ways to reach nth stair 
  
# Recursive function to find  
# Nth fibonacci number 
def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2) 
  
# Returns no. of ways to  
# reach sth stair 
def countWays(s): 
    return fib(s + 1) 
  
# Driver program 
s = 4
print "Number of ways = ", 
print countWays(s) 
