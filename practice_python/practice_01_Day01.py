# 연습 1 >> 입력한 달의 수 달력 만들기
import calendar

print("보고 싶은 달의 수를 입력 하세요")
month = int(input())                   # input()은 무조건 문자열 함수 
print(calendar.month(2026, month))



