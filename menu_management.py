def add():
    x = input("Enter the item to be added: ")
    if x not in menu:
        menu.append(x)
        print(x,'is added')
        print("Updated menu:")
        print(menu)
    else:
        print(x,'already exists')

def remove():
    x = input("Enter the item to be removed: ")
    if x in menu:
        menu.remove(x)
        print(x,'is removed')
        print("Updated menu:")
        print(menu)
    else:
        print(x,'is not available')

def check():
    x = input("Enter the item to be checked: ")
    if x in menu:
        print(x,"is available")
    else:
        print(x,'is not available')

menu = input("Enter initial menu: ").split()

print("Enter 1 to add an item")
print("Enter 2 to remove an item")
print("Enter 3 to check the availability of an item")
print("Enter 4 to exit")

while True:
    choice = int(input("Choice: "))
    
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        check()
    elif choice == 4:
        break
    else:
        print("Invalid choice!\nTry again")
