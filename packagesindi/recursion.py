def sum_array(array):
    sum_new = 0
    for i in array:
        sum_new+=i
    return sum_new
    '''Return sum of all items in array'''

def fibonacci(n):
    if n == 1:
        return(1)
    elif n == 0:
        return(0)
    else:

        return fibonacci(n-1) + fibonacci(n-2)
'''Return nth term in fibonacci sequence'''
def factorial(n):
     if n == 0:
        return 1
     else:
        return n * factorial(n-1)
   

def reverse(word):
    str=""
    if len(word) <= 1:
        return word

    return reverse(word[1:]) + word[0]
    '''Return word in reverse'''
