Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello Python world")
Hello Python world
>>> "Hello Python world"
'Hello Python world'
>>> 1
1
>>> 2
2
>>> 1+2
3
>>> 2**10
1024
>>> 2**0
1
>>> 2**1
2
>>> 2**2
4
>>> 2**3
8
>>> 2**4
16
>>> 7%3
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> "Hello Python world"
'Hello Python world'
>>> name=input("이름 입력:")
이름 입력:김명설
>>> name
'김명설'
>>> "abcd"+def"
SyntaxError: invalid syntax
>>> "abcd + "def"
SyntaxError: invalid syntax
>>> "abcd"+"def"
'abcddef'
>>> "abcd"+5
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    "abcd"+5
TypeError: can only concatenate str (not "int") to str
>>> print*"abcd"+5)
SyntaxError: unmatched ')'
>>> a=input("정수 입력:")
정수 입력:1
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
'1'
>>> a=int(input("정수 입력:"))
정수 입력:1
>>> a
1
>>> print("abcd",5)
abcd 5
>>> 
======== RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/asmd.py ========
첫 번째 숫자 입력:
Traceback (most recent call last):
  File "C:/Users/LIBPC1-01/Documents/programming/0513/asmd.py", line 1, in <module>
    a=int(input("첫 번째 숫자 입력:"))
ValueError: invalid literal for int() with base 10: ''
>>> 
======== RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/asmd.py ========
첫 번째 숫자 입력:4
두 번째 숫자 입력:6
4 + 6 = 10
4 - 6 = -2
4 * 6 = 24
4 / 6 = 0.6666666666666666
4 // 6 = 0
4 % 6 = 4
>>> 
>>> 
======== RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/asmd.py ========
첫 번째 숫자 입력:5
두 번째 숫자 입력:3
5 + 3 = 8
5 - 3 = 2
5 * 3 = 15
5 / 3 = 1.6666666666666667
5 // 3 = 1
5 % 3 = 2
>>> 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
>>> 
>>> print("123" end="*****")
SyntaxError: invalid syntax
>>> print("123",end="*****")
123*****
>>> 
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
>>> 
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
----------------------------------------
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
----------------------------------------
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
 1 1 
Python is [good           ]
Python is [good           ]
Python is [           good]
Python is [     good      ]
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
----------------------------------------
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
----------------------------------------
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
 1 1 
Python is [good           ]
Python is [good           ]
Python is [           good]
Python is [     good      ]
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
----------------------------------------
 1 2 
 1 2 
 2 1 
 1 2 3
 3 2 1 
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
하나 둘 셋 1 2 3
하나-둘-셋-1-2-3
첫번째 값
두번째 값
첫번째 값 ---> 두번째 값
첫번째 값  두번째 값
첫번째 값두번째 값
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
----------------------------------------
Hello World!!
Hello World!!
나의 이름은 '한사람'입니다.
나의 이름은 "한사람"입니다.
나의 이름은 "한사람"입니다.
나의 이름은 '한사람'입니다.
 1 1 
Python is [good           ]
Python is [good           ]
Python is [           good]
Python is [     good      ]
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
당신의 나이는 [             22]세
당신의 나이는 [22             ]세
----------------------------------------
 1 2 
 1 2 
 2 1 
 1 2 3
 3 2 1 
 *         3* *         2* *         1* 
>>> print("Hello Python world")
Hello Python world
>>> a='dfkdjgkfgdfdfdf'
>>> a="Life is too short"
>>> len(a)
17
>>> a="abcd"
>>> a[1]
'b'
>>> a[1]
'b'
>>> a[-3]
'b'
>>> a[0:3]
'abc'
>>> a[0:4]
'abcd'
>>> 
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
>>> 
======= RESTART: C:/Users/LIBPC1-01/Documents/programming/0513/output.py =======
>>> 
