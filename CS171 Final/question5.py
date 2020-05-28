def count_case_switches(letters):
    i = 0
    for letter in letters:
        next_letter = letters.index(letter)
        if letter.islower() == True :
            if letters[next_letter + 1].isupper()  :
                i += 1
        if letter.isupper() == True :
            if letters[next_letter + 1].islower()  :
                i += 1
    return i

print(count_case_switches("AbbAAAbbb"))
print(count_case_switches("wWwww"))
                        