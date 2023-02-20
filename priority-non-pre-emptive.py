n=int(input("Enter no. of processes : "))
print("Enter the Processes-ID,Burst Time,Priority : ")
l=[]
for i in range(n):
    l.append(list(map(int,input("\t\t").split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][2]>l[j][2]:
            #sorting the priority order
            l[i],l[j]=l[j],l[i]
ct=0
for i in  range(n):
    ct += l[i][1]
    l[i].append(ct)
tat,wt=0,0
print("PID BT  Priority   AT   TAT   WT")
for i in range(n):
    print(l[i][0],"   ",l[i][1],"   ",l[i][2],"   ",0,"   ",l[i][3],"  ",l[i][3]-l[i][1])
tat,wt=0,0
for i in range(n):
    tat += l[i][3]
    wt  += l[i][3]-l[i][1]
print("avg TAT:",tat/n)
print("avg WT:",wt/n)