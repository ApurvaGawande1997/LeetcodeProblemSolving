class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict={}
        for i in range(0,len(nums)):
            complement=target-nums[i]
            if complement in map_dict:
                return [map_dict[complement],i]
            map_dict[nums[i]]=i
        return []