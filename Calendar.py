#Known Errors: Does not provide a correct answer when going backwards in time

numDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
           7:31, 8:31, 9:30, 10:31, 11:30, 12:31} #Dictionary of days per month

error= "Invalid format or date, please try again: " #Error message printed

def check (x): #Method that verifies the correct format and limit of the day and month
    if x.isupper() or x.islower():
        return False
    if x.find("/") != 2 or x.rfind("/") != 5:
        return False
    if int(x[0:2]) < 1 or int(x[0:2]) > 12:
        return False
    if int(x[3:5]) < 1 or int(x[3:5]) > numDays[int(x[0:2])]:
        return False
    if len(x) < 7:
        return False
    return True

date1 = input("Enter the first date in the format MM/DD/YYYY (ex. 12/25/2009):") #Asks for user input

while not check(date1): #Will continue to ask until proper format is input for first date
        date1 = input(error)
        
date2 = input("Enter the second date in the format MM/DD/YYYY (ex. 12/31/3782):") #Prompt for second date

while not check(date2): #Repeatedly asks for correct format of second number
        date2 = input(error)

d1 = int(date1[3:5]) #The following lines splice the string input into integer values for day month and year
m1 = int(date1[0:2])
y1 = int(date1[6:])

d2 = int(date2[3:5])
m2 = int(date2[0:2])
y2 = int(date2[6:])

def leap(x): #Takes in a year value and returns a boolean representing if a year will leap or not
    if x % 400 == 0: return True
    elif x % 100 == 0: return False
    elif x % 4 == 0: return True
    else: return False;

def count (d1,m1,y1,d2,m2,y2): #Day counter method
    sum = 0    #Sum of days to be returned
    if y2 == y1 and m2 == m1: # If the month and day are the same
        return d2-d1
    if y2 == y1: #If the years are the same
        sum += d2
        for m in range (m1,m2):
            if leap(y1): numDays[2] = 29 #When this is seen, it changes the February day count during a leap year
            if m == m1:
                sum += numDays[m] - d1
                continue
            sum += numDays[m]
    else: #If the month and year are not the same...
        sum += d2 #The days of the last incomplete month
        for y in range (y1, y2 +1):
            if y == y1: #Counts the days in the first incomplete year
                for m in range (m1,13):
                    if m == m1:
                        if leap(y): numDays[2] = 29
                        else: numDays[2] = 28
                        sum += numDays[m] - d1
                        continue
                    else:
                        if leap(y): numDays[2] = 29
                        else: numDays[2] = 28
                        sum += numDays[m]
            if y == y2: #Counts the days in the last incomplete year
                for m in range (1,m2):
                    if leap(y): numDays[2] = 29
                    else: numDays[2] = 28
                    sum += numDays[m]
            if (y != y1 and y != y2): #Counts the intermediate complete years
                for m in range (1,13):
                    if leap(y): numDays[2] = 29
                    else: numDays[2] = 28
                    sum += numDays[m]
    return sum
    


result = count(d1,m1,y1,d2,m2,y2)
if result == 1:
    print("\nThere is {} day between {} and {}".format(result,date1,date2))
else:
    print("\nThere are {} days between {} and {}".format(result,date1,date2))    