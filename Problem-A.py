# Given an array A of N integers, write a function missing_int(A) that returns the smallest
# positive integer (greater than 0) that does not occur in A.
# ○ A = [1, 3, 6, 4, 1, 2] should return 5
# ○ A = [1, 2, 3] should return 4
# ○ A = [-1, -1, -1, -5] should return 1
# ○ A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2


def missing_int(A):
    print(max(A) + 2)
    for i in range(1, max(A) + 2): #loop using the max number and 1 in the array extend the number by 2 or more for safe search
        if i not in A: #allow only values that is not exist in array
            return i
    return 1

A1 = [1, 3, 6, 4, 1, 2]
A2 = [1, 2, 3]
A3 = [-1, -1, -1, 5]
A4 = [1, 3, 6, 4, 1, 7, 8, 10]

print(A1," => ",missing_int(A1))
print(A2," => ",missing_int(A2))
print(A3," => ",missing_int(A3))
print(A4," => ",missing_int(A4))

# I did provide the most optimized solution for this problem