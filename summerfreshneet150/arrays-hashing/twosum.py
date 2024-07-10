    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for x in range(len(nums)):
            diff = target - nums[x]

            if diff in s:
                return[x, s[diff]]
            else:
                s[nums[x]] = x