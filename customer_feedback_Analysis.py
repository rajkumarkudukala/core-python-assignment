def positive_percentage(ratings):
    length = len(ratings)
    if(length == 0):
        print("No ratings Entered")
    else:
        count = 0
        for i in range(length):
            if ratings[i] >= 4:
                count+=1
        print("Positive Feedback: ",count*100/length,"%",sep='')


ratings = list(map(int, input("Enter ratings[1-5] (space seperated): ").split()))
positive_percentage(ratings)
