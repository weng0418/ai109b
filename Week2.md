# Week2
# 爬山演算法

## 課堂實作:

### hillClimbing.py
```
def hillClimbing(s, maxGens, maxFails):   # 爬山演算法的主體函數
    print("start: ", s.str())             # 印出初始解
    fails = 0                             # 失敗次數設為 0
    # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
    for gens in range(maxGens):
        snew = s.neighbor()               #  取得鄰近的解
        sheight = s.height()              #  sheight=目前解的高度
        nheight = snew.height()           #  nheight=鄰近解的高度
        if (nheight >= sheight):          #  如果鄰近解比目前解更好
            print(gens, ':', snew.str())  #    印出新的解
            s = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    print("solution: ", s.str())          #  印出最後找到的那個解
    return s                              #    然後傳回。
```
### solutionScheduling.py
```
from random import random, randint, choice
from solution import Solution
import numpy as np

courses = [
{'teacher': '  ', 'name':'　　', 'hours': -1},
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

cols = 7

def randSlot() :
    return randint(0, len(slots)-1)

def randCourse() :
    return randint(0, len(courses)-1)


class SolutionScheduling(Solution) :
    def neighbor(self):    # 單變數解答的鄰居函數。
        fills = self.v.copy()
        choose = randint(0, 1)
        if choose == 0: # 任選一個改變 
            i = randSlot()
            fills[i] = randCourse()
        elif choose == 1: # 任選兩個交換
            i = randSlot()
            j = randSlot()
            t = fills[i]
            fills[i] = fills[j]
            fills[j] = t
        return SolutionScheduling(fills)                  # 建立新解答並傳回。

    def height(self) :      # 高度函數
        courseCounts = [0] * len(courses)
        fills = self.v
        score = 0
        # courseCounts.fill(0, 0, courses.length)
        for si in range(len(slots)):
            courseCounts[fills[si]] += 1
            #                        連續上課:好                   隔天:不好     跨越中午:不好
            if si < len(slots)-1 and fills[si] == fills[si+1] and si%7 != 6 and si%7 != 3:
                score += 0.1
            if si % 7 == 0 and fills[si] != 0: # 早上 8:00: 不好
                score -= 0.12
        
        for ci in range(len(courses)):
            if (courses[ci]['hours'] >= 0):
                score -= abs(courseCounts[ci] - courses[ci]['hours']) # 課程總時數不對: 不好
        return score

    def str(self) :    # 將解答轉為字串，以供印出觀察。
        outs = []
        fills = self.v
        for i in range(len(slots)):
            c = courses[fills[i]]
            if i%7 == 0:
                outs.append('\n')
            outs.append(slots[i] + ':' + c['name'])
        return 'score={:f} {:s}\n\n'.format(self.energy(), ' '.join(outs))
    
    @classmethod
    def init(cls):
        fills = [0] * len(slots)
        for i in range(len(slots)):
            fills[i] = randCourse()
        return SolutionScheduling(fills)
```
* hilClimginScheduling.py
```
from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionScheduling import SolutionScheduling # 引入平方根解答類別

# 執行爬山演算法 (最多3萬代、失敗一千次就跳出)
hillClimbing(SolutionScheduling.init(), 30000, 1000)
```

# 模擬退火法
### 模擬退火其實也是一種貪心演算法，但是它的搜尋過程引入了隨機因素。在迭代更新可行解時，以一定的概率來接受一個比當前解要差的解，因此有可能會跳出這個區域性的最優解，達到全域性的最優解。以下圖為例，假定初始解為左邊藍色點A，模擬退火演算法會快速搜尋到區域性最優解B，但在搜尋到區域性最優解後，不是就此結束，而是會以一定的概率接受到左邊的移動。也許經過幾次這樣的不是區域性最優的移動後會到達全域性最優點D，於是就跳出了區域性最小值。

## 補充內容
<img src="img/Week2-1.jpg"> 
<img src="img/Week2-2.jpg"> 
