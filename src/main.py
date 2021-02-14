# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from itertools import chain
from itertools import zip_longest
from itertools import permutations
from itertools import combinations
from itertools import islice
from itertools import tee
# use of enumerate, zip
from functools import partial
from functools import wraps
from collections import defaultdict
from collections import Counter
from collections import deque
from queue import Queue
import _thread as thread
from threading import Thread, Lock
from timeit import Timer
import time
from pprint import pprint
import copy
import os
import sys
from sys import getsizeof
from pathlib import Path
import re
import contextlib
from contextlib import contextmanager

# enumerate, zip are built-in
# operator overloading and intercepting calls with
# init, repr, str, add, radd, iadd, getattr, getattribute, hasattr, call
# recursion and importance of super,

# a = [1, 2, 3, 4, 5, 6]
# b = [6, 67, 8, 9]

# for _ in a+b:
#     print(_)
#
# for _ in chain(a, b):
#     print(_)

# c = [(1, 2, 3), (3, 4, 5)]


# for _ in chain(c):
#     print(_)
# for _ in chain.from_iterable(c):
#     print(_)

# for _ in zip(a, b):  # zip is a built-in function
#     print(_)

# for _ in zip_longest(a, b, fillvalue="test"):
#     print(_)
# print(dict(zip_longest(a, b)))
# print(dict(zip(a, b)))

# colours = ["red", "blue", "yellow"]
#
# for index, colour in enumerate(colours, 1):  # enumerate is a built-in function
#     print(index, colour)
#
# colours = [("red", 45), ("blue", 32), ("yellow", 47)]
#
# for a, (b, c) in enumerate(colours):
#     print(a, b, c)


# colours = ["red", "blue", "yellow"]
# for p in permutations(colours, 1):
#     print(p)
# print("-------------------------")
# for p in permutations(colours, 2):
#     print(p)
# print("-------------------------")
# for p in combinations(colours, 2):
#     print(p)
# print("-------------------------")
# for p in combinations(colours, 3):
#     print(p)
# print("-------------------------")


# for n in islice(range(100), 10, 70, 12):
#     print(n, sep="*", end=" ")

#
# x = range(10)
# a, b = tee(x, 2)


# class History:
#
#     def __init__(self, lines, history_length=10):
#         self.lines = lines
#         self.history = deque(maxlen=history_length)
#
#     def __iter__(self):
#         for line_num, line in enumerate(self.lines, 1):
#             self.history.append((line_num, line))
#             yield line
#
# with open('main.py', 'r') as f:
#     lines = History(f)
#     for line in lines:
#         if 'qqq' in line:
#             for line_num, hist_line in lines.history:
#                 print(line_num, hist_line)


#
# iterable = range(5)
# candle = deque(iterable)
#
#
# def burn(direction, next_source):
#     while True:
#         try:
#             next = next_source()
#         except IndexError:
#             break
#         else:
#             print(direction, next)
#             time.sleep(1)
#     print(direction, 'done!')
#
#
# left = Thread(target=burn, args=('Left', candle.popleft))
# right = Thread(target=burn, args=('Right', candle.pop))
#
#
# def start(l,r):
#     l.start()
#     r.start()
#
#
# start(left, right)
# print(Timer(partial(start, left, right)).timeit(1)*1000)


#
#
# def tail(filename, n=10):
#     with open(filename) as f:
#         return deque(f, n)
#
#
# with open("file1.txt", 'w') as f:
#     for i in range(100):
#         f.write(f"This is line number: {i}. \n")
#
# pprint(tail('file1.txt'))

# dq = deque(range(1000))
# _list = list(range(1000))
#
#
# def rotate_deque(dq):
#     for i in range(1000):
#         dq.rotate()
#
#
# def rotate_list(_list):
#     for i in range(1000):
#         _list = _list[-i:] + _list[:-i]
#
#
# deque_timer = Timer(partial(rotate_deque, dq))
# list_timer = Timer(partial(rotate_list, _list))
#
# print(f'deque (10 x 1000 rotations): {deque_timer.timeit(10) * 1000} ms')
# print(f'deque (10 x 1000 rotations): {list_timer.timeit(10) * 1000} ms')
#

#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# olivia = Person('olivia')
# list_of_names = ['Daisy', 'Isobel', 'Sarah', olivia]
# shallow_copy = copy.copy(list_of_names)
# deep_copy = copy.deepcopy(list_of_names)
# slicing = list_of_names[:]
# list_copy_method = list_of_names.copy()
# asterisk = [*list_of_names]
# list_func = list(list_of_names)
# other = list_of_names * 2
# another = list_of_names + []
#
# olivia.name = "Olivia"
#
# print('Original ', list_of_names)
# print('Shallow Copy', shallow_copy)
# print('Deep Copy ', deep_copy)
# print('Slicing ', slicing)
# print('List .copy() method ', list_copy_method)
# print('Iterable unpacking ', asterisk)
# print('list(old_list)', list_func)
# print('old_list * 2', other)
# print('old_list + []', another)


# class SlottedPlanet:
#     __slots__ = ['cities', 'rivers']
#     def __init__(self, cities, rivers):
#         self.cities = cities
#         self.rivers = rivers
#
# slotted_earth = SlottedPlanet(['Delhi', 'Bombay'], ['Gnaga', 'Yamuna'])
#
# class Planet:
#     def __init__(self, cities, rivers):
#         self.cities = cities
#         self.rivers = rivers
#
# earth = Planet(['Delhi', 'Bombay'], ['Gnaga', 'Yamuna'])
#
# print(len(dir(slotted_earth)))
# print(len(dir(earth)))
#
# print(getsizeof(slotted_earth))
# print(getsizeof(earth))
# print(getsizeof(earth.__dict__))

#  slotted instances are smaller in memory footprint than non-slotted, can same lot of memory with that
#  access to slotted instances are faster than non-slotted


# def counter(id, count):
#     for i in range(count):
#         print(f'[{id}] ---> {i}\n')
#         time.sleep(1)


# for i in range(5):
#     counter(i, 5)

