#1
def solve(a):
    return sum(a)


#2
natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i): # str로 변형시켜 8, 5, 1로 해서 하나씩 받은 다음 int로 하여 더하기
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)


#3
n = int(input())

hansu = 0

for i in range(1, n + 1):
    if i < 100:
        hansu += 1
    else:
        n_str = list(map(int, str(i))) # 숫자를 자릿수를 기준으로 분류해서 나누는 방법
        if n_str[1] - n_str[0] == n_str[2] - n_str[1]:
            hansu += 1

print(hansu)