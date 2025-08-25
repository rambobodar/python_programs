num=int(input("enter the number"))

match num:

    case 0:
        print("num is zero")

    case 10:
        print("num is 10")

    case _ if num < 100:
        print("this mnunm not valide")
        
    case _ if num >100:
        print("hogest number ")


        #this is a match case topic