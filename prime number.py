def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

n = int(input("Enter a positive integer: "))
primes = []
for i in range(2, n+1):
    if is_prime(i):
        primes.append(i)
print("The prime numbers up to", n, "are:", primes)
