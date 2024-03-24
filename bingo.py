import random

def bingo_init():
    bingo=[[0]*5 for _ in range(5)]
    bingo[2][2]="x"
    return bingo

def gen_bingo(bingo):
    for i in range(5):
        for j in range(5):
            while True:
                if i==0:
                    temp=random.randint(1,15)
                elif i==1:
                    temp=random.randint(16,30)
                elif i==2:
                    temp=random.randint(31,45)
                elif i==3:
                    temp=random.randint(46,60)
                else:
                    temp=random.randint(61,75)
                if temp not in bingo[i]:
                    break
            if bingo[i][j]!="x":
                bingo[i][j]=temp
    return bingo

def bingo_machine():
    return random.randint(1,75)

def bingo_number(bingo,num):
    flag=False
    for i in range(5):
        for j in range(5):
            if bingo[i][j]==num:
                bingo[i][j]="x"
                flag=True
                break
        if flag:
            break
    return bingo

def bingo_judge(bingo):
    for i in range(5):
        if (bingo[i][0]=="x" and bingo[i][1]=="x" and bingo[i][2]=="x" and bingo[i][3]=="x" and bingo[i][4]=="x"):
            bingo[0][0]=-1
            return bingo
    for j in range(5):
        if (bingo[0][j]=="x" and bingo[1][j]=="x" and bingo[2][j]=="x" and bingo[3][j]=="x" and bingo[4][j]=="x"):
            bingo[0][0]=-1
            return bingo
    if (bingo[0][0]=="x" and bingo[1][1]=="x" and bingo[2][2]=="x" and bingo[3][3]=="x" and bingo[4][4]=="x"):
        bingo[0][0]=-1
        return bingo
    if (bingo[0][4]=="x" and bingo[1][3]=="x" and bingo[2][2]=="x" and bingo[3][1]=="x" and bingo[4][0]=="x"):
        bingo[0][0]=-1
        return bingo
    return bingo

def main():
    population=45
    people=[]
    for _ in range(population):
        people.append(gen_bingo(bingo_init()))
    turn=1
    store=[]
    path="outputs/"+str(random.randint(1,2023))+".txt"
    with open(path,'a') as f:
        while True:
            while True:
                num=bingo_machine()
                if num not in store:
                    store.append(num)
                    break
            print("Turn: "+ str(turn) + " NUMBER: " + str(num),file=f)
            flag=0
            for i in range(population):
                if people[i][0][0]!=0:
                    people[i]=bingo_number(people[i],num)
                    people[i]=bingo_judge(people[i])
                    if people[i][0][0]==-1:
                        print("PLAYER-" + str(i) + " CLEAR!",file=f)
                        temp=people[i]
                        temp[0][0]="x"
                        for t in temp:
                            print(t,file=f)
                        people[i][0][0]=0
                if people[i][0][0]==0:
                    flag+=1
            print("CLEAR NUMBER: "+str(flag),file=f)
            print("CLEAR RATE: " + str((flag/population)*100) + "%",file=f)
            print("",file=f)
            if flag==population:
                exit()
            turn+=1

if __name__=="__main__":
    main()