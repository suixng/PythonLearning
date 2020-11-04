print("input n")
#n=input()
def Test(n,i,j):
    i=int(i)
    j=int(j)
    m=""
    for i in range(1,int(n)+1):
        for j in range(1,int(n)+1):
            if(int(n)==i*j):
                m=str(i)+"X"+str(j)+"X"+m
                if(j<int(n)):
                    Test(str(j),i+1,1)
                print(n+"=="+m)
            
Test(input(),1,1)




        

