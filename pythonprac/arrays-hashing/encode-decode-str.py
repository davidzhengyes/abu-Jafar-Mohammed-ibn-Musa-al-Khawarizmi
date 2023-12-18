#https://www.lintcode.com/problem/659/
#https://leetcode.com/problems/encode-and-decode-strings/
#leetcode premium hmph
#chinese website i cant get it to work account so soln untested
#https://www.youtube.com/watch?v=B1k_sxOSgv8 
#watching soln after.

def encode(strs):
    res=""
    for x in range(len(strs)):
        res+=str(len(strs[x]))
        res+="#"
        res+=strs[x]
    return res

