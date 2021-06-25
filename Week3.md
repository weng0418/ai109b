# Week3
# 遺傳演算法
## 說明
### 遺傳演算法是一類借鑒生物界的進化規律（適者生存，優勝劣汰遺傳機制）演化而來的隨機化搜索方法。它是由美國的J.Holland教授1975年首先提出，其主要特點是直接對結構對象進行操作，不存在求導和函數連續性的限定；具有內在的隱並行性和更好的全局尋優能力；採用概率化的尋優方法，能自動獲取和指導優化的搜索空間，自適應地調整搜索方向，不需要確定的規則。遺傳演算法的這些性質，已被人們廣泛地應用於組合優化、機器學習、信號處理、自適應控制和人工生命等領域。它是現代有關智能計算中的關鍵技術之一。
### keyGa.py
```
from geneticAlgorithm import GeneticAlgorithm
import random

class KeyGA(GeneticAlgorithm):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def randomChromosome(self): # 隨機產生一個染色體 (一個 16 位元的 01 字串)
        bits=[]
        for _ in range(len(self.key)):
            bit = str(random.randint(0,1))
            bits.append(bit)
        return ''.join(bits)
  
    def calcFitness(self, c): # 分數是和 key 一致的位元個數
        fitness=0
        for i in range(len(self.key)):
            fitness += 1 if c[i]==self.key[i] else 0
        return fitness
  
    def crossover(self, c1, c2):
        cutIdx = random.randint(0, len(c1)-1)
        head   = c1[0:cutIdx]
        tail   = c2[cutIdx:]
        return head + tail
    
    def mutate(self, chromosome): # 突變運算
        i=random.randint(0, len(chromosome)-1) # 選擇突變點
        cMutate = chromosome[0:i]+random.choice(['0','1'])+chromosome[i+1:] # 在突變點上隨機選取 0 或 1
        return cMutate # 傳回突變後的染色體

# 執行遺傳演算法，企圖找到 key，最多執行一百代，每代族群都是一百人
kga = KeyGA("1010101010101010")
kga.run(100, 20)
```
# 加密演算法
## XOR加密
### XOR算法原理是:當一個數A和另一個數B進行異或運算會生成另一個數C，如果再將C和B進行異或運算則C又會還原為A。

### 相對於其他的簡易加密算法，XOR算法的優點如下。

* (1)算法簡單，對於高級語言很容易能實現。

* (2)速度快，可以在任何時候、任何地方使用。

* (3)對任何字符都是有效的，不像有些簡易加密算法，只對西文字符有效，對中文加密後再解密無法還原為原來的字符。

## 凱薩密碼
### 凱撒密碼是密碼學中，一種最簡單的加密算法。原理並不復雜，只要理解了，實現起來並不困難。凱薩密碼是一種針對英文字母的加密法，它能使一篇英文文章不會被外人閱讀，對外人而言只是一串亂碼，概念很簡單，就是把字母位移固定的量(稱為偏移量)！

## 維吉尼亞密碼
### 是使用一系列凱撒密碼組成密碼字母表的加密算法，屬於多表密碼的一種簡單形式。
##  原理
### 在一個凱撒密碼中，字母表中的每一字母都會作一定的偏移，例如偏移量為3時，A就轉換為了D、B轉換為了E……而維吉尼亞密碼則是由一些偏移量不同的愷撒密碼組成。為了生成密碼，需要使用表格法。這一表格包括了26行字母表，每一行都由前一行向左偏移一位得到。具體使用哪一行字母表進行編譯是基於密鑰進行的，在過程中會不斷地變換。

# 補充
