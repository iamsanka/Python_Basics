import os.path

#declare int list and float list
#int_list=[]
#float_list=[]
#get Current Working Directory
path=os.getcwd()
#go in to the examples folder
path+="/examples/"
#Declaring File names
int_File='int.txt'
Float_File='float.txt'

#asking user to enter no's
no=input("Enter a Integer or a Floating point no : ")
while len(no)>0 :
    try :
        no=int(no)
        #int_list.append(no)
        if(os.path.exists(path+int_File)) :
            file=open(path+int_File, "a")
            file.write("\n"+str(no))
        else :
            file=open(path+int_File, "w")
            file.write(str(no))
    except ValueError:
        try :
            no=float(no)
            #float_list.append(no)
            if(os.path.exists(path+Float_File)) :
                file=open(path+Float_File, "a")
                file.write("\n"+str(no))
            else :
                file=open(path+Float_File, "w")
                file.write(str(no))
        except ValueError:
            print("Value you entered is a String")
    no=input("Enter a Integer or a Floating point no : ")

#Reading Files
int_f = open(path+int_File, "r")
print("Records in the Integer No file")
print(int_f.read())

float_f = open(path+Float_File, "r")
print("Records in the Floating No file")
print(float_f.read())