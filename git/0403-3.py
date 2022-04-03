##응용예제 1번##
##전역 변수 부분##

year = 0

##메인 코드 부분##

if __name__=="__main__":
    year=int(input("연도를 입력하세요 : "))

    #윤년이 될 수 있는 경우 2가지
    #1.4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는다.
    #2.400으로 나누어 떨어진다.

    if((year%4==0)and(year%100!=0))or(year%400==0):
        print("%d년은 윤년입니다."%year)

    else:
        print("%d년은 윤년이 아닙니다."%year)
        
-------

#x와 y를 매개변수로 받고 합을 반환해주는 함수

def add(x,y):
    return x+y

print(__name__)

--------

import addModule

print(Module.add(3,5))

---------

##응용예제 2번##

import turtle

##전역 변수 부분##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

##메인 코드 부분##
if __name__=="__main__":

    #초기설정
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50) #그래픽 창 크기 지정
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)

    num = int(input("숫자를 입력하세요 :"))
    binary = bin(num) #bin(): 10진수를 2진수로 바꿔주는 함수 -> ex) 101010


#거북이 좌표
    curX = swidth/2
    curY = 0

for i in range(len(binary)-2):
    turtle.goto(curX,curY)

    #각각의 비트값 알아내기 (최하위 비트값)
    if num & 1:
        turtle.color('red')
        turtle.turtlesize(2)

    else:
        turtle.color('red')
        turtle.turtlesize(2)

        turtle.stamp()
        curX -=50
        num >>=1 ##num = num>>1

turtle.done


-----------------

##연습문제 10번##

import turtle

##전역 변수 부분##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

##메인 코드 부분##
if __name__=="__main__":

    #초기설정
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50) #그래픽 창 크기 지정
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)
    
    num = input("2진수를 입력하세요 :")
    num = input("2진수를 입력하세요 :")

    
    num = int(num1, 2) #int(",2)
    num = int(num2, 2)

    result = num1lnum2

    #num1에 대한 거북이 출력
    binary = bin(num1)
    curX = swidth/2
    curY = sheight/3

    for i in range(len(binary)-2):
    turtle.goto(curX,curY)

    if num1 & 1:
        turtle.color('red')
        turtle.turtlesize(2)

    else:
        turtle.color('red')
        turtle.turtlesize(1)

        turtle.stamp()
        curX -=50
        num1 >>=1

    #num2에 대한 거북이 출력
    binary = bin(num2)
    curX = swidth/2
    curY = 0

for i in range(len(binary)-2):
    turtle.goto(curX,curY)

    if num2 & 1:
        turtle.color('red')
        turtle.turtlesize(2)

    else:
        turtle.color('red')
        turtle.turtlesize(1)

        turtle.stamp()
        curX -=50
        num2 >>=1
        
    #result에 대한 거북이 출력
    binary = bin(result)
    curX = swidth/2
    curY = sheight/3

    for i in range(len(binary)-2):
    turtle.goto(curX,curY)

    #각각의 비트값 알아내기 (최하위 비트값)
    if result & 1:
        turtle.color('red')
        turtle.turtlesize(2)

    else:
        turtle.color('red')
        turtle.turtlesize(1)

        turtle.stamp()
        curX -=50
        result >>=1
    
turtle.done



---------------

##연습문제 6번##

num1, num2 = -100, 100

(1) (num1 == num2) and (num1!=num2)
>>> False

(2) (num1 == num2) or (num1!=num2)

>>> True

(3) (num1 >= num2) and (num1<=num2)
>>> False

(4) (num1 >= num2) or (num1<=num2)
>>> True


--------------


##연습문제 9번##
##전역변수 선언##

c500 = c100 = c50 = c10 = 0 ##이렇게 간단하게 사용하기
c500, c100, c50, c10, 0,0,0,0 ##이렇게 하지 말기

c500 = int(input("500원짜리 개수-->"))
c500 = int(input("100원짜리 개수-->"))
c500 = int(input("50원짜리 개수-->"))
c500 = int(input("10원짜리 개수-->"))

sum = (500*c500) + (100*c100) + (50*c50) + (10*c10)

print("##동전의 합계 ==> %d원" %sum)
