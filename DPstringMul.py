@author: gaoyu
"""

#dynamic programming
count=0
k="k3(aa2(2(a)))"
def dp(astring):
    
    length=len(astring)
    count=0
    count2=0
    right=0
    left=length
    
    
    for i in range(0,length):
        if astring[i]=="(":
            if count==0:
                left=i
            count+=1
            count2+=1
            
        else:
            if astring[i]==")":
                count-=1
                count2+=1
                if count==0:
                    right=i
    if count2==0:
        return astring
    subleft=left+1
    subright=right
    sub=astring[subleft:subright]        
    asubstring=dp(sub)
    
    toadd=asubstring
    multiply=int(astring[left-1])
    for i in range(1,multiply):
        asubstring+=toadd
    
    astring=astring[0:left+1]+asubstring+astring[right:length]
    return astring
    
print(dp(k)) 
