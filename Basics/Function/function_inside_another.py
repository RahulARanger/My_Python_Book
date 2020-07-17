def lets_do():
    def goto():
        a=int(input())
        if a!=6:
            print('The number is not 6')
            goto()
    goto()        
    print('Hmm Correct')
    return None
if __name__=='__main__':
    lets_do()
