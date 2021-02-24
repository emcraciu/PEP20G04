# switch 2 variables using tuple
var1 = 1
var2 = 2
print('Variable 1 is:', var1, 'Variable2 is:', var2)
var1, var2 = var2, var1
print('Variable 1 is:', var1, 'Variable2 is:', var2)

var = 1
var = var + 1
print(var)

var += 1
print(var)

var /= 3
print(var)

# Bit operation

print(bin(10))

print(True & True)
print(True & False)
print(10 & 10)

print(11 | 9)
print(11 or 9)

print(9 | 11)
print(9 or 11)

print(11 >> 2)
print(~11)
print(~True)
print(~(-1))
print(~(-4))

print(11 ^ 20)
print(31 ^ 20)

print('##########')
# print(
#     chr(
#         (ord('a') ^ ord('x')) ^ ord('x')
#     )
# )

print(ord(' '))
print(ord('a') ^ ord('x'))


# print(chr(ord(' ') ^ ord('x')))
# print(chr(97))


def crypt(my_str, key):
    result = ''
    for var in my_str:
        new_chr = chr(ord(var) ^ key)
        result += new_chr
        print(result)


crypt('my_str', 128)
# crypt(123)

# # if statement
# print('############')
# def if_statement(number):
#     if number < 2:
#         print('True')
#     elif number > 3:
#         print('more then 3')
#     elif number == 3:
#         print('number is 3')
#     else:
#         print('this is else')
#
#
# if_statement(2)
#
#
# print(type("my_".__iter__()))
# my_iter = "my_".__iter__()
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# print(dir(1))
