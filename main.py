import hashlib

block = {
    "number": "0x157acfe",
    "hash": "0x8a826e6c3cbeacc82937ad7b6a821a6a25b63383bc05eb0ddb807bb41c518d34",
    "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97",
    "time": "0x682c4633",
    "count": 1
}

prizes = [
    ["P1",  3],
    ["P2",  3],
]

memebers = [
    "User1",
    "User2",
]

# Generate the seed
seed_input = block["number"] + block["hash"] + block["miner"] + block["time"]
seed = hashlib.sha256(seed_input.encode()).hexdigest()

hash_value = 0
for char in seed:
    hash_value = (hash_value << 5) - hash_value + ord(char)
    hash_value &= 0xFFFFFFFF  # Simulate 32-bit integer overflow

# Random number generator
def get_random_int(max_value: int) -> int:
    global hash_value
    hash_value = (hash_value * 9301 + 49297) % 233280
    return abs(hash_value) % max_value

memebers = memebers[::-1]

prizes_count = 0
for i in prizes:
    prizes_count += i[1]

min_value = min(prizes_count, len(memebers))

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
