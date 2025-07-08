import hashlib
import time

def proof_of_work(nickname: str, difficulty: int):
    prifix = '0' * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        input_data = f"{nickname}{nonce}".encode('utf-8')
        hash_result = hashlib.sha256(input_data).hexdigest()
        if hash_result.startswith(prifix):
            elapsed = time.time() - start_time
            print(f"\n✅ Found hash with {difficulty} leading zeros:")
            print(f"Input      : {nickname}{nonce}")
            print(f"Nonce      : {nonce}")
            print(f"Hash       : {hash_result}")
            print(f"Time Taken : {elapsed:.4f} seconds")
            return
        nonce += 1

nickname = "thneonl"

# 第一次：4个0
proof_of_work(nickname, difficulty=4)

# 第二次：5个0
proof_of_work(nickname, difficulty=5)



# (base) ➜  BaseDemo git:(main) ✗ uv run pow.py

# ✅ Found hash with 4 leading zeros:
# Input      : thneonl248388
# Nonce      : 248388
# Hash       : 000080e4b7a175fefabffc6361fd210a60168e8454caa6f783ac0aea4fe1a701
# Time Taken : 0.5312 seconds

# ✅ Found hash with 5 leading zeros:
# Input      : thneonl1756269
# Nonce      : 1756269
# Hash       : 000009e644872792a6b373be4683f7f7a9b7f519ca3dbdc1b0970a139e5f455d
# Time Taken : 3.0648 seconds