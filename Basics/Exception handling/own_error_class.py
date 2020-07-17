class error(Exception):
    def __init__(self, message='Correct Number'):
        self.message=message
        super().__init__(self.message)
number=int(input())
try:
    if number==6:
        raise error('Correct Number')
except Exception as e:
    print(e)     
else:
    print('Incorrect Number')      
