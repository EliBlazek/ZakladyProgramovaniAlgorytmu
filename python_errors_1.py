
#seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#print('My favorite season is ', seasons[4]) #This is calling a nonexistent index (because zero indexing)

#The correct way is: 
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])

# for number in range(10): #both A and B are not specified. Also number is written with capitation.
#       # use a if the number is a multiple of 3, otherwise use b    
#     if (Number % 3) == 0:       
#         message = message + a    
#     else:        
#         message = message + "b"
#     print(message)
def is_divided_by_three(number): #I have no idea what the code was suposed to do, so I rewrote it. Somehow. To do something useful. 
        # use a if the number is a multiple of 3, otherwise use b   
        a = "This number is multiple of 3" 
        b = "This number is not a multiple of three"
        if (number % 3) == 0:       
            message = a    
        else:        
            message = message + b
        print(message)

is_divided_by_three(float(input("Write down a number and I will tell you if you can divide it by three.")))

def my_name_printer():
    usr_name = input("Tell me your name: ")
    

def another_custom_division():
    my_num1 = input("Insert 1st number")
    my_num2 = input("Insert 2nd number")
    try:
        x = float(my_num1) 
        y = float(my_num2) 
    except:
        print("Please insert a number. That was not a number")
    else: 
        if y == 0:
            print("We cannot divide by zero.") #I don't know, what's better. To use 'try: x/y' or this. 
        else: 
            my_end_result = x/y
            return(my_end_result)
                

print(another_custom_division())

# year == int.input("Greetings! What is your year of origin.") #Wow. This code is horrible. It's kinda worse than mine. 

# if year <= 1900
#     print("Woah. That's the past.")
# elif year > 1900 && year < 2000:
#     print("That's totally the present.")
# elif: #Yeah. Year 2001 is not the future, right? Logic error is also error.
#     print("Far out, that's the future.")

year = int(input("Greetings! What is your year of origin."))

if year <= 1900:
    print("Woah. That's the past.")
elif year > 1900 and year < 2020:
    print("That's totally the present.")
elif year >= 2020:
    print("Far out, that's the future.")

