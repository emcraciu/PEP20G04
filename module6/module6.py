class MyIter1():
    counter = 0

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        self.counter = self.counter + 1
        if self.counter > self.number:
            raise StopIteration
        return self.counter


class MyInt(int):

    def __iter__(self):
        return MyIter1(self)


my_int = int.__new__(MyInt, 3)
print(my_int)

for x in my_int:
    print(x)


# lambda

def my_fun(x):
    return x + 1


print(my_fun)


def my_fun_out(a):
    def my_fun(x):
        return a * x + 1

    return my_fun


my_fun_in = my_fun_out(3)
for i in range(10):
    print(my_fun_in(i))


def my_fun_out(a):
    return lambda x: a * x + 1


# lambda *args: <code>
print()
var1 = lambda x: True


def outer(func1, x):
    print(func1(x))


outer(lambda x: x + 1, 3)

for i in range(10):
    outer(lambda x: x + i, 3)

# map

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

var_map = map(lambda x: chr(96 + x), list1)
print(next(var_map))
print(list(var_map))

for i in var_map:
    print(i)

# filters
print()
list1 = [0, 1, 2]
list2 = [1, 2]

var_filter = filter(lambda x: x, list1)
for i in var_filter:
    print(i)
var_filter = filter(lambda x: x, list1)
print(list(var_filter))

var_filter = filter(lambda x: True, list1)
print(list(var_filter))

print()
list3 = ['', 0, None]
print(any(list1))
print(any(list3))

print()
print(all(list1))
print(all(list2))

# file operation

file = open('my_text', mode='r')
print(type(file))
file_content = file.read()
print(type(file_content))
print(file_content)
file.close()

file = open('my_text', mode='w')
file.write('my new text')
file.flush()
file.close()


file = open('my_text', mode='rb')
content = file.read()
print(type(content))
print(content)
file.close()

file = open('my_text', mode='wb')
my_test = b'\n{file}\x00 aa' # 00000000
file.write(my_test)
file.close()


with open('my_text', mode='wb') as file:
    my_test = b'\n{file}\x02 aa'  # 00000002
    file.write(my_test)
    print('x')

class MyClass():
    def __init__(self):
        self.__name__ = 'x'
    def __enter__(self):
        print('we are in')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('we are out')
        import time
        time.sleep(1)

my_obj = MyClass()
with my_obj as obj1:
    print(dir(obj1))
    raise Exception

