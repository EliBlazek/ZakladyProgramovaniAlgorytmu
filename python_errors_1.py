
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

for number in range(10): #fixed
    # use a if the number is a multiple of 3, otherwise use b   
    a = "This number is multiple of 3" 
    b = "This number is not a multiple of three"
    if (number % 3) == 0:       
        message = message + a    
    else:        
        message = message + b
    print(message)

def another_custom_division():
    while True:
        my_num1 = input("Insert 1st number")
        my_num2 = input("Insert 2nd number")
        try:
            x = float(my_num1) 
            y = float(my_num2) 
        except:
            print("Please insert a number. That was not a number")
            continue
        else: 
            if y == 0:
                print("We cannot divide by zero.") #I don't know, what's better. To use 'try: x/y' or this. 
                continue
            else: 
                my_end_result = x/y
                return(my_end_result)
            break
                

print(another_custom_division())

