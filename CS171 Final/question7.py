numbers = {
    1:"00011",
    2:"00101",
    3:"00110",
    4:"01001",
    5:"01010",
    6:"01100",
    7:"10001",
    8:"10010",
    9:"10100",
    0:"11000",
    }

zip = input("Please enter your ZIP Code: ")
zip_digits = [int(i) for i in zip]
postal_string = '1'
remainder = (sum(zip_digits)) % 10

for digit in zip_digits:
    postal_string = postal_string + numbers[digit]

postal_string = postal_string + numbers[remainder]
postal_string = postal_string + '1' 
print('Your bar code is: {}'.format(postal_string))
    