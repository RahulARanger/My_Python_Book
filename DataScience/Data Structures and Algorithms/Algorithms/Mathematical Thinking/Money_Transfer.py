# in a country where only 13 and 7 type of coin is used find the rate of the transfer of the money 
# from the sender to receiver for each query
while True:
    transfer=int(input('Enter the amount of the money that one needs to give: '))
    check=transfer//13
    transfer-=check*13
    _13s=check
    check=transfer//7
    transfer-=check*7
    _7s=check
    check=transfer//6
    transfer-=check*6
    _13s+=check
    _7s+=check
    if transfer>0:
            _7s+=transfer*2
            _13s-=transfer
    if _7s>0:print('Give {} seven amount of coin{}'.format(_7s,'s' if _7s>1 else ''))
    if _13s!=0: print('{} {} thirteen amount of coin{}'.format('Give' if _13s>0 else 'Take',_13s if _13s>0 else -_13s,'s' if _13s!=1 else ''))
    if input('Wanna Continue (y/n): ')=='y':continue
    else:break    