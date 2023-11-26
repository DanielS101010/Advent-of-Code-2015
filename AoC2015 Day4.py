from hashlib import md5


def hash_with_leading_zeros(secrete_key, leading_zeros):
    i = 0
    while True:
        hash = md5((secrete_key + str(i)).encode()).hexdigest()

        if hash.startswith(leading_zeros * "0"):
            return i

        i += 1


print(hash_with_leading_zeros("bgvyzdsv", 5))
print(hash_with_leading_zeros("bgvyzdsv", 6))
