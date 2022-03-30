import sys
from collections import deque

n,m=map(int,input().split())
start=[deque(), deque()]
temp=[deque(),deque()]

for i in range(n):
    a,b=map(int,input().split())
    start[0].appendleft(a)
    start[1].appendleft(b)

t=0
for _ in range(m):
    temp[t].appendleft(start[t].popleft())
    if not start[t]:##둘 중 하나라도 0이 되면
        break
    win=-1
    for i in [0,1]:
        if temp[i] and temp[i][0]==5: # 둘중 하나가 5
            win=0
    if temp[0] and temp[1] and temp[0][0]+temp[1][0]==5:
            win=1
    if win!=-1:##종 치지 않을 경우 pass
        for i in [1-win,win]: ##누구 카드를 먼저 가져오는지
            while temp[i]:
                start[win].append(temp[i].pop())
    t=1-t

if len(start[0])>len(start[1]):
    print('do')
elif len(start[1])>len(start[0]):
    print('su')
else:
    print('dosu')