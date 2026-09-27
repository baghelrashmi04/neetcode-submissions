class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dict_seen={} #value:index
            for i,n in enumerate(nums):
                
                a= target-n
                if a in dict_seen:
                    
                    return [dict_seen[a],i]
                dict_seen[n]=i
            return


