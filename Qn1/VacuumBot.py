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

    def left(self):
        self.currentPos = 0

    def right(self):
        self.currentPos = 1

    def runSimulation(self):
        print(super().__str__())

        moves = 0
        while(moves < 1000):
            if self.locationCondtion[self.currentPos] == 1:
                self.suck()
            else:
                self.score += 1
                if self.currentPos == 0:
                    self.right()
                elif self.currentPos == 1:
                    self.left()
            
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
    print('\nVacuum Bot\n')
    print('Details are mentioned in README.pdf\n')
    print(30*'=')
    print()

    main()