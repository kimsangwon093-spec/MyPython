import datetime                     # >> calendar모듈 임포트
today = datetime.date.today()       # >> 변수 today에 실행 시점의 년월일 데이터 타입
birth = datetime.date(1993, 3, 21)  # >> 변수 birth에 생년월일 데이터 대입
print(today - birth)                # >> 2가지 날짜 데이터를 빼서 경과한 일지를 계산해 출력