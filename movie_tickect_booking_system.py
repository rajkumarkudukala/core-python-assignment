def book(available, booked):
    seat = int(input("Enter the seat to be booked: "))
    if seat in available:
        available.remove(seat)
        booked.append(seat)
        print(seat,"is booked")
        print("Available seats: ", available)
    else:
        print(seat,"is not available")
        print("Available seats: ", available)

def cancel(available, booked):
    seat = int(input("Enter the seat to be cancel: "))
    if seat in booked:
        booked.remove(seat)
        available.append(seat)
        available = sorted(available)
        print(seat,"is cancelled")
        print("Available seats: ", available)
    else:
        print(seat, "is not in booked list to cancel")
        print("Available seats: ", available)
        
n = int(input("Enter Total number of seats: "))
available = list(range(1,n+1))
booked = []

print("1) Book Tickect")
print("2) Cancel Ticket")
print("3) Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        book(available, booked)
    elif choice == 2:
        cancel(available, booked)
    elif choice == 3:
        break
    else:
        print("Invalid choice!, try again")
    
