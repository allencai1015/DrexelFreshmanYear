def kruskal_frac(a, b) :
    nums = []
    i = 1
    while i <= b:
        x = ((a+b)**i) / i
        nums.append(x)
        i += 1
    k = sum(nums)
    return k

if __name__ == "__main__" :
    print(kruskal_frac(5,3))
        
        