def sjf(process,n):
    process=sorted(process,key=lambda x:x[1])
    wt=0
    unitsum=0
    turn_sum=0
    print("Process \t BurstTime \t WaitingTime \t TurnAroundTime")
    for i in range(n):
        turn=wt+process[i][1]
        print("p"+str(process[i][0])+"\t\t"+str(process[i][1])+"\t\t"+str(wt)+"\t\t"+str(turn))
        wt += process[i][1]
        waitsum += wt
        turn_sum += turn
    waitsum -= wt
    avgwaittime=round(waitsum/n,3)
    avgturntime=round(turn_sum/n,3)
    return(avgwaittime,avgturntime)
if __name__=="__main__":
    n=int(input("Enter no. of processes :"))
    process=[]
    for i in range(1,n+1):
        process.append((int(input("Enter BT:"))))
    print("\n Shortest Job First Scheduling :")
    res=sjf(process,n)
    print("\n Average Waiting Time=",res[0])
    print("\t Average Turn Around Time=",res[i])