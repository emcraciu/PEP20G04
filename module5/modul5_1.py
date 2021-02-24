# # traceback
#
# try:
#     raise ZeroDivisionError('my message', 'my_arg 2')
#     #raise Exception()
#     #_2 / 0
#     2/0
#     print('no exception')
#
# except ZeroDivisionError as error:
#     print('exception 0')
# except NameError:
#     print('exception 1')
# except Exception:
#     print('exception -1')
# else:
#     print('no error')
#
# x = ''.join(['123', 'abc'])
# print(x)
#
# def add_strings(my_string_list: list):
#     pass
#
# add_strings('abc')
#
#
# class MyException(Exception):
#     def __init__(self, *args):
#         super().__init__(*args)
#
# try:
#     raise MyException('new exception message')
# except MyException as error:
#     print(error.args[0])
#
#
# # assert
#
# assert True, 'this will not be printed'
#
# # assert False, 'this will be printed'
# raise AssertionError('this will be printed')

def fix_zero_division():
    while True:
        try:
            number = int(input('Number: '))
            divider = int(input('Divider: '))
        except Exception:
            print('Bad divider value')
            continue
        try:
            result = number/divider
            assert result
        except ZeroDivisionError:
            return 99999999999
        except AssertionError:
            continue
        else:
            return result

print(fix_zero_division())