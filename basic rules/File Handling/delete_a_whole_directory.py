import os
def delete_files(name):
    for i in name:
        os.remove(i)
def delete_dirs(name):
    dirs,files=[],[]
    lst=os.listdir()
    print(lst)
    for i in lst:
        if os.path.isdir(i):
            dirs.append(i)
        else:
            files.append(i)
    delete_files(files)
    restore=os.getcwd()
    for i in dirs:
        new_name=os.path.join(restore,i)
        os.chdir(new_name)
        delete_dirs(os.getcwd())
        os.chdir(restore)
        os.rmdir(i)               
dir=input('Enter the name of the Directory: ')
add=input('Enter the address of the Directory: ')
# creating the new name in such a way to go inside the given directory
new_name=os.path.join(add,dir)
#going with chdir()
os.chdir(new_name)
print(os.getcwd())
delete_dirs(new_name)
os.chdir(add)
print(os.getcwd())
os.rmdir(dir)
os.system('pause')