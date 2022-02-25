"""

"r" -- Open file for reading - default mode
"w" -- Open file for writing
"x" -- Create file if not exists; if not operation is failed
"a" -- Add more content to a file
"t" -- Text mode;  It has a text data .txt -- default mode
"b" -- binary mode;
"+" -- read and write mode
"""

"""_______________________________READ_______________"""
# f = open("pythontest.txt", "r")  # Open returns file pointer here 'f' is file pointer
# print(f.readline()) #Reading Line by line
# print(f.readlines()) # It gives a [list] of lines
# content = f.read()
# for line in f: #REad line one by one
#    print(line, end="")
# print(content)
# f.close()  # Make sure you close it.
"""_________________WRITE______________________"""
# f = open("pythontest.txt", "w")
# f.write("I Will get the job soooon") # if the file exist; it wil replace the contcnt of th file with the new content
# f.close()

# f = open("pythontest.txt", "w")
# a = f.write("it will be job in cloud computing\n")  # it will add the the line at the end
# print(a)
# f.close()
"""________________Read and Write  r+ mode_______________________ Handle read and write mode"""
f = open("pythontest.txt", "r+") # Read and Write both
print(f.read())
f.write("i Will get the job for sure\n")
f.close
