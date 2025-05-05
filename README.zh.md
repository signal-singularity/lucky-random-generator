# Random

> English: [README.md](./README.md)

這是一個隨機演算法驗證器。結果基於開獎時最新的 ETH 區塊數據生成，用於創建隨機種子。該演算法確保結果不可預測，且可在之後重現和驗證，非常適合彩票活動。

此處的程式碼是 Python 實現，與原始版本完全相同，可用於驗證結果是否已被竄改。

### Data

```python
block = {
    "number": "22419349", # 區塊編號
    "time": "1746470015", # 區塊生成時間
    "miner": "0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5",  # 礦工編號
    "count": 1,  # 計算操作數
}
```

> ⚠️ 獎品及成員順序必須與原始資料完全一致，建議從 MiniAPP 匯出資料。
```python
# 獎品 [名稱, 數量]
prizes = [
    ["P1",  3],
    ["P2",  3],
]
# 成員名稱
memebers = [
    "Novvy"
]
```

### Result

```bash
Winner: Novvy - Prize: P1
Total number: 1
```