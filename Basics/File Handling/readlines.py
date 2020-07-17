fname=input('Enter the name of the File: ')
try:
  with open(fname) as hand:
      lines=hand.readlines()
      hand.close()
      print(lines)
except:
    print('File doesn\'t exist')
print(len(lines))