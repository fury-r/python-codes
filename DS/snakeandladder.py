import random
class Player:
    def __init__(self,id):
        self.start=0
        self.player_id=id
    def increase(self):self.start=self.start+1
    def decrease(self,data):self.start=data

class Board(Player):
    def __init__(self,n):
        self.count=0
        self.players=n
        self.snakes=[[11,9],[15,2],[23,9][28,1]]
        self.ladders=[[2,9],[16,26]]
        self.l=[ Player(n) for i in range (1,n)]
        self.max=50
    def roll(self,data,n):
        self.l[n].increase(data)
        if self.l[n].start in self.snakes:
            self.l[n].decrease(self.snakes[self.snakes.index(self.l[n].start)][1])
        elif self.l[n].start in self.ladder:
                self.l[n].increase(self.ladder[self.ladder.index(self.l[n].start)][1])
    def start(self):
        while True:
            for i in self.l:
                a=input(f'Roll player {i.id} \n Press Enter')
                a=random.randint(1,6)
                print(f'Rolled {a}')
                self.roll(a,i.id-1)
                if i.start==self.max:
                    self.l.pop(self.l.index(i))
            for i in self.l:
                print(f"Player {i.id} is at Position {i.start}")
                