#https://leetcode.com/problems/group-anagrams/
#my idea: have every "set" of anagrams in a dictionary, and store the index of the list in the value.
#so can quickly access the array element.

def group_anagrams(loa):
    anagramclasses={}
    result=[]
    resultlength=0
    for x in range(len(loa)):
        sortedstr="".join(str(x)for x in (sorted(loa[x])))
        if sortedstr in anagramclasses:
            result[anagramclasses[sortedstr]].append(loa[x])
        else:
            #maybe have a variable to hold length of result incrementing
            anagramclasses[sortedstr]=resultlength
            result.append([loa[x]])
            resultlength+=1
    return result








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

    return sdict==tdict
