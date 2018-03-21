#Ex 1
'''
print("Type a number")
n_a= int(input())
print("Type another number to be added")
n_b= int(input())

print("The sum of the two numbers ", n_a," and ", n_b, "is ", n_a+n_b )





# Ex 2
print("enter a phrase:")
phrase=input()

print("The lenght of the phrase is ",len(phrase))

print(type(len(phrase)))

print(phrase[0],phrase[1], phrase[len(phrase)-2],phrase[len(phrase)-1])

'''

# Ex 3

print("Insert the number corresponding to the action you want to perform: 1. insert a new task; 2. remove a task; 3. show all the tasks; 4. close the program.")
print("Your choice: ")
choice=input()

if choice==1:
    ask= input()
    tasks=[ask]
    print("You want to add more? Y/N")
    choice2=input()
    if choice2=="Y":
        print("Go on")
    tasks.append(input())
    print(tasks)    
       elif choice2==N :
              choice=0
