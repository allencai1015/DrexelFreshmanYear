import math

i = 0
def star_sqrt(x) :
    global i
    y = math.sqrt(x)
    i += 1
    if x <= 2:
        i = 0
        return i
    if y >= 2:
        star_sqrt(y)
    return i
        
if __name__ == "__main__" :
    print(star_sqrt(4))