# HW3(Truthtable)

## [程式碼](https://github.com/weng0418/ai109b/blob/main/homework/work3/HW3.py):
```
def truthTable(n):       # 列出 n 變數的所有可能 0,1 排列
	p = []                 # p 代表已經排下去的，一開始還沒排，所以是空的
	return tableNext(n, p) # 呼叫 tableNext 遞迴下去排出所有可能

def tableNext(n, p):
	i = len(p)             # i 是下一個排列的位置
	if i == n:		         # 全部排好了
		print(p)	           # 印出排列
		return               # 返回上層
	for x in [0,1]:        # x 是 0 或 1
		p.append(x)		       # 把 x 放進表
        #print(p)
		tableNext(n, p)	     # 繼續遞迴尋找下一個排列
        #print(p)
		p.pop()			         # 把 x 移出表
        #print(p)
        
truthTable(4)            # 印出4變數的真值表
```

* 參考老師程式範例，並加以註解

## [輸出結果:](https://github.com/weng0418/ai109b/blob/main/homework/work3/HW3.png)
```
[0, 0, 0, 0]
[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 1]
[0, 1, 0, 0]
[0, 1, 0, 1]
[0, 1, 1, 0]
[0, 1, 1, 1]
[1, 0, 0, 0]
[1, 0, 0, 1]
[1, 0, 1, 0]
[1, 0, 1, 1]
[1, 1, 0, 0]
[1, 1, 0, 1]
[1, 1, 1, 0]
[1, 1, 1, 1]
```
