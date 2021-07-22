import random
import sys

def welcome(user):
    return f'Welcome {user}!!!'

def counter(n):
    return range(n)

def package_loc():
    return '\n'.join(sys.path)

def random_int_no(s, e):
    return random.randint(s, e)