# for i in range(5):
#     thread.start_new_thread(counter, (i, 5))
#
# mutex = thread.allocate_lock()
#
#
# def counter2(id, count):
#     for i in range(count):
#         mutex.acquire()
#         print(f'[{id}] ---> {i}\n')
#         time.sleep(1)
#         mutex.release()
#
#
# for i in range(5):
#     thread.start_new_thread(counter2, (i, 5))
#
#
# stdoutmutex = thread.allocate_lock()
# exitmutexes = [thread.allocate_lock() for i in range(10)]
#
# def counter3(id, count):
#     for i in range(count):
#         stdoutmutex.acquire()
#         print(f'[{id}] ---> {i}\n')
#         stdoutmutex.release()
#     exitmutexes[id].acquire()
#
# for i in range(10):
#     thread.start_new_thread(counter3, (i, 100))
#
# for mutex in exitmutexes:
#     while not mutex.locked():
#         pass


# class LearnerClass(Thread):
#     def __init__(self, id, count, mutex):
#         self.id = id
#         self.count = count
#         self.mutex = mutex
#         super().__init__()
#
#     def run(self):
#         for i in range(self.count):
#             with self.mutex:
#                 print(f'[{self.id}] ---> {i}')
#
# stdoutmutex = Lock()
# threads = []
#
# for i in range(10):
#     thread = LearnerClass(i, 100, stdoutmutex)
#     thread.start()
#     threads.append(thread)


# blocks the calling thread(parent thread),
# until the thread whose join method is called terminates
# can set a timeout for waiting, by passing argument
# for thread in threads:
#     thread.join()

# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#         time.sleep(0.1)
#
# t = Thread(target=countdown, args=(10,))
# t.start()
#
# time.sleep(2)
# if t.is_alive():
#     print('Still Running')
# else:
#     print('Complete')


# def producer(out_queue, n):
#     while True:
#         for i in range(10):
#             data = n * i
#             out_queue.put(data)
#             time.sleep(0.2)
#
#
# def consumer(in_queue):
#     while True:
#         data = in_queue.get()
#         print(data)
#         print(in_queue)
#         time.sleep(0.1)
#
#
# q = Queue()
# t1 = Thread(target=producer, args=(q, 1))
# t2 = Thread(target=consumer, args=(q,))
# t1.start();t2.start()

# lexical scoping
# LEGB rule - Local Enclosing Global and Built-In

# x = 10
#
#
# def adder(y):
#     return y + x
#
#
# print(adder(19))
#
#
# def adder2(y):
#     global x
#     x = 20
#     return x+y
#
#
# print(adder2(19))
# print(x)

# Are global variables bad practice
# this is a bad use of global variables

# def first_func():
#     global x
#     x = 0
#
#
# ####
#
#
# def second_func():
#     global x
#     x = 1000
#
#
# first_func()
# second_func()
# first_func()
# print(x)

# we can only know the value of x at any point in code if we know
# which among the two is the most recently called function


# python allows arbitrary nesting of function definition
# Scope - which variables can be seen in which parts of code
# scope --> closures --> namespaces --> oop

# which value will the x inside of nested takes?
# LEGB rule - Local --> Enclosing --> Global --> Built-In rule
# Closures are a product of code and environment
# we can't see local x, no assignment to variable x inside "nested" definition
# By LEGB rule, the next place, python interpreter looks, is in any enclosing scopes
# an enclosing scope is the function definition "first" where nested is defined
# if not found, then global score where x is defined
# if not found, then it checks if x is a built-in object
# if not found, then throws Exception

# x = 1
#
#
# def first():
#     x = 2
#
#     def nested():
#         # x = 3
#         print(x)
#
#     nested()
#
#
# first()

# dunder variables, __name__ variable

# run first() function when this file is run directly from terminal
# if __name__ == '__main__':
#
#     first()

# __init__.py file in a package can be used to expose the API the package wishes to provide
# to “flatten” the needed references from the submodules and subpackage

# package/
#   __init__.py
#   module_1.py
#   module_2.py
#   sub_package_1/
#       __init__.py
#       sub_module_1.py
#       sub_module_2.py

# if __init__.py files is empty, when we do 'import package', or 'import package.sub_package'
# with dir(package) or dir(package.sub_package) command, we can't see any of our sub-modules

# so to import sub_module_1.py, and use functions there, we need to do
# import package.sub_package_1.sub_module_1
# package.sub_package_1.sub_module_1.func_in_sub(1, 2)

# becoming unwieldy for end-user

# to overcome, we create a patch work with top level __init__.py file,

# in that file
# from .sub_package_1.sub_module_1 import func_in_sub
# from .sub_package_1.sub_module_1 import *

# and with in sub_module we can define exactly which functions to export
# by defining list of strings in __all__ attribute of the module file

# __all__ = ['func_in_sub']

# and in top level __init__.py file
# __all__ = (sub_package_1.sub_module_1.__all__ + sub_package_2.sub_module_2.__all__)

# with the above code, in client files, where we use the package, we can do
# from package import *
# to get all the functions we need from the package

# thus __init__.py is used to 'flatten' references references to objects in packages


# below code creates a class object and assigns it a name
# name of this class object is 'Tweet'
# think of it like a 'factory'
# providing default behaviour and able to create objects in its image with invocation Tweet()
# any changes made to objects "produced" by factory won't propagate back up to the factory

# class Tweet:
#     pass
#
#
# a = Tweet()
# b = Tweet()
# instance objects inherit class attributes and
# get their own namespace to add and access attributes

# a.message = "140 characters"
# b.message = "different message"


# dunder methods are special hooks in python
# these methods are called automatically at certain times(ex: after object creation),
# classes can override most of these, we will focus on __init__() method

# whenever we call class object, instance object is first created with __new__ method
# and then any attributes are initialised with __init__ method
# it's is more of "initializer" method than a "constructor" method


