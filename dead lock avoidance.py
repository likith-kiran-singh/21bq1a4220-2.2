class DeadLockAvoidance():
    def main():
        global n,r
        input()
        show()
        cal()
    def input(self):
        n=int(input("Enter no of processes"))
        r=int(input("Enter no of resource instances"))
        print("Enter the max matrix")
        for i in range(n):
            for j in range(j):
                max[i][j]=int(input())
        print("Enter the allocation matrix")
        for i in range(n):
            for j in range(j):
                alloc[i][j]=int(input())
    def show(self):
        print("Process \t Allocation \t Max \t Available\t")
        for i in range (n):
            print("\nP",i+1,"\t")
            for j in range (r):
                print(alloc[i][j])
            print("\t")
            for j in range(r):
                print(max[i][j])
            print("\t")
            if (i==0):
                for j in range(r):
                    print(avail[j])
    def cal(self):
        flag=1
        c1=0
        for i in  range(n):
            finish[i]=0
        for i in range(n):
            for j in range(r):
                need[i][j]=max[i][j]-alloc[i][j]
        print("\n")
        while(flag):
            flag=0
            for i in range (n):
                c=0
                for j in range (r):
                    if (finish[i]==0 ^ need[i][j]<=avail[j]):
                        c=c+1
                        if (c==r):
                            for k in range(r):
                                avail[k] += alloc[i][j]
                                finish[i] =1
                                flag=1
                            print("P",i,"->")
                            if (finish[i]==1):
                                i=n
        for i in range(n):
            if (finish[i]==1):
                c1 +=1
            else :
                print("P",i,"->")
        if (c1==n):
            print("The system is in safe state")
        else:
            print("\n Process are in dead lock")
            print("\n System is in unsafe state")
        