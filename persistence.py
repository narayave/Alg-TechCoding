
# Code wars

'''

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

'''


def persistence(n):
    # your code
    
    count = 0
    while len(str(n)) > 1:
        count += 1
        tmp = str(n)
        
        res = 1
        for i in tmp:
           res *= int(i)
        
        n = res        
        
    return count