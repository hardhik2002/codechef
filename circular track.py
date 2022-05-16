# cook your dish here
for _ in range(int(input())):
    a,b,m=map(int,input().split())
    if a>b:
        print(min(a-b,m-a+b))
    else:
        print(min(b-a,a+m-b))
