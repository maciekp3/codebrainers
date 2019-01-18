
def my_func():
    return "awesome"

def primes(n):
    """return list of first primes up to n
    >>> is_prime(5)
    """
    prim = []
    for i in range(n):
        if is_prime(i):
            prim.append(i)
    return prim

def is_prime(n):
    """return true if n is prime
    
    >>> is_prime(5)
    True
    >>> is-prime(8)
    False
    """
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # print(is_prime(5))
    # print(is_prime(8))
    # print(primes(100))
    import doctest
    doctest.testmod()
