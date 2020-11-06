def ini(str):
    if(len(str)==0):
        return
    name=str[0].upper()
    for i in range(1,len(str)-1):
        if(str[i]==' '):
            name+='.'.join(str[i+1].upper())

        
    print("The initials are "  + name)



    
wr=input("Enter your name :")
ini(wr)



