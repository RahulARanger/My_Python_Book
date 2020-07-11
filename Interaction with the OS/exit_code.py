import os
import sys
try:
    file_name=sys.argv[1]
except:
    print('File name is not given ')
    sys.exit(1)
if not os.path.exists(file_name):
 with open(file_name,'w') as f:
    f.write('New File has been Created')
    print('The New File has been created')
else:
    print('The File Already Exists')
    sys.exit(1)
