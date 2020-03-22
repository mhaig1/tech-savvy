encrypted_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

encrypted_msg = 'map'


orginal_msg = ""

for letter in encrypted_msg:
    if letter.isalpha():
        decrypted_letter = chr(ord(letter) + 2)
    else:
        decrypted_letter = letter
    orginal_msg += decrypted_letter


print(orginal_msg)