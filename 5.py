import numpy as np

def hill(msg, key):
    msg = msg.upper()
    if len(msg)%2 != 0:
        msg += 'X'
    enc = ''
    for i in range(0, len(msg), 2):
        pair = np.array([[ord(msg[i])-65], [ord(msg[i+1])-65]])
        res = np.dot(key, pair) % 26
        enc += ''.join([chr(val[0]+65) for val in res])
    return enc

key = np.array([[3,3],[2,5]])
print("Encrypted:", hill("HI", key))
