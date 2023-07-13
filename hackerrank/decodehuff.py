def decodeHuff(root, s):
    result=''
    main=root
    c=0
    while c<len(s):
        if (root.left==None and s[c]=='0' ) or (root.right==None and s[c]=='1'):
            result+=root.data
            root=main
        if s[c]=='1':
            root=root.right
        elif s[c]=='0':
            root=root.left
        c+=1
    result+=root.data
    print(result)
    return result