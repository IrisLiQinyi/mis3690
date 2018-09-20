def move(n,source,bridge,destination):
    if n == 1:
        print (source,bridge)
        return
    else:
        move(n-1,destination,source,bridge)
        print (n,source,bridge)
        move(n-1,destination,bridge,source)
move(4,'A','B','C')