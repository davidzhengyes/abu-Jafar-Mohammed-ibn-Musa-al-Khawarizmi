nums = [1,2,3,4]

def containsDup(nums):
    s = set()
    for x in range(len(nums)):
        if nums[x] in s:
            return True
        else:
            s.add(nums[x])

    return False