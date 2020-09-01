import googletrans
text=input('Enter the text: ')
to=input('Enter the code for the to language: ')
translator=googletrans.Translator()
# TODO: googletrans.Translator().translate() is a method which accepts src as a from language and dest as the destination language
result=translator.translate(text,src='en',dest=to)
# ? result is a object here and it has important variables
print('Source Language:',result.src)
print('Destination Language:',result.dest)
print(result.origin,'->',result.text)
print('English Pronunciation:',result.pronunciation)
lst=[i for i in result.text]
print(lst)