# DSC 510
# Week 8
# Programming Assignment Week 8.1
# Author Michael Ersevim
# 8/1/2021 *** Re-submitted 8/13/2021 ***

'''Purpose of code is to read in the text of the Gettysburg address, split the text, make it
all lower case, strip out punctuation and count how many there are of each word in descending order
'''

import pprint
import string
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
 #   print(counts)

def add_word(counts): #Add words to the dictionary
    for key, val in list(counts.items()):
        lst.append((val,key))
    lst.sort(reverse=True)
    for key in lst:
        print(key,counts[key])
'''
def pretty_print(lst): #Print out the results
    print("The number of words in the text is", len(counts))
    print("--------------------------------------")
    print("Counts Word")
    pprint.pp(lst)
#    print(word,counts[word])
'''
#print(" 'word','count' ") #will print exactly what you see.
##String formatting looks like this: print('{:11s}{:11s}'.format('Word', 'Count'))


#def process_file(lst):
#    data = []
#    filePath = input("Enter the filename you want to save to: ") #user names the output file
#    with open(filePath, 'w') as fileHandle:  # open with a 'w' to prep writing the file
#        data = fileHandle.read(lst)  #define variable as a string to write to the file
 #       print(data)
  #  fileHandle.write(data) #writes the file

def main(): #Perform all the Main task
    fhand = open('Gettysburg.txt')
    process_line(fhand)
    add_word(counts)
#    pretty_print(lst)
 #   process_file(lst)

if __name__ == "__main__":
    main()