# class Tweet:
#     # whenever the class object is called, Tweet(),
#     # instance created is passed as first argument to __init__ method
#     # self refers to the particular instance, it can be self, or it can by any placeholder name
#     # self is not "keyword", in this particular context(init method)
#     def __init__(a):
#         a.k = "message"
#
#     # can be called from instance namespace
#     # can be called from class namespace, passing first argument as some instance of class
#     def print_k(b):
#         print(b.k)
#
#     # only available through class namespace
#     # won't have access to instance attributes, vive-versa, instances can't use this method
#     def print_c():
#         print("class namespace method")
#
#     # can be called from instance namespace
#     # can be called from class namespace, passing first argument as some instance of class
#     def print_d(d):
#         print(d.k)


# whenever the class object is called, the instance is passed as first argument to init method
# t = Tweet()
# print(t.k)
# t.print_k()
# Tweet.print_k(t)

# like above, append can called from namespace of a list instance or list class namespace
# a = [1, 2, 3]
# a.append(13)
# list.append(a, 15)
# print(a)

# with open('file1.txt') as f:
#     for line in f:
#         if line.strip() == '******':
#             break
#     for line in f:
#         if line.strip() == '******':
#             break
#         print(line, end='')


# join method takes path components, that tries to "intelligently" join them together
# based on underlying os
# path = os.path.join(os.sep, 'Users', 'SMarya', 'WORK', 'practice-python', 'file1.txt')
# print(path)
# print(os.sep)

# used to convert a possibly given windows path to posix path, vice-versa,
# by automatically detecting underlying OS
# making it easy to write OS agnostic software
# a = Path(path)
# type(a)
# f = open(a)
# for _ in range(10):
#     print(f.__next__(), end='')
# f.close()
#
# s = "\\user\\bench"
# g = r"\user\bench"
# both are equivalent

# for user input in python2 - raw_input('Enter a number: ')
# for user input in python3 - input('Enter a number: ')


# user_input = input('Enter a number: ')
# print(user_input)
#
# if user_input == '7':
#     # tells python not to expect anything in the indented block
#     # and move on to the next unintended line
#     pass
# else:
#     print(user_input)
#
# sentence = "# used to convert , a possibly given windows path to posix path , vice-versa, " \
#            "# by automatically detecting underlying OS , # making it easy to write OS agnostic" \
#            " software"
# words = sentence.split()
#
#
# word_counter = Counter(words)
# print(word_counter.most_common(3))

# reg ex increases your capability as a programmer


# \s Matches Unicode whitespace characters (which includes [ \t\n\r\f\v]
# cleaned_words = re.split(r'[#;.,\s]\s*', sentence)
# word_counter = Counter(cleaned_words)
# print(word_counter.most_common(3))

# Python Dictionaries
# how do we map multiple values to the same key?
# d = {}
# d['a'] = 1
# d['a'] = 2  # overwrites previous value
# print(d)
#
# items = (
#     ('a', 1),
#     ('a', 3),
#     ('b', 1),
#     ('b', 1)
# )
#
# d = {}
# for key, value in items:
#     if key not in d:
#         d[key] = set()
#     d[key].add(value)

# we are holding the items we want in a set assigned to a key
# we can do this another way with defaultdict
# all we need to do is,
# tell python, which data structure we want our items to contain in

# d = defaultdict(set)
#
# for key, value in items:
#     d[key].add(value)
#
# print(d)
#
# d = defaultdict(list)
#
# for key, value in items:
#     d[key].append(value)
#
# print(d)


# variable positional and keyword arguments

#
# def printer(*args):
#     print(type(args))
#     print(args)
#
#
# printer(1, 2, 3, "sod")
#
#
# def printer2(*args, **kwargs):
#     print(args, kwargs)
#
#
# printer2(1, 2, 3, a=10, b="sid")


# you can see this used in decorators, where it means that decorator can accept
# any function call and any arguments that the function is called with,
# decorators can do this with no knowledge of what function is decorated with it

# you can also see this in iterables of arbitrary length

# conn_details = ('localhost', 5000)
# host, port = conn_details
# a, b, c, d, e, f = 'String'


# file = '/Users/SMarya/WORK/practice-python/file1.txt'
# path = '/Users/SMarya/WORK/practice-python'

# os built-in module has many handy methods in submodules, like below

# os.path.exists(file)
# os.path.exists(path)

# there are methods to tell, what we passed in, is a file or directory or a symbolic link
# we have full access to the metadata
# can get size in bytes, modified time

# os.path.isfile(path)
# os.path.isdir(path)
# os.path.islink(file)
# os.path.getsize(file)
# os.path.getsize(path)
# os.path.getatime(file)

# modified time, returned is seconds past the UNIX epoch
# os.path.getmtime()

# a way of converting that to datetime
# from datetime import datetime
# datetime.fromtimestamp(os.path.getmtime(file)).strftime('%A, %B, %d, %Y, %I:%M:%S')

'''
it helps to know which functions return text, which return bytes
especially for network programming

binary data can be read from and write to text file,
by reading from buffer attribute stdin or writing to buffer attribute of stdout
'''
# sys.stdout.write("text\n")

# throws error
# sys.stdout.write(b'sidadeq')

# using buffer attributes, won't throw error
# sys.stdout.buffer.write(b'text')

# using output redirection to write help text in a file

# with open('sys_help.txt', 'w') as f:
#     prev_stdout = sys.stdout
#     sys.stdout = f
#     help(sys)
#     sys.stdout = prev_stdout

# there is a decorator that does just this in contextlib built-in module
# called redirect_stdout, underlying mechanics is just as above

# contextlib.redirect_stdout

# can understand iteration by considering the context, iterable object, iterator object
# for x in [1, 2, 3, 4, 5]:
#     print(x)
#
# for x in {'Paris': 10, 'York': 30}:
#     print(x)
#
# for x in "String":
#     print(x)
#
# x = list([1, 2, 5, 3])

# dunder iter is available on iterable objects
# return the iterator object
# i = x.__iter__()
# print(i.__next__())
# print(next(i))
#
# # for loop is equivalent to below
# # under the hood
# iter_obj = x.__iter__()
# while True:
#     try:
#         x = next(iter_obj)
#     except StopIteration:
#         break
#     print(x)


