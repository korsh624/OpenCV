r=[0,0,0,0,0,0]
k=0
for i in range(0,6):
    r[i]=int(input())
print(r)
newr=[]
for i in range(0,6):
    t=r[i]
    for j in range(0,6):
        if(r[j]==t):
            if(i!=j):
                newr.append(r[j])
print(newr)
