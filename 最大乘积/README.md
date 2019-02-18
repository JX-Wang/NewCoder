```python
while 1:
    try:
        item = raw_input()
        n = item.split(" ")
        m = []
        for i in n:
            m.append(int(i))
        m.sort()
        if len(m) == 3:
            t = m[0] * m[1] * m[2]
            print t
        elif len(m) > 3:
            x1, x2 = m[0], m[1]
            m.reverse()
            y1, y2 = m[0], m[1]
            a = x1 * x2 * y1
            b = x1 * x1 * y2
            c = y1 * y2 * x1
            d = y1 * y2 * x2
            temp = []
            temp.append(a)
            temp.append(b)
            temp.append(c)
            temp.append(d)
            temp.sort()
            print temp[3]
        else:
            pass
    except:
        break
```
