with open('python\check.txt','r') as file:
    for line in file:
        print(line)
        print(line.strip()) # THis removes leading and trailing whitespace including newlines
        print(line.rstrip())    # This removes trailing whitespace including newlines
        print(line.lstrip())    # This removes leading whitespace
           