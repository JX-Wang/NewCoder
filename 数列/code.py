while 1:
    n = input()
    a = [1, 2]
    while n >= 1:
        try:
            k = input()
            if k > 2:
                for i in range(2, k):
                    a[0], a[1] = a[1], 2*a[1] + a[0]
                    a[i] = a[1]
                print a[1] % 32767
            elif k == 1:
                print a[0] % 32767
            else:
                print a[1] % 32767
        except Exception as e:
            break
        n -= 1