name = "Sasha"
group = "IT-32"

d = 30  
c = 5  

n = d * c

print(f"{name}, {group}")
print(f"n = {d} * {c} = {n}")

divisors_count = 0
divisors_sum = 0

print("Divisors:", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        divisors_count += 1
        divisors_sum += i

print()
print(f"Divisors count: {divisors_count}, sum: {divisors_sum}")

if n < 2:
    print(f"{n} is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

primes_count = 0

print(f"Primes up to {n}:", end=" ")

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        print(number, end=" ")
        primes_count += 1

print()
print(f"Primes count: {primes_count}")