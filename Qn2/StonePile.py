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

def main():
    initialState = list(map(int, input('Enter initial state of stone piles: ').split()))

    game = Game(initialState)
    print('Current state: [%d, %d]'%(game.state[0], game.state[1]))

    while(sum(game.state) > 0):

        action = list(map(int, input("Player 1's turn: ").split()))
        game.state[action[0]] -= action[1]
        print('Current state: [%d, %d]'%(game.state[0], game.state[1]))

        if sum(game.state) == 0:
            print("You won!")
            break

        action = minimax(game, 2)
        game.state[action[0]] -= action[1]
        print("Player 2 removed %d from %s pile" % (action[1], \
            '1st' if action[0] == 0 else '2nd'))
        print('Current state: [%d, %d]'%(game.state[0], game.state[1]))
        if sum(game.state) == 0:
            print("You Lost:(")

if __name__ == "__main__":
    main()