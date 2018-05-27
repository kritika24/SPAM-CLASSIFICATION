def hidden(input1,wi,bi):
    return (input1*wi)+bi
n=int(input())
while n!=0:
    temp,minX,maxX=map(int,(input().split()))
    nsp=0
    sp=0
    t=[]
    while temp!=0 :
        wi,bi=map(int,(input().split()))
        dat=0
        for input1 in range(minX,maxX+1):
            input1=hidden(input1,wi,bi)
            if input1%2==0:
                nsp=nsp+1
            else:
                sp=sp+1
        #print(nsp,sp)
        temp=temp-1
    t.append(nsp)
    t.append(sp)
    n=n-1
for i in range(0,len(t),2):   
    print(t[i],t[i+1])
