class Solution:
    def threeSum(self, nums: list[int]):
        n=set()
        final=[]
        for index1,x in enumerate(nums):
            for index2, y in enumerate(nums):
                for index3,z in enumerate(nums):
                    if((index1!=index2!=index3)):
                        q=x+y+z
                        if(q==0):
                            t=[x,y,z]
                            r=sorted(t)
                            u=tuple(r)
                            n.add(u)
        i=list(n)
        for l in i:
            g=list(l)
            final.append(g)
        return final
print(Solution.threeSum(self,[-1,0,1,2,-1,-4]))