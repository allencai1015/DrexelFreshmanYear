def h_psi(a, n):
    nums = []
    i = 1
    while i <= n:
        x = (n ** i)/ (i ** a)
        nums.append(x)
        i += 1
    h = sum(nums)
    return h

if __name__ == "__main__" :
    print(h_psi(5,3))
    print(h_psi(3,5))
    print(h_psi(2,7))
    