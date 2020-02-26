#!/usr/bin/python
def flames(name1,name2):
    m=[]
    n=[]
    '''
    above 2 list are used for appending the name1 and name2 into the list
    '''
    count=0 #count variable

    for i in name1:
        m.append(i)
    for j in name2:
        n.append(j)
    a=len(m) #length of list of name1
    b=len(n) #length of list of name2
    q=list(set(m)) #logic for repalcing multiple values into single values for ex 3 a's get replaced by single a
    w=list(set(n)) #logic for repalcing multiple values into single values for ex 3 a's get replaced by single a
    o=[] # empty list for appending common letters from name1 and name2
   
    for r in m:
        if r in n:
            o.append(r)
    for val in o:
        if val in q and w:
            q.remove(val)
            w.remove(val)
    'above 2 for loops append common letters into a new list and and remove them from their existing list'            
    count=len(q)+len(w) #length of the 2 lists of the name1 and name2 after removing the common letters
    luck=['F','L','A','M','E','S']
       
    for l in range(len(luck)):
        if count > len(luck):
            f=count%len(luck)
            if len(luck)>1:
                del(luck[f])
            else:
                print(luck)
        else:
            if len(luck)>1:
                del(luck[count-1])
            else:
                print(luck)

flames('nishkal','shradha')

	
	
	
