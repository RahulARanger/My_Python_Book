import re
line=input('Enter a Line of Text: ').strip()
print('The Number of Words in the Line is {} '.format(len(re.findall(r'\s+',line))+1))
