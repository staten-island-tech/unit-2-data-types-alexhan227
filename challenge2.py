bill = int(input("How much was the bill?: "))
tip = input("Was the service bad, okay, good, or great?: ")
badtip = (bill * 0)
okaytip = (bill * .15)
goodtip = (bill * .20)
greattip = (bill * .25)

# asks if want to tip
tipquestion1 = input("Do you want to tip? (yes or no): ")

# If they say yes, ask about the service rating
if tipquestion1 == "yes":
    if tip == "okay":
        print(f"Your tip is: ${okaytip:.2f}")
        #individuallizing the qeustion allows the code to fufuill ONE conditional at a time
    elif tip == "good":
        print(f"Your tip is: ${goodtip:.2f}")
    elif tip == "great":
        print(f"Your tip is: ${greattip:.2f}")
    elif tip == "bad":
        print(f"Your tip is: ${badtip:.2f}")
elif tipquestion1 == "no":
    print("Have a nice day, come again!")