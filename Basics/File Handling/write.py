fname=input('Enter the name of the file: ')
try:
    with open(fname,'w') as hand:
        print(hand.write("Now the File has the Contents in it"))
        print(hand.write('''
        Doc strings makes it easy to write paragraphs of the data ''')      )  
except:
    print('Tht file cannot be created')
#write() method returns the length of the content of the string that will be written inside the file