'''
generator is a function that produces a sequence of results, instead of single value
just need to put a yield keyword in the function
when we call this function, we create a generator object
'''

# def countdown(n):
#     print('Start counting')
#     while n > 0:
#         yield n
#         n -= 1
#
#
# gen = countdown(10)
#
# print(next(gen))
# # generator object retains state and resumes from where it left
# print(next(gen))
# # stops short of next yield

# generators vs iterables
# replace [] in list comprehension with () to get generator
# a = [1, 2, 3, 4]
# iterable = [x ** 2 for x in a]
#
# for item in iterable:
#     print(item)
#
# generator = (x ** 2 for x in a)
#
# for item in generator:
#     print(item)
#
# for item in iterable:
#     print(item)

# only one time iteration through generator
# below no more returns results
# for item in generator:
#     print(item)
#
#
# def concatenate(sources):
#     for a in sources:
#         for item in a:
#             yield item
#
#
# x = [[1, 2, 3], [99, 98, 100]]
# a = concatenate(x)
# print(next(a))


# above code to equivalent to below, yield from - shortens syntax

# def concatenate(sources):
#     for a in sources:
#         yield from a


'''
yield from can also be used to delegate
yield from function_name -
which also has to be generator function i.e which itself yields
'''

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
#
# def countup(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1


'''
behaviour of this function can be explain as follows
first yields from countdown, yields 5,
in while loop, then 4, 3, 2, 1, 0, runs out of countdown
yields to countup, up until 5 in a while loop
o/p: 5 -> 4 -> 3 -> 2 -> 1 -> (into second generator)0 -> 1 -> 2 -> 3 -> 4
'''
# def combined_gen(n):
#     yield from countdown(n)
#     yield from countup(n)
#
#
# for x in combined_gen(5):
#     print(x)
#
#
# def revc_count():
#     try:
#         while True:
#             n = yield
#             print(n)
#     except GeneratorExit:
#         print("So much more to say about these co-routines")
#
#
# r = revc_count()
# r.send(100)
#
# # how for loop works
# x = [1, 2, 3, 4, 5]
# for i in x:
#     print(i)
#
# # code above is equivalent to code below
# x = [1, 2, 3, 4, 5]
# y = iter(x)
# try:
#     while True:
#         print(next(y))
# except StopIteration as e:
#     pass


'''
what are coroutines?
functions whose execution can be paused/suspended at a particular point,
and then we can resume the execution from that same point later whenever we want.
'''

# def func():
#     print('Function Starts')
#     yield
#     print('Function Ends')
#
#
# try:
#     y = func()
#     print(type(y))
#     next(y)  # First part of the function executed
#     next(y)  # Second part of the function executed
#     next(y)  # Raises StopIteration Exception
# except StopIteration as e:
#     print("in exception space")
#
# try:
#     y = func()
#     print(type(y))
#     next(y)  # First part of the function executed
#     next(y)  # Second part of the function executed
# except StopIteration as e:
#     print("check if execution still goes to exception space? It does!")


'''
generator object will behave similarly to an iterator, but
in the case of an iterator, we are traversing over an iterable.
With a generator, we’re executing parts of the coroutine.

this facility of pausing of the function execution opens up some possibilities
to debug, return and trace the value of a variable across the execution of a function

to send a value at a certain point, can use send function, instead of next
'''
# def func():
#     print('Function part 1')
#     x = yield
#     print(f"value sent first time is {x}")
#     print('Function part 2')
#     a = yield
#     print(f"value sent next time is {a}")
#     print('Function part 3')


# try:
#     y = func()
#     # we can only use send when we are at the yield checkout,
#     # so first function call has to be next(), to reach the first yield
#     next(y)  # Function part 1 executed, to reach the first yield we used next
#     y.send(6)  # Function part 2 executed and value sent 6
#     y.send(12)  # Function part 2 executed and value sent 12 and StopIteration raised
# except StopIteration as e:
#     pass

'''
To switch back and forth between two functions
in multithreading, it is preemptive multitasking,
until an interrupt is encountered by the OS, it will keep executing.
In coroutines case, it is non-preemptive multi tasking,
can switch whenever we want
'''

#
# def func1():
#     print('Function 1 part 1')
#     yield
#     print('Function 1 part 2')
#     yield
#     print('Function 1 part 3')
#     yield
#     print('Function 1 part 4')
#     yield
#     print('Function 1 part 5')
#
#
# def func2():
#     print('Function 2 part 1')
#     yield
#     print('Function 2 part 2')
#     yield
#     print('Function 2 part 3')
#     yield
#     print('Function 2 part 4')
#     yield
#     print('Function 2 part 5')
#
#
# try:
#     a = func1()
#     b = func2()
#     next(a)  # Will execute Function 1 part 1
#     next(b)  # Will execute Function 2 part 1
#     next(a)  # Will execute Function 1 part 2
#     next(a)  # Will execute Function 1 part 3
#     next(b)  # Will execute Function 2 part 2
#     next(b)  # Will execute Function 2 part 3
#     next(b)  # Will execute Function 2 part 4
#     next(a)  # Will execute Function 1 part 4
#     next(a)  # Will execute Function 1 part 5 and raise StopIteration exception
# except StopIteration as e:
#     pass

'''
So if we write our own custom scheduler that handles the switching between multiple
coroutines, we can achieve with single thread what we do with multithreading.
 
Coroutines have many applications such as concurrency 
and other programming patterns can also be implemented, 
like Producer-Consumer or Sender-Receiver in network programming. 
I’ll be exploring those in upcoming articles.
'''
# super() method, inheritance
# class Base:
#     def __init__(self):
#         print("Base.__init__")
#
# class Child1(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Child1.__init__")
#
# class Child2(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Child2.__init__")
#
# class Child3(Child1, Child2):
#     def __init__(self):
#         Child1.__init__(self)
#         Child2.__init__(self)
#         print("Child3.__init__")

