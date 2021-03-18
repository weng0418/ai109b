import copy as cp
global count

count = 0

class State:
    N = 8
    current_grid = []  # 当前棋盘
    NewQ = (-1, -1)  # 当前棋子的位置
    parent_state = None  # 父状态
    deep = 0  # 状态深度

    def __init__(self, parent_state, Q_ij, NQ):
        if parent_state is None:
            self.N = NQ
            self.NewQ = Q_ij  # 当前棋子的位置
            self.parent_state = parent_state
            self.deep = 0
            self.current_grid = [[0 for i in range(self.N)] for j in range(self.N)]  # 当前棋盘
        else:
            self.N = NQ
            self.NewQ = Q_ij  # 当前棋子的位置
            self.parent_state = parent_state
            self.deep = self.parent_state.deep + 1
            self.current_grid = self.update_grid()  # 当前棋盘

    # 根据父状态和当前棋子位置，对当前棋盘的空余位置情况作更新
    def update_grid(self):
        line = self.NewQ[0]
        column = self.NewQ[1]
        if line != -1 and column != -1:
            if self.parent_state is None:
                next_grid = [[0 for i in range(self.N)] for j in range(self.N)]
                next_grid[line][column] = 10
            else:
                next_grid = cp.deepcopy(self.parent_state.current_grid)
                next_grid[line][column] = 10
                # 向上占位
                while line > 0:
                    next_grid[line - 1][column] = 1
                    line = line - 1
                line = self.NewQ[0]
                # 向下占位
                while line < self.N - 1:
                    next_grid[line + 1][column] = 1
                    line = line + 1
                line = self.NewQ[0]
                # 向左占位
                while column > 0:
                    next_grid[line][column - 1] = 1
                    column = column - 1
                column = self.NewQ[1]
                # 向右占位
                while column < self.N - 1:
                    next_grid[line][column + 1] = 1
                    column = column + 1
                column = self.NewQ[1]
                # 向左下角占位
                while column > 0 and line < self.N - 1:
                    next_grid[line + 1][column - 1] = 1
                    column = column - 1
                    line = line + 1
                line = self.NewQ[0]
                column = self.NewQ[1]
                # 向右下角占位
                while column < self.N - 1 and line < self.N - 1:
                    next_grid[line + 1][column + 1] = 1
                    column = column + 1
                    line = line + 1
            return next_grid
        else:
            print("no solution here!")
            return None

    # 打印当前棋盘
    def show_grid(self):
        for i in range(len(self.current_grid)):
            print("|", end="")
            for j in range(len(self.current_grid[i])):
                if self.current_grid[i][j] == 1:
                    print(" ", end=" ")
                else:
                    print("Q", end=" ")
            print("|")
        print("****-----------------*****\n*****-----------------****")


def get_extended_space_list(current_state, NQ):
    global count
    res_list = []
    if current_state.parent_state is None:
        line = 0
        for column in range(len(current_state.current_grid[line])):
            if current_state.current_grid[line][column] == 0:
                res_list.append((line, column))
    else:
        line = current_state.NewQ[0] + 1
        column = 0
        while column <= NQ - 1:
            count += 1
            if current_state.current_grid[line][column] >= 1:
                column = column + 1
            else:
                res_list.append((line, column))
                column = column + 1
    return res_list


NQ = 10
start_grid = [[0 for i in range(NQ)] for j in range(NQ)]
start_Q_ij = (-1, -1)
start_state = State(None, start_Q_ij, NQ)
start_space = get_extended_space_list(start_state, NQ)
open_list = []
solution = 0  # 记录成功结果的数量
search_sum = 0  # 记录找到单个结果时所用搜索次数
sum_in_total = 0  # 记录所有成功结果的搜索次数和
for i in range(len(start_space)):
    new = State(start_state, start_space[i], NQ)
    open_list.insert(0, new)
while len(open_list) != 0:
    # search_sum = search_sum + 1
    # print(len(open_list))
    current_state = open_list.pop(0)
    if current_state.deep == NQ:  # 如果当前状态的deep为NQ，说明所有棋子都放置完毕，即得到一种解
        solution = solution + 1
        print("this is solution No.", solution, sep="")
        current_state.show_grid()
        sum_in_total = sum_in_total + search_sum
        print("search_sum = ", search_sum)
        search_sum = 0
        continue
    new_space = get_extended_space_list(current_state, NQ)  # 得到可放置棋子的位置坐标列表
    for i in range(len(new_space)):
        search_sum += 1
        new_state = State(current_state, new_space[i], NQ)
        open_list.insert(0, new_state)

print("\n\n******************\nThere are ", solution, " solutions to ", NQ, "-Queens problem in total!", sep="")
# print("平均搜索次数为", sum_in_total / solution)
print("平均搜索次数为%.3f" % (count / solution))