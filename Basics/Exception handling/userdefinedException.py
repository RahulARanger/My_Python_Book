class Truth(Exception):
    def __init__(self, msg):
        modified = msg + ' jaani Katsura da'
        super().__init__(modified)


name = input('Enter your Homie Name: ')
if name.lower() != 'Katsura'.lower():
    raise Truth(name)
