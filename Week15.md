# Week15
## Colab 
* Colaboratory 簡稱Colab，是Google Research 團隊開發的一款產品。在Colab 中，任何人都可以通過瀏覽器編寫和執行任意Python 代碼。它尤其適合機器學習、數據分析和教育目的。從技術上說，Colab是一種託管式Jupyter 筆記本服務。用戶無需進行設置，就可以直接使用，同時還能獲得GPU 等計算資源的免費使用權限。
### 優點
* 使用雲端空間，不用自己的電腦空間。
* 免費用Colab的GPU算力，執行epoch的速度很快。
* 可以跳過Mac、Win的各種坑，硬體設定省心。
* 手機平板也可以執行，但建議只用來看成果，因為容易斷線。
### 缺點
* 課程資料超過20G，超過免費的google雲端硬碟容量，也就是要租空間或有免費的教育方案，有些學校有提供校友免費申請，不妨花時間找找，付費資訊參閱google說明。
* Colab設定需要填坑。
* 一定要有網路。 

## 循環神經網路(RNN)
* 循環神經網路（Recurrent neural network：RNN）是神經網路的一種。單純的RNN因為無法處理隨著遞歸，權重指數級爆炸或梯度消失問題，難以捕捉長期時間關聯；而結合不同的LSTM可以很好解決這個問題。
* 時間循環神經網路可以描述動態時間行為，因為和前饋神經網路（feedforward neural network）接受較特定結構的輸入不同，RNN將狀態在自身網路中循環傳遞，因此可以接受更廣泛的時間序列結構輸入。手寫識別是最早成功利用RNN的研究結果。
![image](https://user-images.githubusercontent.com/62419535/123520763-e18e0280-d6e4-11eb-9c5e-206578ff0081.png)

# 資料取自維基百科:[循環神經網路](https://zh.wikipedia.org/wiki/%E5%BE%AA%E7%8E%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)
# 圖片出處:[循環神經網絡](https://arbu00.blogspot.com/2017/05/3-rnn-recurrent-neural-networks.html)

## One-hot
* One-hot在數位電路中被用來表示一種特殊的位元組合，該位元組裏，僅容許單一位元爲1，其他位元都必須爲0。之所以稱爲one-hot就是因爲只能有一個1（hot）。若情況相反，只有一個0，其餘爲1，則稱爲one-cold[1]。在機器學習裏，也有one-hot向量（英語：one-hot vector）的概念。在一任意維度的向量中，僅有一個維度的值是1，其餘爲0。譬如向量[000001000000000]，即爲15維空間中的一組one-hot向量。將類別性資料轉換成one-hot向量的過程則稱one-hot編碼（英語：one-hot encoding）。在統計學中，虛擬變數代表了類似的概念。
* One-hot目前並無公認或被廣泛使用的中文譯名。目前可見的one-hot encoding譯名有獨熱編碼以及一位有效編碼。
![image](https://user-images.githubusercontent.com/62419535/123520886-bce65a80-d6e5-11eb-8187-3e6740e25f37.png)

# 資料取自維基百科:[One-hot](https://zh.wikipedia.org/wiki/One-hot)
