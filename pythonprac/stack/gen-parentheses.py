#https://leetcode.com/problems/generate-parentheses/
#stack?
#idk
#gonna watch neetcode for hint
#looks like tree
#try recursino as n at max 8.
#well done with little hint from neetcode
#was stuck at first assuming it was a stack
#just a classic little recursion question

def generateParenthesis(n):
    
    
    return genpar_rec("(",1,0,n)






def genpar_rec(currstr,open,closed,n):
    if open==n:
        return [currstr+(n-closed)*")"]
    else:
        if closed<open:
            res1=genpar_rec(currstr+"(",open+1,closed,n)
            res2=genpar_rec(currstr+")",open,closed+1,n)
            return res1+res2
        else:
            return genpar_rec(currstr+"(",open+1,closed,n)