# executes __init__ of Base class twice
# can cause serious problems and errors, unless you are very careful
# c3 = Child3()

# >>> c3 = Child3()
# Base.__init__
# Child1.__init__
# Base.__init__
# Child2.__init__
# Child3.__init__

# instead you can use super(), to make it work correctly
# class Base:
#     def __init__(self):
#         print("Base.__init__")
#
# class Child1(Base):
#     def __init__(self):
#         super().__init__()
#         print("Child1.__init__")
#
# class Child2(Base):
#     def __init__(self):
#         super().__init__()
#         print("Child2.__init__")
#
# class Child3(Child1, Child2):
#     def __init__(self):
#         super().__init__()
#         print("Child3.__init__")

# Base __init__ method was executed only once now
# c3 = Child3()

# >>> c3 = Child3()
# Base.__init__
# Child2.__init__
# Child1.__init__
# Child3.__init__

'''
every class you define has a method resolution order(mro)
mro is essentially all base classes in linear order
calculated using see-through linearization
which is a merge-sort of mros from parent classes subject to 3 constraints
1. child classes get checked before parent classes
2. multiple parent classes get checked in the order listed
3. if there are 2 valid choices for next class, one from first parent is chosen

when python sees super(), it continues it's search with the next class in mro
thus, as long as every redefined method consistently uses super, and only calls it once
entire mro list will be worked through and each method in hierarchy is called only once


super() doesn't necessarily go to the direct parent of the class, next in the mro(skipped
by few places), where it goes is decided by the immediete next class in the mro

you can use super() even in classes with no direct parent, though might lead to
unexpected behaviour if you are not careful
'''
# print(Child3.mro())

#
# class Ten:
#     def adder(self, *args):
#         print(sum(args) + 10)
#         # super continues search starting with next class on mro
#         super().adder()
#
# class Hundred:
#     def adder(self, *args):
#         print(sum(args) + 100)
#
# class Experiment(Ten, Hundred):
#     pass
#
# e = Experiment()

'''
Even though there is no relation between Ten and Hundred classes except being
the parents of a common subclass, super call in adder method of Ten called
adder method of Hundred, thus super behaviour can also be unpredictable
super is following mro order
thus it's prudent to exercise extreme caution when using multiple inheritance
'''

# e.adder(1, 2, 3)
# 16
# 100

# print(Experiment.__mro__)
# (<class '__main__.Experiment'>, <class '__main__.Ten'>, <class '__main__.Hundred'>, <class 'object'>)

'''
Metaclasses - customized instance creation

Class is constructed using type by default
code in the body is executed in new namespace and class name is bound locally
to the result of the function "type" which takes 3 arguments
name, bases and a namespace dictionary
'''

# class A:
#     a = 1
#
#
# A = type('A', (object,), dict(a=1))
#
#
# class PrintOnCreation(type):
#     def __call__(cls, *args, **kwargs):
#         print("instance of Planet Created")
#         super().__call__(*args, **kwargs)
#
#
# class Planet(metaclass=PrintOnCreation):
#     def __init__(self, cities):
#         print("weherw afaet")
#         self.cities = cities
#
#
# earth = Planet(['Paris', 'Oslo'])
#
#
# class NullInstances(type):
#     def __call__(cls, *args, **kwargs):
#         raise TypeError('Instantiation Blocked')
#
#
# class Planet(metaclass=NullInstances):
#     def __init__(self, cities):
#         print("weherw afaet")
#         self.cities = cities
#
#
# # throws exception
# earth = Planet(['Paris', 'Oslo'])


# class Singleton(type):
#     def __init__(cls, *args, **kwargs):
#         """
#         This is called when a class with this as meta is initialized,
#         as classes are instances of metaclass
#         so, using this as a hook, we are adding __instance attribute to class namespace
#         i.e class level attribute
#         """
#         cls.__instance = None
#         super().__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         """Check in cls namespace for the value of __instance attribute"""
#         if cls.__instance is None:
#             cls.__instance = super().__call__(*args, **kwargs)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#
# class Planet(metaclass=Singleton):
#     pass
#
#
# first = Planet()
# second = Planet()
# first is second


# class EnforcerMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         for name in clsdict:
#             if name.lower() != name:
#                 raise TypeError('Inappropriate method name: ' + name)
#         return super().__new__(cls, clsname, bases, clsdict)
#
#
# class Root(metaclass=EnforcerMeta):
#     pass
#
#
# class ChildA(Root):
#     def method_name(self):
#         pass


# throws exception while defining class
# class ChildB(Root):
#     def methodName(self):
#         pass
#
#
# a = ChildA()
# b = ChildB()

'''
Explore auto-timing of functions using decorators 
without wraps, the function will look like a wrapper, loose doc strings etc
retains metadata of the original function
'''

#
# def time_func(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """
#         more accurate, better resolution than time.time()
#         includes time elapse during sleep state - thus not accurate for
#         time elasped for execution of a block of code
#         have to use contextmanager from contextlib
#         """
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'{func.__module__}, {func.__name__} : {end - start} seconds')
#         return result
#
#     return wrapper
#
#
# @time_func
# def test_func(x):
#     """This function counts up to 1,000,000 from x"""
#     while x < 1_000_000:
#         x += 1


# help(test_func)
#
#
# def time_func2(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'{func.__module__}, {func.__name__} : {end - start} seconds')
#         return result
#
#     return wrapper


# @time_func2
# def test_func2(x):
#     """This function counts up to 1,000,000 from x"""
#     while x < 1_000_000:
#         x += 1
#
#
# help(test_func2)  # function name,
# test_func2
# test_func2(10)


# @contextmanager
# def time_block(name):
#     start = time.perf_counter()
#     try:
#         yield
#     finally:
#         end = time.perf_counter()
#         print(f'{name} : {end - start} seconds')
#
#
# with time_block('write to file'):
#     with open('file.txt', 'w') as f:
#         for n in range(10):
#             f.write("This is a significant I/O component.\n")


