# sorted_by_second = sorted(['hi', 'hello', 'you', 'coder'],  key = lambda el:el[1])
# print(sorted_by_second)

# sorted([{'name': 'coder', 'age': 15},{'name': 'Andy', 'age': 18}, {'name': 'zoey', 'age': 55}])
# print(sorted)
# sorted_list = sorted([{'name': 'coder', 'age': 15}, {'name': 'Andy', 'age': 18}, {'name': 'zoey', 'age': 55}], key=lambda x: x['age'])
# print(sorted_list)

#mảng 2 chiều
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(matrix[1][2])
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])
        
