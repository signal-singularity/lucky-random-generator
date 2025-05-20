# Random

> 中文介紹: [README.zh.md](./README.zh.md)

This is a random algorithm validator. The results are generated based on the latest ETH block data at the time of the draw to create a random seed. This algorithm ensures unpredictable results that can be reproduced and verified afterward, making it suitable for lottery activities.

The code here is a Python implementation, identical to the original version, and can be used to verify whether the results have been tampered with.

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

> ⚠️ The order of prizes and members must be exactly the same as the original data. It is recommended to export the data from MiniAPP.
```python
# Prizes [Name, Count]
prizes = [
    ["P1",  3],
    ["P2",  3],
]
# Member names
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