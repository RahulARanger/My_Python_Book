class test:
    fav_num=69
    
    def __init__(self):
        self.more_fav_num=66
    @classmethod
    def say(cls):
        more_fav_num=66
        print(more_fav_num)
        print(cls.fav_num)
    
d=test()
d.say()
