# Write a function find_divisible(a, b, k) that accepts three integers: a, b and k, and returns
# the count of the numbers between a and b that are divisible by k
# ○ find_divisible(6,11,2) should return 3
# ○ find_divisible(0,11,2) should return 6

def find_divisible(a, b, k):
    count = 0
    for i in range(a, b): # get only the numbers between a and b
        if i % k == 0: # find if numbers between a and b that is divisible by k
            count += 1
    return count

print(find_divisible(6,11,2))
print(find_divisible(0,11,2))

# I did provide the most optimized solution for this problem