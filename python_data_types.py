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
    y = 'PYTHON'

def OneFromAnother():
    x = "Python"
    y = "Perl"

    MutatedStr1 = print(x[4:6]*4)
    MutatedStr2 = print(y[2]*6)
    return(MutatedStr1, MutatedStr2)

print(OneFromAnother())



