#This is a sample file to extract keywords from a file and print those lines in a new file.
import sys
file1 = open("D:\\Downloads\File1.txt", "r")
lines = file1.readlines()
file1.close()

f = open("D:\\Downloads\myfile.txt", "a+")

#create an empty list
stext = []

#number of keywords
n = int(input("Total number of keywords : "))

#iterating till the range
for i in range (0,n):
    word = input().lower()
    stext.append(word+" ")      #adding each keyword

print(stext)

#sample iteration to find keyword
for i in range(0,n):
    if "new" in stext[i]:
        print("ok")
    else:
        print("not ok")


# Strips the newline character
def line_printer():
    count = 0
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()) + "\n")

#y = line_printer()
original_stdout = sys.stdout

# write content to second file
for line in lines:
        if any(word in line for word in stext):
           # print("ok")
            sys.stdout = f
            count = 0
            count += 1
            print("\n{}".format(line.strip()) + "\n")

       #else:
        #    print("not ok")"""


# close the file
f.close()
