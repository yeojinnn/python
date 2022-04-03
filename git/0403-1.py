# 변수
money,c500,c100,c50,c10=0,0,0,0,0

# 메인코드 부분
money = int (input("교환할 돈은?"))

c500=money // 500
money %= 500

c100=money // 100
money %= 50

c10=money // 10
money %= 10

print (c500, c100,c50,c10, money)

print("\n 500원짜리 ==> %d개"%c500)
