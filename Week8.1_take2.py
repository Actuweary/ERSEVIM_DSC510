# DSC 510
# Week 8
# Programming Assignment Week 8.1
# Author Michael Ersevim
# 8/1/2021                *** Re-submitted 8/14/2021 ***

'''Purpose of code is to read in the text of the Gettysburg address, split the text, make it
all lower case, strip out punctuation and count how many there are of each word in descending order
'''

counts = dict() # define counts as a dictionary
import string #need to improt this for text handling
lst = list() #define lst as a list

def process_line(fhand,counts): #Pull in the lines, strip punctuation and count words
    for line in fhand: #start loop
        line = line.translate(str.maketrans('', '', string.punctuation)) #strip punctuation
        line = line.lower() #make all lower
        words = line.split() #split into lines
        for word in words: #iterate words in a line
            if word not in counts: #adds each word to dictionary...
                counts[word] = 1
            else:
                counts[word] += 1 #and increments if already seen before
    lst=list()
    for key, val in list(counts.items()): #makes a list from the counted values
        lst.append((val,key)) #appends one at a time

    lst.sort(reverse=True) #revrse sort list
    print("There are",len(counts),"unique words in the dictionary!") #print headers
    print("Word - Counts")#print headers
    print("-------------")#print headers
    for key, val in lst:
        print(val," - ", key) #iteratively prints entire list of tuples

def process_file(): #now to save the file
    filename = input("Enter a filename you want to save the output to: ")  # user names the output file
    lst = list()#needed to repeat all this so the variables are defined in this function as well
    for key, val in list(counts.items()):#needed to repeat all this so the variables are defined in this function as well
        lst.append((val, key))#needed to repeat all this so the variables are defined in this function as well
    lst.sort(reverse=True)#needed to repeat all this so the variables are defined in this function as well
    with open(filename, 'w') as fileHandle: #creates new file to be written with 'w'
        fileHandle.write("Total word count:") #add header to file
        fileHandle.write(str(len(counts))+'\n') #add header to file
        fileHandle.write("\nWord - Counts\n") #add header to file
        fileHandle.write("-------------\n") #add header to file
        for t in lst: #iterate list again, converting to string
            fileHandle.write(' - '.join(str(s) for s in t)+'\n')

def main(): #Perform all the Main task
    fhand = open('Gettysburg.txt') #open the text file
    process_line(fhand,counts) #call the line processor
    process_file() #process (i.e., write) the file

if __name__ == "__main__": #good practice
    main()
