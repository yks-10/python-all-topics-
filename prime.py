
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def prime_generator(nums):
    for num in nums:
        if is_prime(num):
            yield num

# Usage
nums = [2, 4, 5, 6, 7, 8, 11]
for num in prime_generator(nums):
    print(num)



