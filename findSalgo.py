
inst=int(input('Enter the number of training examples:'))
ftr=int(input('Enter the number of features:'))
fl=[]
for i in range(ftr):
    f=input('Enter the features:')
    fl.append(f)
print(fl)

L=[]
target=[]
for i in range(inst):
    l=[]
    for j in range(ftr):
        x=input('Enter {} of example {}: '.format(fl[j],i+1))
        l.append(x)
        
    L.append(l)
    t=input('Enter target of example {}:'.format(i+1))
    target.append(t)
print('Training example: \n',L)
print('Target:\n ',target)

h=[]
for k in range(ftr):
    h.append('N')
print('Initial hypothesis: \n',h)

for i,inp in enumerate(L):
    if(target[i]=='Y' or target[i]=='y'):
        for j in range(len(inp)):
            if(h[j]=='N'):
                h[j]=inp[j]
            elif(h[j]==inp[j]):
                continue
            else:
                h[j]='?'
    else:
        continue
print('The hypothesis for the given training example is: \n',h)




#i1=['small','circular','dark','smooth','thick']
# i2=['small','elliptical','light','smooth','thin']
# i3=['small','circular','light','rough','thick']
# i4=['small','elliptical','light','rough','thick']
# i5=['small','elliptical','dark','smooth','thin']
# i6=['big','circular','dark','smooth','thick']
# i7=['small','circular','light','smooth','thick']
# i8=['big','elliptical','light','rough','thin']
