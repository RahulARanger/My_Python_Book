import re
def align(text):
    result=re.search(r'([^,]+),(.+)$',text)
    # modified with the unittest
    if result is None:return '' 
    return result[2]+' '+result[1]
if __name__=='__main__':
    print(align(input('Enter the name: ')))