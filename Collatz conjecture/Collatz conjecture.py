for i in range(1, 10000000000):
    temp = i
    while True:
        if temp == 1:
            break
        elif temp % 2 != 0:
            temp = (temp * 3) + 1
        elif temp % 2 == 0:
            temp = temp / 2
    print(i)

