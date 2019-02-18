```pyhton
while 1:
    try:
        s = raw_input()
        s = s.split()
        print str(int(s[0]) * int(s[1]))
    except:
        break
```
