def test(*args):
    print(type(args))  # ? tuple
    print('Argumens passed: ', args)


def test2(**kwargs):
    print(type(kwargs))  # ?
    print(kwargs)


test('First', 'Second', 'Third')
test2(ni='overflow', lollicon='you')
