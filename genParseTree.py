def disp(parseTreeData):
    noOfTab=0
    flag=0
    for c in parseTreeData:
        if c=="(":
            flag=1
            continue
        if flag==1 and c=="[":
            noOfTab=noOfTab+1
            print "\n"
            printTab(noOfTab)
        elif c==")":
            noOfTab=noOfTab-1
            print "\n"
            printTab(noOfTab)
        print c,

def printTab(n):
    for i in range(0,n):
        print "\t",


