def Ways(n):
    if n<=2:
        return n
    return Ways(n-1)+Ways(n-2)

print(Ways(4))
print(Ways(2))
print(Ways(3))

