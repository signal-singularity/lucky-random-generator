block = {
    "number": "22419349",
    "time": "1746470015",
    "miner": "0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5",
    "count": 1,
}

# Generate the seed
seed = block["number"] + block["time"] + block["miner"]

hash_value = 0
for char in seed:
    hash_value = (hash_value << 5) - hash_value + ord(char)
    hash_value &= 0xFFFFFFFF  # Simulate 32-bit integer overflow

# Random number generator
def get_random_int(max_value: int) -> int:
    global hash_value
    hash_value = (hash_value * 9301 + 49297) % 233280
    return abs(hash_value) % max_value

# Data
prizes = [
    ["P1",  3],
    ["P2",  3],
]
memebers = [
    "Novvy"
]

min_value = min(len(prizes), len(memebers))

total_count = 0
while min_value > 0:
    total_count += 1

    # Select a random prize
    prize_index = get_random_int(len(prizes))
    prize = prizes[prize_index]
    if prize[1] == 0:
        prizes.pop(prize_index)
        continue

    # Select a random member
    member_index = get_random_int(len(memebers))
    member = memebers[member_index]

    # Add winner
    print(f"Winner: {member} - Prize: {prize[0]}")

    # Update data
    memebers.pop(member_index)
    prizes[prize_index][1] -= 1
    min_value -= 1

print(f"Total number: {total_count}")