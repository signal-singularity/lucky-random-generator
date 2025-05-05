# Random

> 中文介紹: [README.zh.md](./README.zh.md)

This is a random algorithm validator. The results are generated based on the latest ETH block data at the time of the draw to create a random seed. This algorithm ensures unpredictable results that can be reproduced and verified afterward, making it suitable for lottery activities.

The code here is a Python implementation, identical to the original version, and can be used to verify whether the results have been tampered with.

### Data

```python
block = {
    "number": "22419349", # Block number
    "time": "1746470015", # Block generation time
    "miner": "0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5",  # Miner ID
    "count": 1,  # Number of operations
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
    "Novvy"
]
```

### Result

```bash
Winner: Novvy - Prize: P1
Total number: 1
```