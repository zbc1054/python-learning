i = 1
print("-"*60)
while i <= 10:
    n = 1
    while n <= 10:
        print("{:5d}".format(i*n),end = '')
        n += 1
    print()
    i += 1
print("-"*60)
