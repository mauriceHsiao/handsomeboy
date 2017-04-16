計算方法分析與設計期中考
=========================


請把結果截圖並壓縮成zip，檔名為學號
1. 請至 github 中把handsomeboy.py檔 fork 下來，並以該檔作答，檔名請改成學號(5分)
2. 用lambda算圓面積 πr^2，π請自己設為3.14，半徑為5，請算出面積(10分)
3. 請印出3組10個亂數，且亂數不重複，順序不能一樣(10分)

![Alt text](/3.png)

4. 請根據以下資料，用matplotlib印出圖表，包含title、xlabel、ylabel(25分)
##### date = [2015-1-10,2015-1-11,2015-1-12,2015-1-13,2015-1-14,2015-1-15,2015-1-16,2015-1-17,2015-1-18,2015-1-19,2015-1-20] 
##### temp = [16.7,17.4,17.1,20.3,16.2,16.1,17.5,15.3,16.8,16,18.4]

![Alt text](/4.png)

5. 請參考以下程式碼，並用亂數產生矩陣A跟B，並讓A跟B相加(25分)

```python
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]
def matrix_add(A, B):
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")
    num_rows, num_cols = shape(A)
    def entry_fn(i, j):
        return A[i][j] + B[i][j]
    return make_matrix(num_rows, num_cols, entry_fn)

print matrix_add(A,B)
```

6. 請參考github上的第6題程式碼，並完成以下填空(紅底)
![Alt text](/6.png)
