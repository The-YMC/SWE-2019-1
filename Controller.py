import ymap
import random



class Contoller():
    
    def __init__(self, n_player, n_piece):
        self.map = ymap.Map(n_player, n_piece)
        self.n_roll = 0
        self.next_turn = 0
        
    def roll(self):
        yut = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        if sum(yut) == 1:
            if yut[0] == 1:
                self.n_roll = -1
            else:
                self.n_roll = 1
        elif sum(yut) == 2:
            self.n_roll = 2
        elif sum(yut) == 3:
            self.n_roll = 3
        elif sum(yut) == 4:
            self.n_roll = 4
        else:
            self.n_roll = 5
    
    def conditional_roll(self, num):
        self.n_roll = num
        
    def map_clicked(self, map_index):
        if self.n_roll != 0 :
            print(self.n_roll, map_index, self.next_turn)
            self.map_info, self.remained_piece, self.next_turn, self.in_goal, self.winner  = self.map.select(self.n_roll, map_index, self.next_turn)
            self.n_roll = 0  
            return self.map_info, self.remained_piece, self.next_turn, self.in_goal, self.winner