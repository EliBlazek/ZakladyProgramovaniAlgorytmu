###################
#Lambda functions#
#################

#Hlavní zdroj inspirace pro mě bylo tohle video: https://www.youtube.com/watch?v=25ovCm9jKfA 
#Autoři si najali profesionální dabérku a herečku, která v sérii o učení Pythonu ztvárnila AI a nahrála všechny poznámky. 
#Je to vtipné, informativní a krátké. A geniální.

big_test_list = [3,4,5,6,8,5]
small_test_list = [134, 51, 16]

g = lambda x : print("smol") if len(x) < 5 else print("Big")

g(big_test_list)
g(small_test_list)


