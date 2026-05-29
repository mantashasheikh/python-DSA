# recursion
def tail(i):
    if i==0:
        return
    print(i)
    tail(i-1)
tail(5)    