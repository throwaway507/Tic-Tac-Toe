import random

players = ['O', 'X']
startingPlayer = random.choice(players)
currentPlayerIndex = players.index(startingPlayer)

win = False
draw = False

board = {
    "t-l": ' ', "t-m": ' ', "t-r": ' ',
    "m-l": ' ', "m-m": ' ', "m-r": ' ',
    "b-l": ' ', "b-m": ' ', "b-r": ' ',
}


def gameWon():
    global win
    win = True
    return True


def gameDrawn():
    global draw
    draw = True
    return True


def boardIsFilled(board):
    if ' ' not in board.values():
        return True

    return False


def printBoard(board):
    print(board["t-l"] + "|" + board["t-m"] + "|" + board['t-r'])
    print(board["m-l"] + "|" + board["m-m"] + "|" + board['m-r'])
    print(board["b-l"] + "|" + board["b-m"] + "|" + board['b-r'])


def isOver(board):
    """Pionowe wygrane: """
    if board['t-l'] == board['m-l'] == board['b-l'] and \
            board['t-l'] != ' ' and board['m-l'] != ' ' and board['b-l'] != ' ':
        return gameWon()
    if board['t-m'] == board['m-m'] == board['b-m'] and \
            board['t-m'] != ' ' and board['m-m'] != ' ' and board['b-m'] != ' ':
        return gameWon()

    if board['t-r'] == board['m-r'] == board['b-r'] and \
            board['t-r'] != ' ' and board['m-r'] != ' ' and board['b-r'] != ' ':
        return gameWon()

    """Poziome wygrane: """
    if board['t-l'] == board['t-m'] == board['t-r'] and \
            board['t-l'] != ' ' and board['t-m'] != ' ' and board['t-r'] != ' ':
        return gameWon()
    if board['m-l'] == board['m-m'] == board['m-r'] and \
            board['m-l'] != ' ' and board['m-m'] != ' ' and board['m-r'] != ' ':
        return gameWon()
    if board['b-l'] == board['b-m'] == board['b-r'] and \
            board['b-l'] != ' ' and board['b-m'] != ' ' and board['b-r'] != ' ':
        return gameWon()

    """Ukośne wygrane: """
    if board['b-l'] == board['m-m'] == board['t-r'] and \
        board['b-l'] != ' ' and board['m-m'] != ' ' and board['t-r'] != ' ':
        return gameWon()
    if board['t-l'] == board['m-m'] == board['b-r'] and \
        board['t-l'] != ' ' and board['m-m'] != ' ' and board['b-r'] != ' ':
        return gameWon()

    """Remis: """
    if boardIsFilled(board):
        return gameDrawn()


def fillBoxes(box, position, board, players):
    if box.lower().startswith('b'):
        if position.lower().startswith('l'):
            board['b-l'] = players[currentPlayerIndex]
        elif position.lower().startswith('m'):
            board['b-m'] = players[currentPlayerIndex]
        elif position.lower().startswith('r'):
            board['b-r'] = players[currentPlayerIndex]
    elif box.lower().startswith('m'):
        if position.lower().startswith('l'):
            board['m-l'] = players[currentPlayerIndex]
        elif position.lower().startswith('m'):
            board['m-m'] = players[currentPlayerIndex]
        elif position.lower().startswith('r'):
            board['m-r'] = players[currentPlayerIndex]
    elif box.lower().startswith('t'):
        if position.lower().startswith('l'):
            board['t-l'] = players[currentPlayerIndex]
        elif position.lower().startswith('m'):
            board['t-m'] = players[currentPlayerIndex]
        elif position.lower().startswith('r'):
            board['t-r'] = players[currentPlayerIndex]


print("WELCOME TO THE TIC-TAC-TOE GAME\n")
print(players[currentPlayerIndex] + " has the first move!")

while not isOver(board):
    print("It's " + players[currentPlayerIndex % len(players)] + "'s player turn\n")
    printBoard(board)
    print()

    while True:
        box = input("Choose the box: top, mid or bot: ")[0].lower()
        position = input("Choose the position: (l)eft, (m)id or (r)ight: ")[0].lower()
        if box + '-' + position not in board.keys():
            print("Unknown box. Try again.\n")
        elif board[box + '-' + position] == ' ':
            break
        else:
            print("This box is already occupied. Try choosing other box.\n")

    fillBoxes(box, position, board, players)
    print()

    # Next turn.
    currentPlayerIndex += 1
    if currentPlayerIndex == len(players):
        currentPlayerIndex = 0

# Show board at the end of the game.
printBoard(board)
# If either of players won.
if win:
    print(players[currentPlayerIndex-1] + " has won the game.")
else:
    print("The game is drawn.")
