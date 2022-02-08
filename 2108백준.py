n = int(input())

array = []
mode = [[0, 0]] * n
for i in range(n):
    array.append(int(input()))

array.sort()
print(mode[0])
print(round(sum(array) / n))
print(array[int((n - 1) / 2)])
for i in range(n):
    if mode[i] == [0, 0]:
        mode[i] = [1, array[i]]
    else:
        mode[i] = mode[i] + [1, 0]
if n > 1:
    if mode[0] == mode[1]:
        print(mode[1])
    else:
        print(mode[0])
else:
    print(mode[0])
print(max(array) - min(array))

# 최빈값 아직 못구함
# 산술평균 : round(total / N)
# 중앙값 : array[int(n-1)/2)]
# 최빈값 : 가장 많이 나타나는 값? 두번째로 작은 값
# 범위 : max(array) - min(array)
