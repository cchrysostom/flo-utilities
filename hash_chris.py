import hashlib

msg = "Chris"

print(msg, hashlib.sha256(msg.encode(encoding='UTF-8')).hexdigest())
print("----------")

for nonce in range(20):
    input_data = msg + str(nonce)
    print(input_data, hashlib.sha256(input_data.encode(encoding='UTF-8')).hexdigest())

