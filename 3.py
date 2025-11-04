def gcd(a,b): return b if a==0 else gcd(b,a%b)

def modinv(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x

p, q = 17, 11
n = p*q
phi = (p-1)*(q-1)
e = 7
d = modinv(e, phi)
msg = 12

enc = pow(msg, e, n)
dec = pow(enc, d, n)

print("Public Key:", (e,n))
print("Private Key:", d)
print("Encrypted:", enc)
print("Decrypted:", dec)
