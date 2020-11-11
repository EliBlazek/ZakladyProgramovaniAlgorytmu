#######################
#Excercise 1 - basics#
#####################
def my_custom_division(a, b):
    my_result = a/b
    print(my_result)
    
my_custom_division(4,2)

def my_custom_sum():
    usr_values=[]

    while True: 
        x = input("Put your value here. Write 'done' when you want to see sum ")
        if x == 'done':
            break
        else:   
            usr_values.append(int(x))
            continue
    result = sum(usr_values)
    print(result)

my_custom_sum()





