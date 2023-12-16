#https://leetcode.com/problems/valid-anagram/
#ideas: we could access the opposite element making each of them a list
#wrong was thinking palindrome.
#use dictionary to count the number of occurrences?
#maybe slow?
#good solve.

def isAnagram(s,t):
    s=list(s)
    t=list(t)
    slen=len(s)
    tlen=len(t)
    if not (slen==tlen):
        return False
    
    sdict={}
    tdict={}
    for x in s:
        if x in sdict:
            sdict[x]+=1
        else:
            sdict[x]=1

    for x in t:
        if x in tdict:
            tdict[x]+=1
        else:
            tdict[x]=1

    print(sdict)

