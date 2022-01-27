# 1. w, i, t (전체중, 일일 에너지 섭취량(일일 기초대사량), 일일 기초대사량 역치)
w, i, t = map(int, input().split())
# print(w,i,t)

# 2. d, ni, a (다이어트기간, 기간 일일 에너지 섭취량, 기간 일일 활동 대사량)
d, ni, a = map(int, input().split())

result1 = 0
result2 = 0

w1 = w
w2 = w

i1 = i
i2 = i

for x in range(d):
    w1 += ni - (i1 + a)
    w2 += ni - (i2 + a)

    if abs(ni - (i2 + a)) > t:
        i2 += (ni - (i2 + a)) // 2

    if w1 <= 0 or i1 <= 0:
        result1 = 1

    if w2 <= 0 or i2 <= 0:
        result2 = 1

if result1 == 0:
    print(w1, i1)

else:
    print("Danger Diet")

if result2 == 0:
    print(w2, i2, end=" ")

    if i - i2 > 0:
        print("YOYO")
    else:
        print("NO")

else:
    print("Danger Diet")