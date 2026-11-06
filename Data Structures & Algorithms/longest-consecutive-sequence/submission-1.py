class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sequence = set(nums)
        longest_count=1
        current_count =1
        for num in nums:
            if (num-1) in sequence:
                continue
            else:
                while (num+1) in sequence:
                    num+=1
                    current_count+=1
                if current_count>longest_count:
                    longest_count=current_count
                current_count=1
        return longest_count