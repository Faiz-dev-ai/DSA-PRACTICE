def nthRoot(n,m):
    low = 1
    high = m
    while(low<=high):
        mid = (low + high)//2
        if mid ** n == m:
            return mid
        elif mid ** n > m:
            high = mid - 1
        elif mid ** n < m:
            low = mid + 1
    return -1
n = 2
m = 64
print(nthRoot(n,m))