# import os 
# import sys
# new_directory="python1"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created successfully.")

import os
#listing files adn directories 
items=os.listdir('.')
print("Files and directories in the current directory:")
for item in items:
    print(item)


#Joining paths =>   Most important to join paths in a platform independent way
dir_name="python1"
file_path="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_path)
print(full_path)



#Check if path exists 

path="file.txt"
if os.path.exists(path):
    print(f"the path {path} exists")
else:
    print(f"path {path} does not exists ")




#CChecking if a path is a File or a Directory 
path="example.txt"
if os.path.isfile(path):
    print("yes it is a file")
if os.path.isdir(path):
    print("yes it is a directory")    