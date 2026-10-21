# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result=[] #empty list to store all intermediate states 
        if not pairs:
            return result
        result.append(pairs.copy())
        for i in range(1,len(pairs)):
            temp=pairs[i]
            j=i-1
            while j>=0 and temp.key < pairs[j].key:
                pairs[j+1]=pairs[j]
                j-=1
            pairs[j+1]=temp
            result.append(pairs.copy())
        return result

        