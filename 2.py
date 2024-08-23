from Crypto.Util.number import *
from sympy import *
from tqdm import *
# from secret import flag
from itertools import *
from math import factorial
import string
table = string.ascii_letters + string.digits + "@?!*"
print(table)
# print(string.digits)
print(permutations(table))
print(total=factorial(len(table)))