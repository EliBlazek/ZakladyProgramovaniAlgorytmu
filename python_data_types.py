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

########################
#STRING MANIPULATION #1#
########################
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


########################
#STRING MANIPULATION #2#
########################
def FirstHalfUpperCase(): 
    str1 = "python"
    LenStr = len(str1)//2
    str2 = str1[0:LenStr:1].upper()
    str1 = str1[LenStr:]
    print(str2 + str1)

FirstHalfUpperCase()

def RepeatFirstLetter():
    x = "python" 
    y = "git"
    z = "Hello world"
    k = "A string that will be a long scream of aaa"
    letter_switch = y
    num_repeats = len(letter_switch)
    repeatedLetter = letter_switch[:1:]
    for i in range(num_repeats): #These complicated conditions are required in order to print the characters correctly to one line. Now I am really starting to doubt if it was a good idea to refuse using Jupyter notebook.
        if i < num_repeats-1:
            print(repeatedLetter, end = "")
        else: 
            print(repeatedLetter)
    
RepeatFirstLetter()

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

def TransformDate(): #Yay! It works now! Web that helped me understand it: https://www.dotnetperls.com/truncate-python #
    origDate = '2018-11-01'
    formatedDate = origDate[5:]
    print(formatedDate)
TransformDate()

##################
#DATA STRUCTURES#
#################
def WorkWithHobbies():
    myHobbies = []
    myHobbies.append("Playing videogames")
    myHobbies.append("Making video games")
    myHobbies.append("Shitposting on Twitter dot com")
    myHobbies.append("Tinkering Linux")
    myHobbies.append("Writting bad Python code") #I should've written a function for this. But I need to do it somehow, then I can write it well.
    print(myHobbies[0]) #Print your fav hobby
    print(myHobbies[-1]) #Print your least fav hobby
    del myHobbies[-1] #Delete your least fav hobby
    print(myHobbies[-1]) #Check if your least fav hobby changed. 
WorkWithHobbies()

def WorkingWithCities():
    filler = "*"
    cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
    cities.sort()
    citiesJoined = filler.join(cities)
    print(cities)
    print(citiesJoined)

WorkingWithCities()

def ScanningZen():
    ZenOfPy = set("Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.")
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    x = alphabet.difference(ZenOfPy)
    print("These letters are not present in the Zen of Python matra:", x)
ScanningZen()

def WorkingWithDicts():
    d = {'payton':'An interpreted, object-oriented programming language'}#Broken dict
    newKey = ("python")
    oldKey = ("payton")
    if newKey != oldKey: #Method from: https://stackoverflow.com/questions/16475384/rename-a-dictionary-key 
        d[newKey] = d[oldKey]
        del d[oldKey]
    print(d)

    phonebook = {("Adam", "Novák"):("6853314")}
    print(phonebook)

    info = {('Name', 'Surname'):('John', 'Doe')} #Zdroj: Stack overflow (thread už si nepamatuju), bratr
    for key, value in info.items():
        output = str.join("_", value)
        print(output)

WorkingWithDicts()
    