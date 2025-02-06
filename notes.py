# strings represent characters, names, words
name = "kammy"
# integers for WHOLE numbers
age = 14
#Boolean is true or false, typically used for evaluations
graduated = False 
#Floats for decimal
money = 4.50 
def add(x,y):
    print(x + y)
#input seeks user resonse and outputs that into the variables
#Bill value will be equal to the response of the user
bill = input("How much was the bill?")
print(bill)


#Lists which store lists of data
students = ["Kammy", "Racheal", "Dennis", "Ian"]
moneys = [1,2,3,4,5,6]
#similar to for i in range(4)
#scalable
for student in students:   
    print(student)
x = 0
for money in moneys:
    x = x + money
