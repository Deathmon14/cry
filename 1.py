def caesar(text, shift):
    res = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            res += chr((ord(ch) - base + shift) % 26 + base)
        else:
            res += ch
    return res

msg = "HELLO"
enc = caesar(msg, 3)
dec = caesar(enc, -3)
print("Encrypted:", enc)
print("Decrypted:", dec)
