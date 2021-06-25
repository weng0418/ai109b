# Week1
# 爬山演算法  
## 爬山算法是一種簡單的貪心搜索算法，該算法每次從當前解的臨近解空間中選擇一個最優解作爲當前解，直到達到一個局部最優解。爬山算法實現很簡單，其主要缺點是會陷入局部最優解，而不一定能搜索到全局最優解。

### 通用的爬山演算法架構
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
### 抽象的解答類別
```
class Solution: # 解答的物件模版 (類別)
    def __init__(self, v, step = 0.01):
        self.v = v       # 參數 v 為解答的資料結構
        self.step = step # 每一小步預設走的距離

    # 以下兩個函數至少需要覆蓋掉一個，否則會無窮遞迴
    def height(self): # 爬山演算法的高度函數
        return -1*self.energy()               # 高度 = -1 * 能量

    def energy(self): # 尋找最低點的能量函數
        return -1*self.height()               # 能量 = -1 * 高度
```
