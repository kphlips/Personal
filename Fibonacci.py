a = 0 #The first of a pair of Fibonacci numbers
b = 1 # The second
temp = 0 # Temporary variable for storing the next number in the sequence
limit = int(input("Enter the maximum Fibonacci number: ")) # Record user input
while limit <0:
	limit = int(input("Must be a positive number. Enter the maximum Fibonacci number: "))
while a <= limit: #Ensures that the number printed will not exceed the limit
        print(a)
        temp = a + b # Creating the next number in the sequence
        a = b #The new first numnber becomes the old second number
        b = temp #The new second number is the sum of the old two numbers
