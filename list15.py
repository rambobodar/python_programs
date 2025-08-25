student=["rambo",7,90.00,True]
print(student)
print(student[0])
print(student[2])
print(student[1])
print(len(student))

#nagetive index

print(student[-3])

#chek the item in present in the list


if 7 in student:
    print("yes")
else:
    print("no")    

if 8 in student:
    print("yes")
else:
    print("no")  

#for slising          

print(student[1:-2])    


""""""""""""""""""""""""""""""""""""

#list comprehension


name=["rambo","rahul","mikelson","7x"]
selname=[n for n in name if "a"in n]
print(selname)

selname=[n for n in name if "8" in n]
print(selname)

ls=[i*i for i in range(10)]
ls=[i for i in ls if i  %2==0]
print(ls)