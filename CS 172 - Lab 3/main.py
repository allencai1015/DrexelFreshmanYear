from fraction import Fraction

def H(n):
    nums = []
    while n > 0:
        temp = Fraction(1, n)
        nums.append(temp)
        n -= 1
    orig = Fraction(0,1)
    for frac in nums:
        orig += frac
    return orig
    
def T(n):
    nums = []
    while n >= 0:
        exp = 2 ** n 
        temp = Fraction(1, exp)
        nums.append(temp)
        n -= 1
    orig = Fraction(0,1)
    for frac in nums:
        orig += frac
    return orig
    
def Z(n):
    nums = []
    while n >= 0:
        exp = 2 ** n 
        temp = Fraction(1, exp)
        nums.append(temp)
        n -= 1
    orig = Fraction(0,1)
    for frac in nums:
        orig += frac
    two = Fraction(2,1)
    return two - orig
    
def R(n,b):
    nums = []
    while n > 0:
        temp = Fraction(1, n) 
        temp = temp ** b
        nums.append(temp)
        n -= 1
    orig = Fraction(0,1)
    for frac in nums:
        orig += frac
    return orig

if __name__ == "__main__":
    def inputN():
        try :
            n = int(input("Enter Number of iterations (integer>0):\n"))
            
            harmonic = H(n)
            twos = T(n)
            zeroes = Z(n)
            prz = R(n,n)
            
            print("H({})={}".format(n, harmonic))
            print("H({})~={:.8f}".format(n, harmonic.approximate()))
            
            print("T({})={}".format(n, twos))
            print("T({})~={:.8f}".format(n, twos.approximate()))
            
            print("Z({})={}".format(n, zeroes))
            print("Z({})~={:.8f}".format(n, zeroes.approximate()))
            
            print("R({},{})={}".format(n, n, prz))
            print("R({},{})~={:.8f}".format(n, n, prz.approximate()))

        except :
            print("Bad Input")
            inputN()
            
    print("Welcome to Fun with Fractions!")
    inputN()
        
