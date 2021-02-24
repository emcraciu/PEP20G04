# variables

# Global

var1 = 1


def my_func():
    print(var1)


my_func()


# Local

def my_func():
    var2 = 2
    print(var2)


my_func()


def my_func():
    var1 = 2
    print(var1)


my_func()


def my_func3():
    def my_func2():
        var1 = 3

        def my_func():
            nonlocal var1
            var1 = 2

        print(var1)
        my_func()

    my_func2()
    print(var1)


# dict

my_dict = {'casa': 'place to sleep'}
my_dict2 = {(1,): '1', 1: '1', 1: '2'}
print(my_dict, my_dict2)

for i in my_dict2:
    print(i, type(i))

for i in my_dict2.keys():
    print(i, type(i))

for i in my_dict2.values():
    print(i, type(i))

print('#############')
for key, value in my_dict2.items():
    print('key is', key, type(key))
    print('value is', value, type(value))

my_dict2.update(number='3')
print(my_dict2)
my_dict2.update({3: '3'})
print(my_dict2)

print(my_dict2.get('number'))
print(my_dict2.get(3))

print('poped value', my_dict2.pop('number'))
print(my_dict2)

mag1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
mag2 = {'mere': 11, 'pere': 15, 'prune': 6}
mag3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
lista_de_magazine = [mag1, mag2, mag3]
lista_de_cumparaturi = {'mere': 2, 'pere': 3, 'prune': 6}

#def best_buy():


# print('a', 'b', sep='@', end='5')
#
#
# def my_print(sep='my_sep', end='my_end'):
#     print(sep)
#     print(end)
