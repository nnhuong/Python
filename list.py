# #:tạo 1 list
# list = ["banana","apple"]
# list_1 = ["heo", "ga", "vit"]
# print(list)
# print(list_1)

# #truy cập các giá trị trong list
# my_list = [1, 2,3, 3, 3, 3, '3', True]
# print(my_list.count(3)) #count đếm có bao nhiêu số (3)

# #lập truy cập từng giá trị
# for item in my_list:
#     print(item)

# #enumerate
# presidents = ["washington", "adams", "jeff"]
# print(presidents)
# for index, presiden in enumerate(presidents):
#     print(f"Presidents # {index}, {presidents} ")


# #slicing
# my_list = [1, 2,'3', True]
# print(my_list[-1]) # truy cập giá trị cuối cùng

# my_list_5 = [1,2,3,4,5]
# print(my_list_5[::3])



# my_list_1 = [1, 2, 3, '4', True]
# print(my_list_1 + [100, "Code"])
# print(my_list_1)
# #hàm sẵn có
# print(my_list_1.append(100)) #append dùng để add 1 giá trị vào trong list
# print(my_list_1.extend([100, "code"])) #extend dùng để add từ 2 giá trị trở lên vào list
# print(my_list_1)
# print(my_list_1.extend([200, 300,]))
# print(my_list_1)

#remove các phần tử
# my_list_2 = [1, 2, 3, 4] #xoá giá trị cuối cùng
# print(my_list_2.pop(1)) #xoá giá trị số 1
# print(my_list_2)

#sorting: sắp xếp
# my_list = [1,5,6,3, 8,0]
# my_list.sort()
# print(my_list)
# sorted(my_list)

# print(sorted(my_list))

#thao tác 
my_list = [1,2,3,7,9]
print(min(my_list))
print(max(my_list))