'''
A descriptor is an object attribute with a binding behaviour
descriptors are a general purpose way of intercepting attribute access, 
they are the mechanism behind @properties, staticmethods, class methods etc



'''


# class A:
#     __attr = 10


'''
A.__attr --> no attribute on this name only for dunder attributes, 
not for regular attributes
A._A_attr --> descriptors intercept class formation and add _A prefix
this is to avoid name clashes with other child and parent classes

for a._A_attr, pythn first looks in instance dictionary, if not there
looks in class itself - lookupchain, then base class
 '''
# a = A()
# print(a._A__attr)

'''
descriptor protocol was when if anyone of the 3, dunder get, 
dunder set or dunder delete had been defined and overwritten 
in a class of which the attribute in question is an instance
'''


# class DescriptorClass:
#     def __init__(self, initial_value=None, name='var'):
#         self.val = initial_value
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         print('Retrieving', self.name)
#         return self.val
#
#     def __set_name__(self, obj, val):
#         print('Setting', self.name)
#         self.val = val
#
#
# # when this is class is defined, when x = is run
# # the descitor hooks run __set_name__ function
# class SimpleClass:
#     x = DescriptorClass(1, 'variable "x"')
#     y = 2
#
#
# s = SimpleClass()
# print(s.x)  # gets rerouted to __get__
# print(s.y)

'''
To overload an operator simply means to intercept built-in operations
in a class's methods. 
'''


# class User:
#     def __init__(self, name):
#         self.username = name
#
#     '''
#     ideal repr is one that uniquely identifies that instance, used for dev, debugging
#     str should return a more user friendly version of that
#     '''
#
#     def __repr__(self):
#         return 'Instance with id {} of class User'.format(id(self))
#
#     def __str__(self):
#         return '{} user-friendly. Debug info in __repr__'.format(self.username)
#
#
# lp = User('lp')
# lp
# str(lp)

''''
operator overloading
'''


# class Upper:
#     def __init__(self, initial):
#         self.data = initial.upper()
#
#     '''
#     operator overloading method
#     with this method, we enable the objects to have addition operation
#     '''
#
#     def __add__(self, other):
#         return Upper(self.data + other)
#
#     # python calls radd only when object on rhs is your class instance
#     # use this if both are equivalent, there is no ordering
#     __radd__ = __add__
#
#     # for inplace agumented addition
#     def __iadd__(self, other):
#         self.data += other
#         return self
#
#
# u = Upper('lowercase')

'''
Say you have a postgres db with a schema. Say, you want to represent the rows of your
database tables as python objects. 
Your code that uses objects corresponding to those rows must know your db schema, 
but your code that connects your objects to db doesn't need to know the schema, can
be generic
'''


# class LazyDB:
#     def __init__(self):
#         self.lp = "photo_lp.jpg"

    # attribute interception technique
    # called on any attempt to access an attribute that isn't in instance dictionary
    # '''
    # __getattr__ is only invoked if the attribute wasn't found the usual ways.
    # It's good for implementing a fallback for missing attributes
    # '''

    # def __getattr__(self, name):
    #     value = 'photo_{}.jpg'.format(name)
    #     # equivalent to 'self.name = value'
    #     setattr(self, name, value)
    #     return value


# class DbVerbose(LazyDB):
#     def __getattr__(self, name):
#         print('Called __getattr__({})'.format(name))
#         # calls LazyDB code, using super avoids recursion
#         return super().__getattr__(name)
#
#
# class ValidatingDB:
#     def __init__(self):
#         self.lp = "photo_lp.jpg"
#
#     '''
#     __getattribute__ is invoked before looking at the actual attributes on the object,
#     and so can be tricky to implement correctly. You can end up in infinite recursions
#     very easily.
#     '''
#
#     def __getattribute__(self, name):
#         print('Called __getattribute__({})'.format(name))
#         try:
#             return super().__getattribute__(name)
#         except AttributeError:
#             value = 'photo_{}.jpg'.format(name)
#             setattr(self, name, value)
#             return value
#
#
# class SetAttrDb:
#     """
#     This is method is called every time we set a value to an attribute
#     here we are intercepting built-in operations
#     """

#     def __setattr__(self, name, value):
#         print('Called __setattr__({} {}))'.format(name, value))
#         super().__setattr__(name, value)
#
#
# db = LazyDB()
# dbv = DbVerbose()
# validating_db = ValidatingDB()
#
# print('Before: {}'.format(db.__dict__))
# print(db.joe)
# print('After: {}'.format(db.__dict__))
#
# print('-' * 40)
#
# print('Before: {}'.format(dbv.__dict__))
# print('joe exists? {}'.format(hasattr(dbv, 'joe')))
# print(dbv.joe)
# print('joe exists? {}'.format(hasattr(dbv, 'joe')))
# print('After: {}'.format(dbv.__dict__))
#
# print('lp: {}'.format(validating_db.lp))
# print('joe: {}'.format(validating_db.joe))
#
# set = SetAttrDb()
# set.a = 10

'''
SUPER and RECURSION
below class falls into recursion
'''


# class Problem:
#     def __init__(self, data):
#         self.data = data
#
#     def __getattribute__(self, name):
#         print('Called __getattribute__({})'.format(name))
#         return self.data[name]
#
#
# p = Problem({'x': 1})
'''
this attempt to access attribute goes into infinite loop
as we are intercepting __getattribute__ inbuilt call, but not redirecting there
but trying to access attribute again, which again calls this method
'''
# p.x

'''
this way, when calling super, it calls the built-in method instead of going recursive
with that, we won't intercept the call with our custom function again

super continue search in next class in mro
'''


# class Problem:
#     def __init__(self, data):
#         self.data = data
#
#     def __getattribute__(self, name):
#         print('Called __getattribute__({})'.format(name))
#         data_dict = super().__getattribute__('data')
#         return data_dict[name]
#
#
# p = Problem({'x': 1})
#
# p.x
#
#
# class Callback:
#     def __init__(self, number):
#         self.num = number
#
#     def __call__(self, *args, **kwargs):
#         self.num += 1
#         print(self.num)

    # '''
    # intercepting call method, to allow call operator('object()')
    # making the object callable
    #
    # Can be used in GUIs by implementing callback for a button
    # esp where state is retained
    # '''


