'''
Created on 9/09/2022

@author: fabian
'''
theBoard = {'7': '', '8': '','9': '',
            '4': '','5': '','6': '',
            '1': '','2': '','3': ''}

boardKeys = []

print(boardKeys)

for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    
    print(board['7'] + '/' + board['8'] + '/' + board['9'] + '/' )
    print('-+-+-')
    
    print(board['4'] + '/' + board['5'] + '/' + board['6'] + '/' )
    print('-+-+-')
    
    print(board['1'] + '/' + board['2'] + '/' + board['3'] + '/' )
    print('-+-+-')

def game():
    turn = 'X'
    count = 0
    
    for  i in range(10):
        
        printBoard(theBoard)
        
        print("It is turn of " + turn + " Specify the place you want to go ")
        
        move = input()
        
        if theBoard[move]== '':
            theBoard[move] = turn
            count+=1
        else:
            print("Sorry this cell location is filled. Please Chosee an another one.")
            
            continue
        if count >= 5:
            
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
            
                break
        
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
        
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
        
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
            
            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
            
            if theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
            
            if theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over \n")
                print("Player " + turn + " won the game")
                
                break
        
        if count == 9:
            print("\nGame Over\n")
            print("The game is Tie!!")
        
        if turn == "X":
            turn="O"
        else:
            turn="X"
        restar = input("Do you want to restar the Game? (y/n)")
        
        if restar == 'y' or restar == 'Y':
            for key in boardKeys:
                theBoard[key]= ' '
            game()
        
        
        
        
if __name__ == "__main__":
    game()
        