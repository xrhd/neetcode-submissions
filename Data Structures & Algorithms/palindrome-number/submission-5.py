import math

def num_digits(x: int) -> int:
    return math.ceil(
        math.log(x, 10)
    )
        
def first_digit(x: int) -> int:
    return x // (10 ** (num_digits(x) - 1))

def last_digit(x: int) -> int:
    return x % 10

def update_number(x: int) -> int:
    origin_n = num_digits(x)
    _x = x % (10**(num_digits(x)-1)) # removes the first digt
    removed_digits = origin_n - num_digits(_x)
    if removed_digits == 1:
        _x //= 10 # removes the last digit
        print(f'{x} -> {_x}')
        return _x
    
    _x //= 10 # remove the last digit
    for _ in range(removed_digits - 1):
        # from now on
        if last_digit(_x) !=  0:
            raise Exception('Is not pallindrom')
        _x //= 10
    
    print(f'{x} -> {_x}')
    return _x

def solution(x: int) -> bool:
    if x < 0:
        return False

    while x > 9:
        if first_digit(x) != last_digit(x):
            return False
        try:
            x = update_number(x)
        except:
            return False
    return True 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return solution(x)
        