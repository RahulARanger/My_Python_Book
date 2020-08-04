# This is the General solution for payment of the amount using x and y coins
# ofc we can't pay amount<x+y except x and y 
# we can't borrow money 
import sys
def do_it(amount,coin1,coin2):
    coins=[0,0]
    _coin1,_coin2=0,0
    if amount%coin1==0:_coin1+=amount//coin1
    elif amount%coin2==0:_coin2+=amount//coin2
    elif amount%(coin1+coin2)==0:
        _coin1+=amount//(coin1+coin2)
        _coin2+=amount//(coin1+coin2)
    else:
        check=do_it(amount-coin1,coin1,coin2)    
        _coin1+=1
        coins[0]+=check[0]
        coins[1]+=check[1]
    coins[0]+=_coin1
    coins[1]+=_coin2    
    return coins    
amount=int(input('Enter the amount to pay: '))
coin1=int(input('Enter the value for the first coin: '))
coin2=int(input('Enter the value for the second coin: '))
if amount!=coin1 and amount!=coin2 and amount<(coin1+coin2):
    print('Not Possible')
else:
    if coin1>coin2:coin1,coin2=coin2,coin1
    if amount==coin1 or amount==coin2:
        coins=[1,0] if amount==coin1 else [0,1]
    else:
        coins=do_it(amount,coin1,coin2)
        if coins[0]<0 or coins[1]<0:
            print('Not possible')
            sys.exit(0)
    print('Pay {} (x{}) and {} (x{}) coins'.format(coins[0],coin1,coins[1],coin2))