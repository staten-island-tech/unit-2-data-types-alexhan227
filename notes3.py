#loop from 2 to Y for i in range(2,15)
#if factor == true add to list
#loop from 2 to Y for i in range(2,15)
# if x isFactor and y isFactor then add to list

isRich = True
is21 = True

def canGamble(isRich, is21):
    if isRich == True and is21 == True:
        print("Let it ride!")
    elif isRich == False and is21 == True:
        print("you are too poor, get out")
    elif isRich ==  False or is21 == False:
        print("you can't play")
        