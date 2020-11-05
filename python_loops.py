def your_name_list():
    names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef','Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav','Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal','Lenka', 'Katerina']
    my_name = input("Whats your name? ")
    if my_name in names_list:
        print(" Hey, that name is pretty ordinary. I mean... it's a cool name, but not that special.")
    else: 
        print(" Wow. Nice unique name, queen. ") #Replace with "king" or "monarch" if needed

your_name_list()

def loopy_fruit():
    my_fruits = ['green apples', 'cherries', 'pineapple on pizza', 'peaches', 'plums', 'strawberries']
    for fruit in my_fruits:
        print("I like " + fruit)

loopy_fruit()

def spelling_alphabet():
    #Řešení inspirováno: https://towardsdatascience.com/simple-morse-code-decoder-in-python-39f6db635af2
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta','e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india','j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike','n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec','r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform','v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee','z':'zulu'}
    
    usr_msg = list(input("Please insert your name. I will spell it for you "))
    spelled_msg = []
    for letter in range (0, len(usr_msg)):
        if usr_msg[letter] in d.keys():
            spelled_msg.append(d[usr_msg[letter]])#I dont get this. Like... at all. Maybe Im just tired, but I dont get dicts. 
            #It almost works, but I honesly have no idea how. I'll look more into it on the weekend. 
    print(spelled_msg)
        


spelling_alphabet()

def shopping_list(): #The program in the excercise didnt make much sense to me. So I rewrite it in order to be useful. Now you can actually make your own shopping lists with it. 
    my_shopping = []
    while True: 
        shopping_item = input("What do you wanna buy? (or type 'Done' to quit)")
        if shopping_item == "Done":
            print("Here is your shopping list, queen: ") #I love writing programs that validate me
            for item in my_shopping:
                print(item)
            break
        elif shopping_item in my_shopping:
            print("Already on the list")
        else: 
            my_shopping.append(shopping_item)

shopping_list()

def more_fun_with_lists(): 
    fav_nums = [6, 7, 14, 21, 121]
    for number in fav_nums:
        print(number, "is my favourite number")
    
    phat_nums = [] #Thread, která mi pomohla: https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number 
    for number in fav_nums:
        phat_nums.append(number * number)
    for number in phat_nums:
        print(number, end = " ")
    print("") 

more_fun_with_lists()

def count_letters_in_string():
    seq = 'ttacgcacacttattactgcacaggttcgttaagtgcacatgcatcttgcattcaatagaggggt' #Random sequence generator: https://www.bioinformatics.org/sms2/random_dna.html 
    count = 0
    for letter in seq:
        if letter == 'a':
            count = count +1
    print("Adenin in a sequence: ",count)

count_letters_in_string()
    
def triple_points_dict(): #I learned about it from: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension 
    scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
    triple_scores = {key:value*3 for (key, value) in scores.items()}
    print(triple_scores)

triple_points_dict()

    