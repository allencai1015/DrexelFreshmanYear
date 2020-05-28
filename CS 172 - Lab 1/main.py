import spellchecker

SP = spellchecker.spellchecker("english_words.txt")
print("Welcome to Text File Spellchecker.")

def get_file():
    file = input("Enter the name of the file to read:\n")
    passed = 0
    failed = 0
    try :
        f = open(file, "r")
        for line_number, line in enumerate(f, 1):
            for word in line.split():
                if SP.check(word) :
                    passed += 1
                else :
                    print("Possible Spelling Error on line {}: {}".format(line_number, word))
                    failed += 1
        print("{:,} words passed spell checker.".format(passed))
        print("{:,} words failed spell checker.".format(failed))
        percentage = (passed / (passed + failed)) * 100
        rounded_percent = round(percentage, 2)
        print("{}% of the words passed.".format(rounded_percent))
    except:
        print("Could not open file.")
        get_file()

if __name__=="__main__":
    get_file()