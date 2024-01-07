def varibleLengthArgExpamle(a,b, *args):
    print(a, b)
    for arg in args:
        print(arg)
        
    def main():
        varibleLengthArgExpamle('a', 'b', 'hello', 1,2,3)
        main()

# def varibleLengthArgExpamle(a, b, *args):
#     print(a, b)
#     for arg in args:
#         print(arg)

# def main():
#     varibleLengthArgExpamle('a', 'b', 'hello', 1, 2, 3)

# # Call the main function to execute the code inside it
# main()

#Hàm lambda
#anonymous function : hàm ần danh
# codexplore = lambda so: so +69

# def codexplore1(so):
#     return so + 69
# print(codexplore(5))

# code = lambda x,y,z: x+y-z
# print(code(5,6,4))

coordinate2D = [(6,9), (9,6), (-1,3), (2,10)]
print(sorted(coordinate2D))
print(sorted(coordinate2D, key = lambda point: point[1]))

number_list = [5,3,-2,4,1,-1,-3,4,5]
print(sorted(number_list))
#viet hoa cac chu cai dau tien
list_keyword = ["codexplore", "welcome", "cacban"]
print (list(map(lambda x: x.title(), list_keyword)))

new_list = [keyword.title()for keyword in list_keyword]
print(new_list)

#filter(func, seq) loc
number_list = [1,2,3,4,5,6,7,8,9,10]
print (list(filter(lambda x: x%2!=0, number_list)))

new_list = [x for x in number_list if x%2!=0]
print(new_list)

#reduce function
from functools import reduce
sequence = [1,3,5,9,6,2,8]
print(reduce(lambda a,b: a+b,sequence))
print(reduce(lambda a,b: a if a>b else b, sequence))

