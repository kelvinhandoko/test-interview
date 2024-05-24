import functools


def getTotalX(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    def lcm_multiple(numbers):
        return functools.reduce(lcm, numbers)

    def gcd_multiple(numbers):
        return functools.reduce(gcd, numbers)

    # LCM of all elements in array a
    lcm_a = lcm_multiple(a)
    # GCD of all elements in array b
    gcd_b = gcd_multiple(b)

    count = 0
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count


# Contoh penggunaan
n = 2
m = 2
a = [2, 6]
b = [24, 36]
print(getTotalX(a, b))  # Output: 2
