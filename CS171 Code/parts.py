# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
    # FIXME: The following line will throw ValueError exception.
if parts[1] is str :
    raise ValueError
    #        Insert try/except blocks to catch the exception.
while name != -1 :
    try :
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
        parts = input().split()
        name = parts[0]
    except ValueError :
        parts[1] = 0

# Get next line
parts = input().split()
name = parts[0]
