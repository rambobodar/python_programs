#function logic bulid in function]
def sumnumber(A,b):
    add=(A+b)
    print(add)

def getbignuumber(A,b):
    if(A<b):
        print("a is small")
    else:
        print("a is biger")        


A=60
b=50
sumnumber(A,b)
getbignuumber(A,b)
""""""""""""""""""""""""""""""""""""""""""""""""""



#defult  argumentsssssssssssss

def avreg(a=10,b=10):
    print("the avgre is",(a+b)/2 )

avreg(b=20) 

#in this case this arguments take defult value from the function 

""""""""""""""""""""""""""""""""""""""""""""""""""




#keyword  argumentsssssssssssss

def avreg(a=10,b=10):
    print("the avgre is",(a+b)/2 )

avreg(b=80,a=20) 

#and not take in order this will take automatic in ordeer value
""""""""""""""""""""""""""""""""""""""""""""""""""



# required argumentsssssssssssss

def cars(newcar,oldcar,midelcar):
    print("yahh this is",newcar,oldcar,midelcar)

cars("ferarri",", bmw",", marsidice")

#in this senario you must be required give a value know as the name

""""""""""""""""""""""""""""""""""""""""""""""""""





