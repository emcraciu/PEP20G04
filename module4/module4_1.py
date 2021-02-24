# Import for functions and variables (to be continued with classes)
import time
from time import sleep

print('Before Sleep')
time.sleep(1)
print('After Sleep')

print('Before Sleep')
sleep(1)
print('After Sleep')


import sys
print(sys.path)

import module4
module4.my_func()

from .to_import import my_func
my_func()

# Traceback

