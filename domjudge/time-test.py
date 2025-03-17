# Python code to challenge a 2-second time limit
import math


# Function to perform a computationally expensive task
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Main computation
def main():
    count = 0
    limit = 10**7  # Adjust this to get close to the 2s limit
    for i in range(limit):
        if is_prime(i):  # Check if the number is prime
            count += 1   # Count the number of primes found

    print("Number of primes found:", count)


if __name__ == "__main__":
    main()
