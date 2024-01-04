#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#slide the L and slide the R and reset into an empty set()

def lengthOfLongestSubstring(s):
    s=list(s)

    l,r=0,1
    longest=0

    unique={}
    if len(s)>=1:
        unique[s[l]]=l
    while r<len(s):
  
        if s[r] in unique:
            longest=max(longest,len(unique))
            l=unique[s[r]]+1 #l should not go to r. should go to the index of the repeated char+1.
            r=l+1
            unique={}
            unique[s[l]]=l

            print(l,r,unique)
        else:
            unique[s[r]]=r
            r+=1

        print(unique)
    longest=max(longest,len(unique))
        



    return longest