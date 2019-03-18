puzzle = 'Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,InvincibleGhost,Melon,Galaxian,VulnerableGhost,VulnerableGhost,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Bell,Cherry,Strawberry,InvincibleGhost,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Dot,Orange,Apple,InvincibleGhost,VulnerableGhost,Key,InvincibleGhost,Dot,Dot,Dot,Dot,Dot,VulnerableGhost'
def points():
    packman = 5000
    packman_life = 3
    for i in puzzle.split(','):
        if i == 'Dot':
            packman += 10
        elif i == 'Cherry':
           packman += 100 
        elif i == 'Strawberry':
            packman += 300
        elif i == 'Orange':
            packman += 500 
        elif i =='Apple':
            packman += 700
        elif i =='Melon':
            packman += 1000
        elif i =='Galaxian':
            packman += 2000
        elif i =='Bell':
            packman += 3000
        elif i =='Key':
            packman += 5000
        elif i == 'InvincibleGhost':
            packman += 0
            packman_life -= 1   
            if packman == 10000:
                packman_life += 1 
        print(packman_life) 
        print(packman) 
    


points()

'''
vulneralble G

class Pacman:
    def __init__(self, points, lives):
        self.points = points
        self.lives = lives

    def __repr__(self):
        return f'{self.points} + {self.lives}'

if __name__ == "__main__":
    pass
'''