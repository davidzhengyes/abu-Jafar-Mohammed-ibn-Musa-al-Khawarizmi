#https://leetcode.com/problems/valid-palindrome/submissions/
#good idea just went through the list too many times turning it into new lists.
#neetcode soln was as slow as mine. maybe list inefficient?
#checking top leetcode solns now.

import numbers


def isPalindrome(s):
    

    slist=list(s.lower())
    res=""
 
    for x in range(len(slist)):

        #damn turns 0 into '0'. how do detect if something is a letter?
        if  (isinstance(slist[x],str) and (("a"<=slist[x] and slist[x]<="z") or (48<=ord(slist[x]) and ord(slist[x])<=57))) or isinstance(slist[x],numbers.Number):
            res+=str(slist[x])
  
    reslist=list(res)

    for x in range(len(reslist)//2):
        if not reslist[x]==reslist[len(reslist)-x-1]:
            return False
    return True

    
    