def fun1(a, b,c):
    def fun2(x):
        return x+a+b+c
    return fun2

f = fun1(1,2,3)
print(f(4))