#https://leetcode.com/problems/evaluate-reverse-polish-notation/
#just stacker it
#ok this soln betas 8% kinda slow.

# def evalRPN(tokens):
#     import math
#     stack=[]
#     for x in tokens:
#         if x=="*" or x=="+" or x=="/" or x=="-":
#             print(stack)
#             b=stack.pop()
#             a=stack.pop()
#             print(a,b)
#             if x=="/":
#                 if int(a)*int(b)>0:
#                     stack.append(str (math.floor(int(a)/ int(b))))
#                 else:
#                     stack.append(str (math.ceil(int(a)/ int(b))))
#             else:
#                 stack.append(str(eval(a+x+b)))
#         else:
#             stack.append(x)

#     return int(stack[0])


########
#trying something else
###
#deque no faster. lets see how neetcode doesit
def evalRPN(tokens):
    from collections import deque
    import math
    stack=deque()
    for x in tokens:
        if x=="*" or x=="+" or x=="/" or x=="-":

            b=stack.pop()
            a=stack.pop()

            if x=="/":
                if int(a)*int(b)>0:
                    stack.append(str (math.floor(int(a)/ int(b))))
                else:
                    stack.append(str (math.ceil(int(a)/ int(b))))
            else:
                stack.append(str(eval(a+x+b)))
        else:
            stack.append(x)

    return int(stack[0])
        

