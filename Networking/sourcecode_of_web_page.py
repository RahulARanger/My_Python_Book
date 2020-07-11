import urllib.request
website=input('Enter the link of the website: ')
filed=None
try:
  filed=urllib.request.urlopen(website)
  for i in filed:
      print(i.decode().strip())
except:
     print('Wrong link (gets excuted for anything including for the protected websites like https://crackdev.com/adobe-acrobat-pro-dc-final-full/#forward)')
