n=int(input())
try: 
    lst=list(map(int,input().split()))
    lst.sort()
    for i in range(1,n+1):
        if lst[i-1]!=i: 
            print(i)
            break    
except:
    print(n)