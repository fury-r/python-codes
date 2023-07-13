import random
from webapp import app
class Player:
    def __init__(self,data):
        self.id=data['name']
        self.position=[0,0,0,0]
        self.pieces=4

class Ludo:
    def __init__(self,data):
        self.color=['yellow','red','blue','green']
        random.shuffle(self.color)
        self.player=[[data[i],self.color[i]] for i in range (len(self.color))]
