#python primitive data types
#int = 2,
#float = 1.25,
#string="Name",
#Boolean= True
#type function to get the data type of the variable

print("welcome to the Tip Calculator!")
bill = float(input("What was the total bill ? $"))
tip = int(input("How much tip would you like to give ? 10, 12, 15 ? "))
divide = int(input("How many people are there ? " ))
output = (bill + tip)/divide
print(f"Each person has to pay ${output}")