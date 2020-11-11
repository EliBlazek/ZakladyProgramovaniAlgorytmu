my_lipsum_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum consectetur nibh ex, quis pretium risus faucibus eu. Ut placerat lorem vel sapien vestibulum consequat. Aliquam sit amet lacinia turpis, eget congue orci. Nulla faucibus, massa sed ultricies consectetur, arcu massa aliquam ante, id egestas ligula ligula ornare nunc. Mauris euismod, lorem non maximus sagittis, sapien justo. "

def num_of_letters(a):
    num_upper = sum(1 for letter in a if letter.isupper()) #A thread that helped me: https://stackoverflow.com/questions/18129830/count-the-uppercase-letters-in-a-string-with-python 
    num_lower = len(a) - num_upper

    print("input: ",a)
    print("Upper case: ", num_upper)
    print("Lower case: ",num_lower)

    

num_of_letters(my_lipsum_str) 
#Generated witl lipsum.com