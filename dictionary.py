# my_dictionary = {"name": "CodeXplore", "content": "Program Youtube Channel"}
# print(my_dictionary)

# my_dict = dict(name="CodeXplore", content="Program Youtube Channel")
# print(my_dict)

# #access items
# content_in_dict = my_dict["content"]
# print(content_in_dict)

# if "name" in my_dict:
#     print(my_dict["name"])
# else:
#     print("No key found")

my_dictionary = {"name": "CodeXlore", "content": "Programming Youtube Channel"}
print(my_dictionary)

my_dict = dict(name="CodeXlore", content="Programming Youtube Channel")  # Sửa tên khóa "name" ở đây
print(my_dict)

# Truy cập các mục
content_in_dict = my_dict["content"]
print(content_in_dict)

if "name" in my_dict:
    print(my_dict["name"])
else:
    print("No key found")

my_dict ["email"] = "codexplore@gmail.com"
print (my_dict)

del my_dict["name"]

my_dict.pop("content")
print(my_dict)

my_dict["age"] = 25
print(my_dict)

for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key,value)

#is unique
str = "abcd" #unique
print(str)
str1 = "aabbcc" #not unique
print (str1)


def unique(str):
    char_set = {}

    for char in str:
        # print(char)
        if char in char_set:
            return False
        char_set[char] = True
        return True
    
class Test(unittest.TestCase):
        dataT = [('abcd'), ('s484882'), ('')]
if __name__ == "__main__":
    str = "abcccggggd"
    print(unique(str))

import unittest