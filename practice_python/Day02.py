# print() >> 출력함수

import calendar

print("지금부터 파이썬에 대해 공부할 예비 프로그래머 입니다.")

u_name = "김상원"
u_age = "33"

print("이 유저의 이름은 " + u_name + " 이고 나이는 " + u_age + "세 입니다.")

# input() >> 입력함수
print("당신의 이름은? >>")
name = input()
print("저의 이름은 " + name + " 입니다.")

# 연습 1 >> 입력한 달의 수 달력 만들기
print("보고 싶은 달의 수를 입력 하세요")
month = int(input())                   # input()은 무조건 문자열 함수 
print(calendar.month(2026, month))
