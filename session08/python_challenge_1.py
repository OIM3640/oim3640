def decrypt(message):
    """
    Return a decrypted message
    """
    new_message = ""
    for c in message:
        if c.isalpha() and c!='y' and c!='z':
            c = chr(ord(c) + 2)
        elif c == 'y':
            c = 'a'
        elif c == 'z':
            c = 'b'
        new_message += c
    return new_message

hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(decrypt(hint))
print(decrypt('map'))
    
        