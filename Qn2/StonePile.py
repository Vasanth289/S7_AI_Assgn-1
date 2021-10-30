class Game:

    def __init__(self, initialState):
        self.state = initialState

    def actions(self, state):
        res = []

        for pile in range(2):
            for stone in range(1, state[pile]+1):
                res.append([pile, stone])
        # print('possible actions')
        # print(res)
        return res

def minimax(game, player):

    def newState(state, action):
        state_ = state.copy()
        state_[action[0]] -= action[1]
        return state_
    
    def recurse(state, player):
        # print(state, player)

        if sum(state) == 0:
            if player == 2:
                return (1, None)
            else:
                return (-1, None)
        
        choices = []
        possibleActions = game.actions(state)
        for action in possibleActions:
            # print('state-action')
            # print(state, action)
            nxtState = newState(state, action)
            # print(nxtState)
            nxtPlayer = 1 if player == 2 else 2
            choices.append((recurse(nxtState, nxtPlayer)[0], action))
        
        # print('choices')
        # print(choices)
        if player == 1:
            res = max(choices)
        else:
            res = min(choices)
        
        return res
    
    value, action = recurse(game.state, player)
    return action

def main(conf, startPlayer):
    initialState = list(map(int, input('\nEnter initial state of stone piles: ').split()))

    game = Game(initialState)
    if conf == 'y' or conf == 'Y':
        print('\nHuman vs Bot')
    else:
        print('\nBot vs Bot')
    print('\nCurrent state: [%d, %d]'%(game.state[0], game.state[1]))

    while(sum(game.state) > 0):

        if (conf == 'y' or conf == 'Y') and startPlayer == 1:
            action = list(map(int, input("Player 1's turn (pile, stones): ").split()))
        else:
            action = minimax(game, startPlayer)
            print("Player %d removed %d from %s pile" % (startPlayer, action[1], \
                '1st' if action[0] == 0 else '2nd'))

        game.state[action[0]] -= action[1]
        print('\nCurrent state: [%d, %d]'%(game.state[0], game.state[1]))

        if sum(game.state) == 0:
            if (conf == 'y' or conf == 'Y') and startPlayer == 1:
                print("You won!")
            else:
                print("Player %d won!" % startPlayer)
            break
        
        nxtPlayer = 1 if startPlayer == 2 else 2
        if (conf == 'y' or conf == 'Y') and startPlayer == 2:
            action = list(map(int, input("Player 1's turn (pile, stones): ").split()))
        else:
            action = minimax(game, nxtPlayer)
            print("Player %d removed %d from %s pile" % (nxtPlayer, action[1], \
            '1st' if action[0] == 0 else '2nd'))

        game.state[action[0]] -= action[1]
        print('\nCurrent state: [%d, %d]'%(game.state[0], game.state[1]))
        if sum(game.state) == 0:
            if (conf == 'y' or conf == 'Y') and startPlayer == 2:
                print("You won!")
            else:
                print("Player %d won!" % nxtPlayer)

if __name__ == "__main__":
    print('Stone Pile Game\n')
    print('Game instructions are given README.pdf\n')
    print(30*'=')
   
    conf = input('\nDo you want to play?(y/n)')
    if conf == 'y' or conf == 'Y':
        conf_ = input('\nWould you like to go first?(y/n)')
        if conf_ == 'y' or conf_ == 'Y':
            startPlayer = 1
        else:
            startPlayer = 2
    else:
        startPlayer = int(input('\nWho should start first? Player 1 or Player 2: '))
    main(conf, startPlayer)