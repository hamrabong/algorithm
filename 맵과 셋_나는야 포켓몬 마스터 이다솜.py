import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pkmn = []  # 포켓몬 이름을 저장할 list
pkmn_dic = {}  # 포켓몬 이름에 따른 번호를 저장할 dictionary

for i in range(n):
    pk = input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1

for _ in range(m):

    query = input().rstrip()

    # query가 숫자이면 list에서 조회 후 출력
    if query.isdigit():
        print(pkmn[int(query) - 1])
    # query가 문자열이면 dictionary에서 조회 후 출력
    else:
        print(pkmn_dic[query])