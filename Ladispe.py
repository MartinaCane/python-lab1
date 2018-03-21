# Ex 1
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

print("Insert the number corresponding to the action you want to perform:")
print("1. insert a new task; 2. remove a task; 3. show all the tasks; 4. close the program.")
print("Your choice: ")
choice=input()

while choice!='4':
    if choice=='1':
        ask= input("Go on: ")
        tasks=[ask]
        choice2=input("You want to add more? (Y/N) ")
        while choice2=='Y':
            tasks.append(input("Go on: "))
            print("Your list is: ", tasks)
            choice2=input("You want to add more? (Y/N) ")
        if choice2=='N':
             choice=input("What now? ")

    if choice=='2':
        tasks.remove(input("Insert a task to be removed: "))
        print(tasks, " Task successfully delated ")
        choice3=input("You want to delate more? (Y/N) ")
        while choice3=='Y':
            tasks.remove(input("Go on: "))
            print(tasks, " Task successfully delated ")
            choice3=input("You want to delate more? (Y/N) ")
        if choice3=='N':
             choice=input("What now? ")

    if choice=='3':
        print(tasks)
        choice=input("What now? ")

print("Bye") 
