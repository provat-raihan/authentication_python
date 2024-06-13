def sum(num:list[int]):
    # num=[1,2,0,-1,-2]
    n=set()
    final=[]
    for index1,x in enumerate(num):
        for index2, y in enumerate(num):
            for index3,z in enumerate(num):
                # print(x)
                # print(y)
                # print(z)
                # print(x,y,z)
                if(index1!=index2):
                    if(index2!=index3):
                        if(index3!=index1):
                            q=x+y+z
                            if(q==0):
                                t=[x,y,z]
                                r=sorted(t)
                                u=tuple(r)
                                # print(u)
                                # print(t)
                                n.add(u)
                                # print(type(n))
                                # final.append(n)
    i=list(n)
    for l in i:
        g=list(l)
        final.append(g)
    print(final)
    # final=set(n)
    # print(final)

sum([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8])