N, M = map(int, input().split())
t = list(map(int, input().split()))
end = max(t)
start = 1
while start <= end:
    mid = (start + end) // 2
    m = 0
    for i in t:
        if i >= mid:
            m += i - mid

    if m >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
