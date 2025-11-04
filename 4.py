p, g = 23, 5
a, b = 6, 15
A = pow(g, a, p)
B = pow(g, b, p)
secretA = pow(B, a, p)
secretB = pow(A, b, p)
print("Alice Key:", A)
print("Bob Key:", B)
print("Shared Secret (Alice):", secretA)
print("Shared Secret (Bob):", secretB)
