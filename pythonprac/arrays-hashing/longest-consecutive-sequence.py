#https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(nums):
    longest=0
    numSet=set(nums)

    for x in nums:
        if x-1 not in numSet:
            length=0
            while x+length in numSet:
                length+=1

            longest=max(length,longest)
    
    return longest

