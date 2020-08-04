# try to prove that it is possible to pay any amount>=8 with 3 and 5 coins
# note we can't exchange any coins from the borrower
# we even have unlimited 3 and 5 coins
def do_it(amount):
    _5,_3=0,0
    coins=[0,0]
    if amount%3==0:_3=amount//3
    elif amount%5==0:_5=amount//5
    elif amount%8==0:
        _3=amount//8
        _5=amount//8
    else:
        check=do_it(amount-3)
        coins[0]+=check[0]
        coins[1]+=check[1]
        _3+=1
    coins[0]+=_3
    coins[1]+=_5
    return coins
amount=int(input('Enter the amount to pay: '))
if amount<8 and amount!=3 and amount!=5: 
    print('Not Possible')
else:
    if amount==3 or amount==5:        coins=[1,0] if amount==3 else [0,1]
    else:coins=(do_it(amount))
    print('Pay {} (x5) coins and {} (x3) coins '.format(coins[1],coins[0]))