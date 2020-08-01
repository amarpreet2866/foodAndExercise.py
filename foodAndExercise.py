#Amarpreet Singh
def exercise():    
    i = input("\nEnter your exercise: ")
    of.write(str(gettime()) + " : " + i + "\n")
def food():
    i = input("\nEnter your food: ")
    of.write(str(gettime()) + " : " + i + "\n")
def gettime():
    import datetime
    return datetime.datetime.now()
useAgain = "y"
while useAgain =="y":    
    try:
        s = int(input("1.Enter Log\n2.Retrive\nSelect 1 or 2 : "))    
        n = int(input("\n1.Harry\n2.Rohan\n3.Hammad\nEnter your Selection  : "))
        t = int(input("\n1.Exercise\n2.Diet \nSelect 1 or 2 : "))    
        if s ==1:
            addMore = "y"
            while addMore == "y":
                try:
                    if n==1 and t==1:
                        with open("harrye.txt" ,"a") as of:
                            exercise()
                    elif n==1 and t==2:
                        with open("harryf.txt" ,"a") as of:
                            food()
                    elif n==2 and t==1:
                        with open("rohane.txt" ,"a") as of:
                            exercise()
                    elif n==2 and t==2:
                        with open("rohanf.txt" ,"a") as of:
                            food()        
                    elif n==3 and t==1:
                        with open("hammade.txt" ,"a") as of:
                            exercise()
                    elif n==3 and t==2:
                        with open("hammadf.txt" ,"a") as of:
                            food()
                    else:
                        print("You have entered wrong.Please enter again")   
                    addMore = input("Do you want to add more?\nPress y for Yes and n for No\nEnter : ")         
                except:
                    print("You have entered wrong.Please enter again")               
        elif s == 2:
            try:
                if n==1 and t==1:
                    with open("harrye.txt") as of:
                        print(of.read())
                elif n==1 and t==2:
                    with open("harryf.txt") as of:
                        print(of.read())
                elif n==2 and t==1:
                    with open("rohane.txt") as of:
                        print(of.read())
                elif n==2 and t==2:
                    with open("rohanf.txt") as of:
                        print(of.read())        
                elif n==3 and t==1:
                    with open("hammade.txt") as of:
                        print(of.read())
                elif n==3 and t==2:
                    with open("hammadf.txt") as of:
                        print(of.read())
                else:
                        print("You have entered wrong.Please enter again")        
            except:
                print("You have entered wrong.Please enter again")
        else:
            print("Please enter correct input!")
        useAgain = input("\nDo you want use it again\nPress y for Yes and n for No\nEnter :  ")            
    except:
        print("Please enter correctly!")
print("Thanks for using. Hope to see to again.")