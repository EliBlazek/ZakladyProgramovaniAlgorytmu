from math import factorial
from functools import lru_cache

my_num = 8

lru_cache(1000) #built-in cache. It should enhance performance. Idea is from Socratica https://www.youtube.com/watch?v=Qk0zUZW-U_M&t 
def my_custom_factorial(a):
    my_counter = a 
    if a == 0:
        return(1)
    elif a > 9999:
        print("Sorry, im not going to melt my processor. Go find a NASA computer.")
    else: 
        while my_counter >= 0: #To je prasárna, ten loop. 
            my_counter = my_counter - 1 
            return a * (my_custom_factorial(a-1))

my_result1 = (my_custom_factorial(my_num))

def rate_functions(): #I was too lazy comparing numbers in terminal myself.
    my_result2 = factorial(my_num) #I'd love to time it and see how my functions holds up to the default Python factorial. But I'm not sure what modul to use and how. 
    if my_result1 == my_result2:
        print("Yeah, works well enough.")
        print(my_result1)
    else: print("Faulty logic in your function")

rate_functions()
