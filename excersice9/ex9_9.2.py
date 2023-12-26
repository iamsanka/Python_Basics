#Read all the files on C
import os

#Specifying the path
path="C://"
#list down all the files in the path
dir_list=os.listdir(path)

print("Files and Directories in ",path, " : ")
print(dir_list)

###Explanation!!!!!!!!!!!1
#whe we try to create a file to the root path we need to give the specifica permissions other wse it will show
# an error 
try :
    #create a new text file in the specificlocation
    f = open("C:/ayho.txt", "x")
    print(dir_list)
except PermissionError :
    print("Permission denied to create the file")

#to give the file permissions 
#we can use the 'stat' package in the python
#we can use S_IRUSR|S_IWUSR|SIXUSR to give the all permissions which is equalent to chmod777