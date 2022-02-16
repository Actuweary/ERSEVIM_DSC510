# DSC 510
# Week 7
# Programming Assignment Week 7.1
# Author Michael Ersevim
# 7/23/2021

'''Purpose of code is to read in the text of the Gettysburg address, split the text, make it
all lower case, strip out punctuation and count how many there are of each word in descending order
'''

import string
import pprint
global fhand
lst = list()
counts = dict()
global words

def process_line(fhand): #Pull in the lines, strip punctuation and count words
    for line in fhand:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

def add_word(counts): #Add words to the dictionary
    for key, val in list(counts.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    for key in lst:
        print(key, counts[key])

def pretty_print(lst): #Print out the results
    print("The number of words in the text is", len(counts))
    print("--------------------------------------")
    print("Counts Word")
    pprint.pp(lst)

def main(): #Perform all the Main task
    fhand = open('Gettysburg.txt',encoding="utf-8")
    process_line(fhand)
    add_word(counts)
    pretty_print(lst)

if __name__ == "__main__":
    main()
