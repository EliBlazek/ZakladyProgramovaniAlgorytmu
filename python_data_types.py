##############
#KING PROBLEM#
##############
def HeritageMoney():
    money = 1256983 
    num_kids = 28
    money_remaining = money%num_kids 
    return (money_remaining)
print("After giving out an even cut to all of his kids, the king will be left with", HeritageMoney(), "golden coins.")

##################
#LOGIC EVALUATION#
##################
LogicalSentense1 = "Remainder after division of 12^52 by 15 is less than  8 or 3^5  is more than 100"
LogicalSentense2 = "5 times 3^3 is not equal to 900 divided by 75"

def LogicOp1():
    x = (12**52)%15
    y = (3**5)
    eval= x < 8 or y > 100
    return (eval)

def LogicOp2():
    x = 5 * (3**3)
    y = 900/75
    eval = x != y
    return(eval)
print(LogicalSentense1, "is", LogicOp1())
print("And", LogicalSentense2, "is", LogicOp2())

#######################
#STRING MANIPULATION 1#
#######################
def TwoStringsToOne():
    x = '[[]]'
    x1 = x[0:2]
    x2 = x[2:4]
    y = 'PYTHON'
    result_str = x1 + y + x2
    print(result_str) #This may be the worst possibne solution to this problem. But it kinda works!

TwoStringsToOne()

def OneFromAnother():
    x = "Python"
    y = "Perl"

    MutatedStr1 = x[4:6]*4
    MutatedStr2 = y[2]*6
    print(MutatedStr1, MutatedStr2)

OneFromAnother()

#######################
#String manipulation 2#
#######################
def FirstHalfUpperCase(): 
    x = "python"
    upperPart = x[0:len(x)//2].upper
    #lowerPart = x[len(x)//2:]
    print(upperPart)

FirstHalfUpperCase()
    


############
#Fix errors#
############

print(7 + 3 * 2) #Works well - order of operation gives the correct answer - 13
print('7' + str(3*2) ) #It will calcule the second expression and then concat the two strings - 76
print('7' + '3 * 2') #This just concats the strings together - 73 * 2
#print('7' + 3 * 2) - This would cause runtime error. You cannot combine data types THAT freely. 
#But if this was JS, it would just calculate the numbers... in some weird way. Because JS is weird. 

##################
#Formated strings#
##################

def printHobbyA(): #Why is camel code bad? (refering back to your presentation. I like camel code...)
    hobby = "writting bad Python code"
    x = f"My hobby is {hobby}"
    print(x)
    #I think that for this type of assignment, f strings are superior.
printHobbyA()

def printHobbyB():
    hobby = "writting bad Python code"
    x = "My hobby is {0}.".format(hobby)
    print(x)
    #And this is the requested solution.
printHobbyB()

def TransformDate(): #######DOESNT WORK. NEEDS FIXING############
    origDate = '2018-11-01'
    formatedDate = '{:>5}'.format(origDate)
    print(formatedDate)
TransformDate()