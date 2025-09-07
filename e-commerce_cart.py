def total(items):
    sum = 0
    if(len(items) == 0):
        print("Empty Cart!") #cart has 0 items
    elif len(items) > 5:
        for i in items:
            sum+=items[i]
        sum-=sum*10/100 #10% discount if cart has more than 5 items
    else:
        for i in items:
            sum+=items[i] #No discount if cart has less than or equal to 5 items
    return sum
items = {}
num_entries = int(input("Enter the number of items in the cart: "))

for _ in range(num_entries):
    key = input("Enter the item name: ")
    value = int(input("Enter the price: "))
    items[key] = value

print("Total Price:",total(items))