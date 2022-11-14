# Write a rotate(A, k) function which returns a rotated array A, k times; that is, each
# element of A will be shifted to the right k times
# ○ rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
# ○ rotate([0, 0, 0], 1) returns [0, 0, 0]
# ○ rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]

def rotate(A, K):
    rotated_seq = [] # initialize arr for roated arrays
    for i in range(len(A)): # loop array base on the length of th array
        rotated_seq.append(A[(i-K) % len(A)]) # manipulate array by moving elements to the right
    return rotated_seq

print(rotate([3, 8, 9, 7, 6], 3)) 
print(rotate([0, 0, 0], 1))
print(rotate([1, 2, 3, 4], 4))

# I did provide the most optimized solution for this problem