import csv

# Type your code here. 
filecsv = input()

unique_words = []
count = {}

with open(filecsv, 'r') as csvfile:
   contents = csv.reader(csvfile, delimiter=',')
   for words in contents :
        for x in words : 
            if x not in unique_words:
                unique_words.append(x)
                count[x] = 1
            else :
                repeats = int(count[x])     
                repeats += 1
                count[x] = repeats        
for i in count :
    print("{} {}".format(i, count[i]))