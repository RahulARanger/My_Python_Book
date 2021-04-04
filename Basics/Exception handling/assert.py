try:
    n = int(input())
    assert n > 0, 'The given Number is less than 0'
except Exception as e:
    print(e)
else:
    print('The Given Number is Greater than 0')
finally:
    print('Good Bye!!!')
