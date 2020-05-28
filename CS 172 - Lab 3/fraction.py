#Mark Boady and Matt Burlick
#Drexel University 2018
#CS 172 - Lab 3 Start Code

class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self,a,b):
        self.__num = a
        self.__den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.__den==1:
            return str(self.__num)
        else:
            return str(self.__num)+"/"+str(self.__den)
            
    #Get the Numerator
    def getNum(self):
        return self.__num
        
    #Get the Denominator
    def getDen(self):
        return self.__den
        
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.__num/self.__den
        
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.__num,self.__den)
        self.__num = self.__num // x
        self.__den = self.__den // x
        
    #Find the GCD of a and b
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a % b)
    
    #Compare two fraction objects
    def __eq__(self,other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()
    
    
    
    #Complete these methods in lab
    def __add__(self,other):
        a= self.getNum()
        b = self.getDen()
        x = other.getNum()
        y = other.getDen()
        num = (a * y) + (b * x)
        den = (b * y)
        return Fraction(num, den)
        
    def __sub__(self,other):    # check this
        a= self.getNum()
        b = self.getDen()
        x = other.getNum()
        y = other.getDen()
        num = (a * y) - (b * x)
        den = (b * y)
        return Fraction(num, den)
        
    def __mul__(self,other):
        a= self.getNum()
        b = self.getDen()
        x = other.getNum()
        y = other.getDen()
        num = (a * x)
        den = (b * y)
        return Fraction(num, den)
        
    def __truediv__(self,other):
        a= self.getNum()
        b = self.getDen()
        x = other.getNum()
        y = other.getDen()
        num = (a * y)
        den = (b * x)
        return Fraction(num, den)
        
    def __pow__(self,exp):
        if exp == 0:
            return Fraction(1,1)
        elif exp < 0:
            a= self.getNum()
            b = self.getDen()
            reciprocal = Fraction(b, a)
            neg_exp = exp * -1
            return __pow__(reciprocal, neg_exp)
        else:
            dec = exp - 1
            temp = self.__pow__(dec)
            power = self.__mul__(temp)  
            a = power.getNum()
            b = power.getDen()
            return Fraction(a, b)

