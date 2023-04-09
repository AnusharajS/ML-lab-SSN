n=int(input('Enter num of training data:'))
X=[]
print('Enter data row wise')
for i in range(2**n):         
    a =[]
    for j in range(n):      
         a.append(int(input()))
    X.append(a)
print(X)

alpha=int(input('Enter learning rate:'))
epoch=int(input('Enter num of epochs:'))
#t=int(input('Enter the threshold: '))
b=1
target=[]

#AND FUNCTION
def AND(X,alpha,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==1 and inp[1]==1:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    yin=[]
    wt_b=[0,0,0] #w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            yin=b*wt_b[2]+inp[0]*wt_b[0]+inp[1]*wt_b[1]
            #threshold is 0
            if yin>0:
                fyin=1
            elif yin==0:
                fyin=0
            else:
                fyin=-1

            if(target[i]!=fyin):
                wt_b[0]=wt_b[0]+(alpha*target[i]*inp[0])
                wt_b[1]=wt_b[1]+(alpha*target[i]*inp[1])
                wt_b[2]=wt_b[2]+(alpha*target[i])
        
            print(wt_b)
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")

#OR FUNCTION
def OR(X,alpha,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==1 or inp[1]==1:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    yin=[]
    wt_b=[0,0,0] #w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            yin=b*wt_b[2]+inp[0]*wt_b[0]+inp[1]*wt_b[1]
            if yin>0:
                fyin=1
            elif yin==0:
                fyin=0
            else:
                fyin=-1

            if(target[i]!=fyin):
                wt_b[0]=wt_b[0]+(alpha*target[i]*inp[0])
                wt_b[1]=wt_b[1]+(alpha*target[i]*inp[1])
                wt_b[2]=wt_b[2]+(alpha*target[i])
        
            print(wt_b)
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")

#XOR FUNCTION
def XOR(X,alpha,b,epoch):
    for i,inp in enumerate(X):
        if inp[0]==inp[1]:
            target.append(1)
        else:
            target.append(-1)
    print("Target:",target)
    yin=[]
    wt_b=[0,0,0] #w1 w2 b
    while(epoch>0):
        for i,inp in enumerate(X):
            yin=b*wt_b[2]+inp[0]*wt_b[0]+inp[1]*wt_b[1]
            if yin>0:
                fyin=1
            elif yin==0:
                fyin=0
            else:
                fyin=-1

            if(target[i]!=fyin):
                wt_b[0]=wt_b[0]+(alpha*target[i]*inp[0])
                wt_b[1]=wt_b[1]+(alpha*target[i]*inp[1])
                wt_b[2]=wt_b[2]+(alpha*target[i])
        
            print(wt_b)
        epoch=epoch-1
    target_fnl=[]
    for i,inp in enumerate(X):
        x1=inp[0]
        x2=inp[1]
        g=wt_b[2]+(x1*wt_b[0])+(x2*wt_b[1])
        if g>=0:
            target_fnl.append(1)
        else:
            target_fnl.append(-1)
    print("Target after training: \n",target_fnl)
    if target==target_fnl:
        print("Training successful!")
    else:
        print("Retrain:(")


AND(X,alpha,b,epoch)