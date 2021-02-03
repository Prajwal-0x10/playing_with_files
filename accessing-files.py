import os


fileptr=open('abcd.txt','r')

if fileptr:
    print("file opened Successfully")
fileptr.close()
#After closing the file, we cannot perform any operation in the file. The file needs to be properly closed.
# If any exception occurs while performing some operations in the file then the program terminates without closing the file.

try:
    fileptr=open('abcd.txt','r')
    if fileptr:
        print("file opened Successfully again")
finally:
    fileptr.close()

#printing content of file
with open('abcd.txt','r') as f:
    print(f.read())


#writing in the file
with open('abcd.txt','w+') as f:
    f.write("Abcdefg")
    print(f.read())

#renaming file
os.rename('abcd.txt','file.txt')



