from typing import List
class Solution:
    def finMinDifference(self,timepoints:List[str])->int:
        for i,time in enumerate(timepoints):
            hr,min=time.split(':')
            min_past_midnight=int(hr)*60+int(min)
            timepoints[i]=min_past_midnight

        timepoints.sort()
        
        res=1440+timepoints[0]-timepoints[-1]

        for i in range(1, len(timepoints)):
            res=min(res,timepoints[i]-timepoints[i-1])
        
        return res
    
s=Solution()
print(s.finMinDifference(["23:59","00:00"]))
