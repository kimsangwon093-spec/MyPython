# 퀴즈 개수 늘리기
QUESTION = [
    "대한민국의 수도는?",
    "일본의 수도는?",
    "제작자는 몇 살?",
]

R_ANS = [
    "서울",
    "도쿄",
    "33살"
]
for i in range(3):
    print(QUESTION[i])
    ans = input()

    if ans == R_ANS[i]:
        print("정답입니다")
    else:
        print("틀렸습니다.")