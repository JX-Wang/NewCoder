while 1:
    try:
        s = raw_input()
        temp = []
        for i in s:
            if i not in temp:
                temp.append(i)
            else:
                pass
        temp = "".join(temp)
        print temp
    except:
        break
