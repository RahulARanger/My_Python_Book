# !  n1 and n2 are needed, mising them will raise an error
def test(n1, n2, *extras):
    print('Main Arguments', n1)
    print('extras:', extras)


test('glasses', 'pink glasses', 'shinpachi')
try:
    test('shinpachi')
except:
    print('you missed main argument (Hint: glasses)')
