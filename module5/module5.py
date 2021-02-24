class MyClass:
    pass


print(__name__)
my_object = MyClass()

print(type(my_object))

print(type(''))


class MyClass2():
    def __init__(self):
        print('Constructor')

    def test(self):
        print('NotConstructor')


my_object = MyClass2()

print(dir(''))


class MyClass3():
    attribute1 = 10

    def __init__(self):
        print(self.attribute1)
        print('Constructor')

    def test(self):
        print('NotConstructor')


print(MyClass3.attribute1)
my_object = MyClass3()
print(my_object.attribute1)

print(MyClass3)
print(my_object)

print(dir(''))

MyClass3.test(MyClass3())
my_object.test()

class PhoneBase(object):
    name = None
    number = None
    # def __init__(self):
    #     print(type(self))
    #     self.name = input('name: ')
    #     self.number = input('number: ')

# my_phone = PhoneBase()
# print(my_phone.name)
# print(my_phone.number)

class TouchPhone(PhoneBase):
    screen = 'RGB'
    theme = 'blue_theme'

    def change_theme(self, theme):
        self.theme = theme


# my_touch_phone = TouchPhone()
# my_touch_phone.change_theme('red_theme')
# print(my_touch_phone.theme)

class KeyPhone(PhoneBase):
    key = 12
    color = 'blue'

    def __init__(self):
        super(KeyPhone, self).__init__()
        print(type(self))
        self.keys = 'red'

    def change_color(self, color):
        self.color = color


my_key_phone = KeyPhone()
# print(my_key_phone.name)
# print(my_key_phone.name)
# print(my_key_phone.keys)
# print(my_key_phone.color)
# my_key_phone.change_color('red')
# print(my_key_phone.color)