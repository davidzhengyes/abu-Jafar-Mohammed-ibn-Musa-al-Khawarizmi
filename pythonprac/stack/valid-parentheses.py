#https://leetcode.com/problems/valid-parentheses/
#learn stack


from collections import deque

def isValid(s):
    mystack=deque()

    #fill and pop the 
    for x in s:
        if x=="{" or x=="(" or x=="[":
            mystack.append(x)
        else:
            if not mystack or not equivalent(x)==mystack.pop():
                return False
    if mystack:
        return False
    else: 
        return True

def equivalent(parenthesis):
    if parenthesis==")":
        return "("
    elif parenthesis=="}":
        return "{"
    else:
        return "["