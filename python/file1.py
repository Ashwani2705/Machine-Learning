with open('python\check.txt','r') as file:
    for line in file:
        print(line)
        print(line.strip()) # THis removes leading and trailing whitespace including newlines
        print(line.rstrip())    # This removes trailing whitespace including newlines
        print(line.lstrip())    # This removes leading whitespace
           

with open('python\check.txt','w') as file:
    file.write("Hello world\n")
    file.write("This is a new line ")

#checking the content of the file 
with open('python\check.txt','r') as file:
    for line in file:
        print(line)



#Writing a file without overwriting 
with open('python\check.txt','a') as file:    #opening file in append mode 
    file.write("append operarion taking place lets see ")