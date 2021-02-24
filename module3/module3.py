# for

my_list = [1, 2, 3]

for i in my_list:
    print(i)
    break
else:
    print('else clause')

# type cast
my_list_to_str = str(my_list)
print(type(my_list_to_str))
print(my_list_to_str)

# my_int = 123
# my_int.__iter__()
# list(my_int)

my_str = 'abcd'
my_str.__iter__()
my_str_to_list = list(my_str)
print(my_str_to_list)

#

my_list_in_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def flatten_list(a_list_with_lists):
    pass

a = [1]
b = [2]
print(a + b)

# # loops
# print('##########')
#
# while 10 > len(a):
#     a += [2, 1]
#     if len(a) > 5:
#         print('going to break')
#         break
# else:
#     print(a)
#
# my_text = 'Give text: '
# while input(my_text) != 'hello world':
#     if len(my_text) == 11:
#         my_text = 'Give different text: '
#     elif len(my_text) == 21:
#         my_text = 'Try "hello world": '
# else:
#     print('You got it')

my_list_in_list = [1, [1, 2, [3, 11, [12, [13, 14]]]], [4, 5, 6], [7, 8, 9]]
print(isinstance(my_list_in_list, list))

def flatten_list(my_list):
    result = []
    for element in my_list:
        if isinstance(element, list):
            result = result + flatten_list(element)
        else:
            result.append(element)
    return result

print(flatten_list(my_list_in_list))

def factorial(n):
    #1*2*3...*(n-1)*n
    return n!