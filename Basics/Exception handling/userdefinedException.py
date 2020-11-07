class Truth(Exception):
    def __init__(self,msg):
        modified=msg+' jaani Katsura da'
        super().__init__(modified)
urhomiename=input('Enter your Homie Name: ')
if urhomiename.lower()!='Katsura'.lower():
    raise Truth(urhomiename)
