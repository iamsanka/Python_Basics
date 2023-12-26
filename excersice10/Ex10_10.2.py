import os.path
import pickle

#get Current Working Directory
path=os.getcwd()
#go in to the examples folder
path+="/examples/"
#define the file name
filename="names.txt"

#read the file
lines=[""]
Files=open(path+filename, "r")


with open(path+filename,'r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		listli=strip_lines.split()
		#print(listli)
		m=listl.append(listli)
	print(listl)

print("Total Names : ", len(listl))
print("Sorted Names : ", sorted(listl))

