class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        to_ret=[]
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num]= 1

        sorted_k_items= sorted(seen.items(), key=lambda item :item[1], reverse=True)[:k]
            
        to_ret = [item[0] for item in sorted_k_items]

        return to_ret
