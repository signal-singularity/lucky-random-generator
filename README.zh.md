# Random

> English: [README.md](./README.md)

這是一個隨機演算法驗證器。結果基於開獎時最新的 ETH 區塊數據生成，用於創建隨機種子。該演算法確保結果不可預測，且可在之後重現和驗證，非常適合彩票活動。

此處的程式碼是 Python 實現，與原始版本完全相同，可用於驗證結果是否已被竄改。

### Data

```python
block = {
    "number": "0x157acfe", # Block number (HEX)
    "hash": "0x8a826e6c3cbeacc82937ad7b6a821a6a25b63383bc05eb0ddb807bb41c518d34", # Block hash
    "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97",  # Miner ID
    "time": "0x682c4633", # Block generation time (HEX)
    "count": 1  # Number of operations
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
    "User1",
    "User2",
]
```

### Result

```bash
Winner: User2 - Prize: P2
Winner: User1 - Prize: P2
Total number: 2
```