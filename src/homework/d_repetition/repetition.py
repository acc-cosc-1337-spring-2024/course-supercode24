def get_factorial(num):
    factorial = 1
    for i in range(1, num +1):
        factorial *= i
    return factorial


def sum_odd_numbers(num):
    sum_odd = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            sum_odd += i
        i += 1
    return sum_odd
    
