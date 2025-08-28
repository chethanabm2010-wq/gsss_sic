Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
capitals =['panjim','bhubaneshwar','guwahti','aizwal','imphal','agartala','gangtok','kohima','itanagar','shilong']
print(capitals[10])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(capitals[10])
IndexError: list index out of range
print(capitals[3:3])
[]
print(capitals[::3])
['panjim', 'aizwal', 'gangtok', 'shilong']
print(capitals[3;2:-1])
SyntaxError: invalid syntax
print(capitals[3:2:-1])
['aizwal']
print(capitals[-11])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(capitals[-11])
IndexError: list index out of range
print(capitals[-10])
panjim
print(capitals[:-15:-1])
['shilong', 'itanagar', 'kohima', 'gangtok', 'agartala', 'imphal', 'aizwal', 'guwahti', 'bhubaneshwar', 'panjim']
print(capitals[::-1])
['shilong', 'itanagar', 'kohima', 'gangtok', 'agartala', 'imphal', 'aizwal', 'guwahti', 'bhubaneshwar', 'panjim']
>>> print(capitals[:-15:-1:1])
SyntaxError: invalid syntax
>>> print(capitals[-15:-1:1])
['panjim', 'bhubaneshwar', 'guwahti', 'aizwal', 'imphal', 'agartala', 'gangtok', 'kohima', 'itanagar']
>>> print(capitals[:-15:2])
[]
>>> 
... list1= ['a','b','c','1','2','3']
>>> list2=[2,5,9,10]
>>> for i in enumerate(list2)
SyntaxError: expected ':'
>>> for i in enumerate(list2):
...     print(list2)
...     \n
...     
SyntaxError: unexpected character after line continuation character
>>> digits[pivot+1:] = sorted(digits[pivot+1:])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    digits[pivot+1:] = sorted(digits[pivot+1:])
NameError: name 'digits' is not defined
>>> digits=6789
>>> digits[pivot+1:] = sorted(digits[pivot+1:])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    digits[pivot+1:] = sorted(digits[pivot+1:])
NameError: name 'pivot' is not defined
pivot=7
digits[pivot+1:] = sorted(digits[pivot+1:])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    digits[pivot+1:] = sorted(digits[pivot+1:])
TypeError: 'int' object is not subscriptable
