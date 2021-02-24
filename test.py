print(__name__)

import module4
module4.my_func()
print(module4.var1)

from module4 import my_func
my_func()