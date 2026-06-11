# for 구문
# for i in range(1, 5):
#   print(i)
# range (반복횟수) >> 0 에서 시작하며, 지정한 횟수만큼 반복
# range (시작값, 종료값) >> 변수값 시작값에서 시작하며, 종료값까지 반복
# range (시작값, 종료값, 증감값) >> 변수를 지정한 값

print("방탈출 게임")
print("[system] >> 당신은 방에 갇혔다. 그래서 탈출 해야만 한다.")

item = ["커터칼조각", "클립"]
print("방을 조사하던중 이상한 물건을 발견 하였다")
print("조사 해볼까요?")

print("yes")
print("no")
yorn = input()

if yorn == "yes":
    print("자물쇠로 잠긴 작은 상자를 찾았다")
    item.append("자물쇠로 짐긴 상자")
    print(item)

if yorn == "no":
    print("일단은 그냥 두었다")

print("클립으로 잠물쇠를 해제 합니다")
print("yes")
print("no")
using = input()

if using == "yes":
    print("방열쇠를 입수했다")
    item.append("열쇠")
    item.remove("클립")
    item.remove("자물쇠로 짐긴 상자")
    print(item)

print("이제 당신은 문을 열고 나갈수 있습니다")
print("나가시겠습니까?")

print("yes")
print("no")
esc = input()

if esc == "yes":
    print("당신은 탈출 하였습니다!")
    item.remove("열쇠")
    print(item)

if esc == "no":
    print("좀더 조사를 하기로 합니다")



