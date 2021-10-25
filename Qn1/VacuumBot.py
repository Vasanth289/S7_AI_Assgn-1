import random

class Environment:

    def __init__(self, environment):
        self.locationCondtion = environment

    def __str__(self):
        status = ['Clean', 'Dirty']
        return 'Environment: [A:%s, B:%s]'%(status[self.locationCondtion[0]], status[self.locationCondtion[1]])

class VacuumBot(Environment):

    def __init__(self, startPos, environment):
        super().__init__(environment) 
        self.currentPos = startPos
        self.startPos = startPos
        self.score = 0

    def suck(self):
        self.locationCondtion[self.currentPos] = 0

    def move(self):
        newPos = random.randint(0, 1)

        if self.currentPos == newPos:
            pass
        
        if self.locationCondtion[newPos] == 0:
            self.score += 1
        
        self.currentPos = newPos

    def runSimulation(self):
        print(super().__str__())

        moves = 0
        while(moves < 1000):
            if self.locationCondtion[self.currentPos] == 1:
                self.suck()
            else:
                self.move()
            
            moves += 1
    
    def __str__(self):
        return 'Start Position: %s\n'%('A' if self.startPos == 0 else 'B') + \
            'Performance Score: %d\n'%(self.score)

def main():
    for startPos in range(2):
        for A in range(2):
            for B in range(2):
                bot = VacuumBot(startPos, [A, B])
                bot.runSimulation()
                print(bot)

if __name__ == '__main__':
    main()