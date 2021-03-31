def n_queen(k):
    global count

    for i in range(k - 1):  # 判斷是否可放置皇后的條件
        judge = queen[i] - queen[k - 1]
        if judge == 0 or abs(k - 1 - i) == abs(judge):
            return

    if k == n:
        print(queen)  # 輸出皇后放置序列
        count += 1  # 解的個數
        return

    for i in range(n):  # 放置皇后
        queen[k] = i
        n_queen(k + 1)

count = 0
n = 8  # 此處的n為幾，則為幾皇后問題
queen = [0 for _ in range(n)]
n_queen(0)
print(count)