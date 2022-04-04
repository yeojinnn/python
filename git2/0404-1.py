Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a=99

if a<100:
    print("100보다 작음")

    
100보다 작음

=========== RESTART: C:/CookPython/code05_test.py ===========
이것참

=========== RESTART: C:/CookPython/code05_test.py ===========
이것참

=========== RESTART: C:/CookPython/code05_test.py ===========
100보다 작음
100보다 작은 게 맞음
이것참

=========== RESTART: C:/CookPython/code05_test2.py ==========
100보다 큼
큼

=========== RESTART: C:/CookPython/code05_test3.py ==========
100보다 큼
100보다 큼2
100보다 큼2
끝

=========== RESTART: C:/CookPython/code05_test4.py ==========
정수입력2
짝수입니다.
끝

=========== RESTART: C:/CookPython/code05_test5.py ==========
50보다 크고 100보다작군요.

=========== RESTART: C:/CookPython/code05_test6.py ===========
C
C

============= RESTART: C:\CookPython\code05-07.py ============
Traceback (most recent call last):
  File "C:\CookPython\code05-07.py", line 1, in <module>
    if a>=90:
NameError: name 'a' is not defined

============= RESTART: C:\CookPython\code05-07.py ============
D
학점입니다.^^

============= RESTART: C:\CookPython\code05-07.py ============
A
학점입니다.^^

========== RESTART: C:/CookPython/code05-07 뒤집기_.py ==========
Traceback (most recent call last):
  File "C:/CookPython/code05-07 뒤집기_.py", line 1, in <module>
    if a>=60:
NameError: name 'a' is not defined

========== RESTART: C:/CookPython/code05-07 뒤집기_.py ==========
A
학점입니다.^^

========== RESTART: C:/CookPython/code05-07 뒤집기_.py ==========
성적?:99
A
학점입니다.^^

========== RESTART: C:/CookPython/code05-07 뒤집기_.py ==========
성적?:90
A
학점입니다.^^
A
----------


j=55

if j>=60
SyntaxError: expected ':'

j=55
if j>=60:
    r="합격"

    
else:
    
SyntaxError: invalid syntax

j=55
if j>=60:
    r="합격"
else:
    r="불합격"
r
SyntaxError: invalid syntax
r
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    r
NameError: name 'r' is not defined
j
55

j=55

if j>=60:
    r="합격"
else:
    r="불합격"

    
r
'불합격'

'합격' if j>=60 else '불합격'
'불합격'
r='합격' if j>=60 else '불합격'

r
'불합격'

range(1,250)
range(1, 250)
for i in range(1,10)
SyntaxError: expected ':'
fir i in range(1,10):
    
SyntaxError: invalid syntax
for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9

for i in range(10):
    print (i)

    
0
1
2
3
4
5
6
7
8
9




friut=['사과', '배', '딸기', '포도']

friut
['사과', '배', '딸기', '포도']
print (fruit)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print (fruit)
NameError: name 'fruit' is not defined. Did you mean: 'friut'?
fruit=['사과', '배', '딸기', '포도']
fruit
['사과', '배', '딸기', '포도']
print (fruit)
['사과', '배', '딸기', '포도']
fruit[0]
'사과'
fruit[3]
'포도'
fruit[2]
'딸기'
fruit[1]
'배'


fruit
['사과', '배', '딸기', '포도']

fruit append ('바나나')
SyntaxError: invalid syntax

fruit append ('바나나')
SyntaxError: invalid syntax

fruit.append ('바나나')
fruit
['사과', '배', '딸기', '포도', '바나나']
fruit.append ('귤')
fruit [4]
'바나나'
fruit
['사과', '배', '딸기', '포도', '바나나', '귤']
print (fruit)
['사과', '배', '딸기', '포도', '바나나', '귤']

i
if '포도' in fruit:
    print ("있다")
else:
    print ("없다")

    
있다

============= RESTART: C:/CookPython/code05-09.py ============
Traceback (most recent call last):
  File "C:/CookPython/code05-09.py", line 4, in <module>
    swidth. sheight = 500, 500
NameError: name 'swidth' is not defined

============= RESTART: C:/CookPython/code05-09.py ============
Traceback (most recent call last):
  File "C:/CookPython/code05-09.py", line 10, in <module>
    turtle.screensize(swidth.sheight)
AttributeError: 'int' object has no attribute 'sheight'

============= RESTART: C:/CookPython/code05-11.py ============
1. 입력한 수식 계산 2. 두 수 사이의 합계 : 