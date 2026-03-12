# puzzle 1

encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# print(f'g -> {chr(ord("g") + 2)}')
# print(f'f -> {chr(ord("f") + 2)}')
# print(f'm -> {chr(ord("m") + 2)}')
# print(f'n -> {chr(ord("n") + 2)}')
# print(f'c -> {chr(ord("c") + 2)}')


def decrypt(data, shift=2):
    s = []
    for c in data:
        if c.isalpha():
            if ord(c) + shift > ord("z"):
                s.append(chr(ord(c) + shift - 26))
            else:
                s.append(chr(ord(c) + shift))
        else:
            s.append(c)
    return "".join(s)


print(decrypt(encrypted))
print(decrypt("map"))

# for i in range(25):
#     print(f"shift = {i}: {decrypt(encrypted, shift=i)}")
