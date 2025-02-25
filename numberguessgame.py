import random #imports the "random" code
x = random.randint(1,10) #makes the limits between 1 and 10 to pick a random number

print (x) #delete later, only used to speed up testing

guess = int(input("Guess the number: ")) #calls the user input "guess" and converts it into an integer for consistency

guesses = [] #defines guesses as a list of the "guess" that the user inputs, DONT PUT ANYTHING IN THE LIST BEFOREHAND KEEP IT EMPTY

def guess_history (guess): #defines guess_history as a list that each "guess" adds to
     guesses.append(guess) #tacks on each guess to the end
     print ("used guesses", guesses) #prints the "used guesses text" followed by the guesses


guess_history(guess) #the initial guess the user puts
while guess != (x): # while the guess IS NOT EQUAl to (x) the loop is in effect
        if guess > (x): #if the guess is smaller than (x)
            print ("Wrong! Too High, Guess Again: ") #print this
        elif guess < (x): # if guess is greater than (x)
            print ("Wrong! Too Low, Guess Again: ") #print this

        guess = int(input()) #takes in another input by the user until the loop ends
        guess_history(guess) #prints the list in order for the user to see used guesses, the second and all the following inputs
        

print ("correct!") #when the user finally guesses the right answer, breaks the loop and prints this text

#Code ensues as follows- imports random and creates random number from 1 to 10
#defines the "guess" and an input the user inputs and establishes as a integer
#it defines guesses as an empty list
#def function "guess_history" to track and print guesses, takes the empty list "guesses"
#and adds the "guess" inputs from the user
#then runs guess history in order register the first guess
#runs the while loop
#when loop breaks prints correct