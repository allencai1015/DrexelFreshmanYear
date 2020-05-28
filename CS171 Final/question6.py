print("To exit type 'quit'")
usrstr = input("Enter text:")
nums = []
onesplace = []
tensplace = []
while usrstr != 'quit':
    for char in usrstr:
        x = ord(char)
        nums.append(x)
    for num in nums:
        ones = num % 10
        onesplace.append(ones)
        tens = (num % 100) // 10
        tensplace.append(tens)
    x = sum(onesplace)
    y = sum(tensplace)
    qhash = x * y
    nums.clear()
    onesplace.clear()
    tensplace.clear()
    print("Hash is {}".format(qhash))
    usrstr = input("Enter text:")
