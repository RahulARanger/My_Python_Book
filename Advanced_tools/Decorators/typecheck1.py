def typecheck(func):
    def check(element):
        if type(element) not in [int,float]:
            raise TypeError('Not a Number')
        return func(element)
    return check
@typecheck
def onhere(element):
    print('{} is a number'.format(element))

onhere(6)
onhere('23')
