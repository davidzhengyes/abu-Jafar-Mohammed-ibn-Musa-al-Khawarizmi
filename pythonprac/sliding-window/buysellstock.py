#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#probably just two pointers on the same side L to R
#Maybe move the big one right until you find one bigger. When you find one bigger or end of list
#move the small one right until you find one smaller. have 4 variables, 2 for pointers and 2 to hold 
#current small and current big.
#exec(open("buysellstock.py").read())
#maxProfit([10,9,8,7,8,9,3])
##
##should have calculated current max profit so don't have to do all this sketchy increasing thing 
##to the right
##as an algorithm it works, but just a lot easier to code if you have the number maxprofit to compare.
##MY ALGORITHM WAS CORRECT.
##This also avoids having to have a currsell and currbuy.
##
# def maxProfit(prices):
#     n=len(prices)
#     if n==1:
#         return 0
    
#     else:

#         #well one while loop to find a price that is bigger than the previous.
#         #find any ONE value that is greater than the previous, otherwise return 0.

#         for x in range(n):
            
#             if x==n-1:
#                 return 0 #works for non-increasing list.
        
#             if prices[x+1]>prices[x]:
#                 buy=x
#                 sell=x+1
#                 break    #just finds first instance where prices[x]<prices[x+1]
#         # return (buy,sell)
#         currbuy=buy
#         currsell=sell

#         while True:
#             print(buy,sell)
#             while prices[sell+1]<=prices[currsell]:
#                 if sell==n-2:
#                     #meaning we are at the end and there was no more greater than the previous
#                     break

#                 sell+=1
            
#             if sell==n-2:
#                 pass
#             else:
#                 sell+=1
#                 #we have found a value that is greater
#                 currsell=sell

#             #do the same thing with the left side, going up to one left of the current sell index
#             while prices[buy+1]>=prices[currbuy]:
#                 if buy==sell-1:
#                     break
#                 buy+=1
#             if buy==sell-1:
#                 pass
#             else:
#                 #found a smaller buy value
#                 buy+=1
#                 currbuy=buy

#             if sell==(n-1) and buy==(n-2):
#                 break
            
        

#         return prices[currsell]-prices[currbuy]


#:(
def maxProfit(prices):
    l,r=0,1
    maxP=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxP=max(maxP,profit)
        else:
            # l+=1 knew this was suspicious
            l=r #works because we have already colleceted the in-between maxes.
        r+=1
    return maxP

            