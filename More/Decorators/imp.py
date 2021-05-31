def check(fun):
    print('check This')
    def internal():
        fun()
    return internal
@check
def tryThis():
    print('tried')

tryThis() # output: tried
# run this without uncommenting anything: output: check This
