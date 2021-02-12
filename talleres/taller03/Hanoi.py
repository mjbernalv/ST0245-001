def hanoi(N, a = "Tower 1", b = "Tower 2", c = "Tower 3"):
    if N ==1:
        print("Move from " + a + " to " + c)
    else:
        hanoi(N-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(N-1, b, a, c)

hanoi(3)