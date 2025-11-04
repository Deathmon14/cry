def vigenere(msg, key):
    msg, key = msg.upper(), key.upper()
    key = (key * (len(msg)//len(key)+1))[:len(msg)]
    cipher = ""
    for m, k in zip(msg, key):
        cipher += chr(((ord(m)+ord(k)) % 26) + 65)
    return cipher

print("Encrypted:", vigenere("ATTACKATDAWN", "LEMON"))
