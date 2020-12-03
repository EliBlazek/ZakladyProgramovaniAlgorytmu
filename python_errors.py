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

for number in range(10): #both A and B are not specified. Also number is written with capitation.
      # use a if the number is a multiple of 3, otherwise use b   
    a = "This number is a multiple of 3" 
    b = "This number is not a multiple of three"
    if (number % 3) == 0:       
        message = message + a    
    else:        
        message = message + b
    print(message)

    