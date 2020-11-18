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