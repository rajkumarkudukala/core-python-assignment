def calculate_fare(trips):
    length = len(trips)
    if length == 0:
        print("No trips to calculate: ")
        return
    total = 0
    for i in range(length):
        cost = 50+trips[i]*10
        print(f"Trip {i+1}: ${50+trips[i]*10}")
        total += cost
    print("Total Fare:",total)
    return

trips = list(map(int,input("Enter trips (space seperated): ").split()))
calculate_fare(trips)