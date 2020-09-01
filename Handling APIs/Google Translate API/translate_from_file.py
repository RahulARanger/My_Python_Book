import googletrans
path=input('Enter the File Path: ')
hand=open(path,'r')
translator=googletrans.Translator()
resulto,resultd,resultp=str(),str(),str()
for i in hand:
    line=i
    result=translator.translate(i,src='en',dest='ja')
    resulto=resulto+result.origin
    resultd=resultd+'\n'+result.text
    resultp=resultp+'\n'+result.pronunciation
print('From: ')
print(resulto)
print('To:')
print(resultd)
print('Pronunciation:')
print(resultp)