# c = Callback(1)
# c()
# c()
#
#
# class Button:
#     def __init__(self, *args, **kwargs):
#         self.command = kwargs['command']
#
#
# b1 = Button(commad=c)

'''
This way, by assigning callback to a button,
button can store the state using callback object
'''

'''
other operators that can be overloaded include 
'enter' and 'exit' to create a context manager
'iter' to create an instance that supports iteration
'''

''''
Place an exception windsup at runtime
where exceptions are handled is more of a function of control flow than of statement syntax

Exception - Classes - hierarchy 
The exception is handled closest catch block up and above which matches the exception

BaseException has 4 Sub Classes - KeyboardInterrupt, SystemExit, Exception etc

try:
    pass
except Exception as e:
    # handles everything, bad python code
    # need to be more specific
    print("hi")

'''

'''
PYTHON BYTECODE
'''


# def concatenate(x, y):
#     return x + y


'''
>>> concatenate.__code__.co_code
b'|\x00|\x01\x17\x00S\x00'

To disassemble code
'''
import dis

# dis.dis(concatenate)
'''
>>> dis.dis(concatenate)
line no.   Mem Off Instruction          Arguments
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
'''


# def absolute(x):
#     if x > 0:
#         return x
#     else:
#         return -x


'''
>>> absolute.__code__.co_code
b'|\x00d\x01k\x04r\x0c|\x00S\x00|\x00\x0b\x00S\x00d\x00S\x00'

>>> dis.dis(absolute)
  2           0 LOAD_FAST                0 (x)              if x > 0
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               4 (>)
              6 POP_JUMP_IF_FALSE       12

  3           8 LOAD_FAST                0 (x)              return x
             10 RETURN_VALUE

  5     >>   12 LOAD_FAST                0 (x)              return -x
             14 UNARY_NEGATIVE
             16 RETURN_VALUE
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE

last two lines are dead code - won't be reached here as there is already a return above it
this is because of cpython code generation rule, where it append the last two instructions when 
there is no explicit return statement in python code this will help return from the function
'''

'''
With some Default Parameters - we see Unexpected Behaviour(expected, if you know why)
This happens when the default parameters are mutable. 
Default values are always evaluated when the function definition is executed
When python encounters function definition, it executes default parameters in order to create 
a function object that is then used when you call it
'''


# def append_one(value, _list=[]):
#     _list.append(value)
#     return _list
#
#
# a = append_one(1)
# b = append_one(2)

'''
>>> a = append_one(1)
>>> b = append_one(2)
>>> a
[1, 2]      # expected [1]
>>> b
[1, 2]      # expected [2]
>>> append_one.__defaults__
([1, 2],)

to hack around it we can do
'''


# def append_one(value, _list=None):
#     if _list is None:
#         _list = []
#     _list.append(value)
#     return _list


'''
>>> a = append_one(1)
>>> b = append_one(2)
>>> a
[1]
>>> b
[2]
>>> append_one.__defaults__
(None,)
'''

'''
understanding mutable defaults enable us use them for valid use cases.
Memoization - speeds up programming by storing results of expensive function calls
'''


# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# @time_func
# def memoization(n, memo={}):
#     try:
#         value = memo[n]
#     except KeyError:
#         value = fib(n)
#         memo[n] = value
#     return value


'''
>>> memoization(36)
__main__, memoization : 4.769559389911592 seconds
24157817

caches the value for the second call, takes fraction of the time

>>> memoization(36)
__main__, memoization : 4.093162715435028e-06 seconds
24157817
'''

'''
lambda functions, scoping, binding a run-time/definition time(default-arguments)
'''

# x = 5
# adder1 = lambda y: x + y
# x = 10
# adder2 = lambda y: x + y
# print(adder1(1))
# print(adder2(10))
'''
>>> print(adder1(1))        x is bound at run time, not definition time - i.e most recent value of x
11
>>> print(adder2(10))
20
'''
# x = 5
# adder1 = lambda y, x=x: x + y
# x = 10
# adder2 = lambda y, x=x: x + y
#
# print(adder1(1))
# print(adder2(10))
'''
>>> print(adder1(1))        when added as default, x is picked at definition time - i.e most recent value of x
6
>>> print(adder2(10))
20
'''

'''
lambda is used for callback handlers, embedded directly in a registration calls arguments lists
also used as values in jump tables, dict of actions to be performed on-demand

also makes code readable, all the code needed right where is used

when you needed to put small pieces of executable code in places where def statements are illegal syntactically
ex: in a list, def is a statement, lambda is an expression(line of code)
'''

# list1 = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
# for func in list1:
#     print(func(4))

'''
To simulate the same with defs, need you to declare temporary function definitions, before the list,
which will only be used once, and can cause clutter in namespace, taking up names
'''

'''
body of the lambda has to be single expression, appear to place extreme limits on logic you can put in lambda
but we need can do some hacks, to perform loops within lambda do map calls and list comprehensions
'''

# s = lambda x: list(map(sys.stdout.write, x))
# '''
# >>> s(['One', 'two', 'four'])
# Onetwofour[3, 3, 4]
# '''
#
# func = lambda x: lambda y: x + y
#
# print(func(1)(2))

'''
A common use of lambda is to define in-line call back functions in tkinter, when creating GUI
'''

# from tkinter import Button, mainloop
#
# x = Button(
#     text='Button text',
#     action=lambda: sys.stdout.write('Something\n')
# )
# x.pack()
# mainloop()

'''
GENERATORS
'''


# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
#
# for i in countdown(10):
#     print(i)
#
# x = countdown(10)  # creates generator
# x
# next(x)
'''
From Generators to Coroutines
PEP 342 - Introduced yield as an expression 
--> can now use yield on the right side of an assignment

Generators produce data for iteration, Coroutines consume data
Despite Similarities, they are Distinct Concepts 

Below is an example of coroutine, 
Coroutine does more than, just generate values, but can also consume values sent to it

There is use of having yield produce a value in a coroutine, but it's not tied to iteration!!

"yield from name" is explained away as merely being shorthand for 
yielding values from an iterator, including other generators

But it's real use lies in, allowing delegation to a sub-generator
so that any next(gen) or gen.send("data") can be passed on to nested generators,
acting as a tunnel, that passes data back(generator) and forth(coroutine)
'''


# def finder(x):
#     while True:
#         input_text = yield
#         if x in input_text:
#             print(input_text)


'''
>>> a = finder(10)
>>> a.send("wes")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
Priming a coroutine can be done either by a.send(None) or next(a), 
need to be done once at the beginning
>>> a.send(None)
>>> a.send([1,2,3])
>>> a.send([1,2,20, 10, 20, 10])
[1, 2, 20, 10, 20, 10]

To end the coroutine
>>> a.throw(AttributeError, "Can be any Exception")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in finder
AttributeError: Can be any Exception
>>> a.send([10])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

'''
From Python 3.5 onwards, the preferred way of declaring coroutines is with "async await" syntax
these are known as native coroutines, to distinguish them from generator based coroutines 
'''


# def greet(name):
#     return 'Hello ' + name
#
#
# async def _greet(name):
#     return 'Hello ' + name


'''
>>> greet
<function greet at 0x101e3a7b8>
>>> _greet
__main__:1: RuntimeWarning: coroutine '_greet' was never awaited
<function _greet at 0x101e3a840>
>>> greet("sid")
'Hello sid'
>>> _greet("sid")
<coroutine object _greet at 0x101b91af0>
>>> g=_greet("Python")
>>> g
<coroutine object _greet at 0x101b91af0> 
>>> g.send(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: Hello Python

We get a StopIteration with value  attribute of the exception is return value of function


we get StopIteration exception because once the execution started with send() call, 
we have reached end of async block and returning, not "yielding" - 
recall that when generator runs out, also raises StopIteration
'''

'''
Coroutines are there to be driven by something else
can't call next, as it's not an iterator, way to get the data we want is to send in None
run function sends in None, catches exception, returns value attribute, thus drives coroutine
'''


# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         print(e.value)
#         return e.value


'''
>>> run(_greet("Sid"))
'Hello Sid'
'''

'''
async functions can call other async functions. 
But if you have to call another async function, you have to use await keyword before it.
'''


# async def main():
#     print(await _greet('LP'))
#
#
# run(main())
#
#
# async def main():
#     names = ['Alabama', 'Bristol', 'Calagary']
#     for name in names:
#         print(await _greet(name))
#     return "Testing"
#
#
# run(main())


# class A:
#     async def instance_method(self):
#         print('instance method')
#
#     @classmethod
#     async def class_method(cls):
#         print('class method')
#
#     @staticmethod
#     async def static_method(self):
#         print('static method')


'''
>>> a.instance_method
<bound method A.instance_method of <__main__.A object at 0x101e37fd0>>
>>> a.instance_method()
<coroutine object A.instance_method at 0x101e1b990>
'''

'''
Synchronous vs Asynchronous
'''
import time


# def count():
#     # represents network calls, server work,
#     # waiting for network bases I/O as ooposed CPU intensive work
#     time.sleep(1)
#     print('1')
#     time.sleep(1)
#     print('2')
#     time.sleep(1)
#     print('3')
#
#
# def main():
#     for _ in range(3):
#         count()


# if __name__ == '__main__':
#     t1 = time.perf_counter()
#     main()
#     t = time.perf_counter() - t1
#     print(f'Total time elapsed: {t:0.2f} seconds')
'''
above code takes 9 seconds to finish, each cycle 
runs to completion before next cycle begins
'''

import asyncio


# async def count():
#     await asyncio.sleep(1)
#     print('1')
#     await asyncio.sleep(1)
#     print('2')
#     await asyncio.sleep(1)
#     print('3')

# takes 3 seconds
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# asyncio.run(main())
'''
takes 3 seconds instead of 9 seconds - 
all 3 1's at once, then all 3 2's at once, then all 3 3's at once,
when the first await in count is hit, python was free to do other work, 
ex starting second, and then third count function call
'''
# takes 9 seconds, calls another coroutine - count, start's that coroutine and then waits for the results
# async def main():
#     for _ in range(3):
#         await count()
#
# asyncio.run(main())

'''
Asynchronous frameworks need a scheduler, usually called event-loop.
Which keeps track of all the running tasks
When a function is suspended, it them returns control to the event loop,
which then will find another function to start or resume and this is called
cooperative multitasking
'''

# loop = asyncio.get_event_loop()
#
# async def greeter(name):
#     print("Hi", name, "You are in a coroutine.")
#
# try:
#     print('starting coroutine')
#     coro = greeter('LP')
#     print('entering event loop')
#     loop.run_until_complete(coro)
# finally:
#     print('closing event loop')
#     loop.close()

'''
This example has two phases that are to be executed in order, 
but can run concurrently with other operations
'''
loop = asyncio.get_event_loop()
async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result1 = await phase2(result1)
async def phase1():
    print('in phase1')
    return 'phase1 result'
async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)
asyncio.run(outer())




'''
Profiling Python Programs
'''
import cProfile
import pstats

#
# def short():
#     time.sleep(0.01)
#
#
# def long():
#     time.sleep(0.1)
#
#
# def call_short():
#     for i in range(100):
#         short()
#
#
# def call_long():
#     for i in range(100):
#         long()
#
#
# profiler = cProfile.Profile()
# profiler.runcall(call_short)
# profiler.print_stats()
# cProfile.run('call_short()', 'short.stats')
# stats = pstats.Stats('short.stats')
# stats.print_stats()
'''
>>> profiler.print_stats()
         203 function calls in 1.132 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.132    1.132 <stdin>:1(call_short)
      100    0.001    0.000    1.131    0.011 <stdin>:1(short)
      100    1.130    0.011    1.130    0.011 {built-in method time.sleep}
        2    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
