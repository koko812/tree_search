BOARD_LEN=3

board = [8,0,2,3,5,6,7,4,1]

def goal (board):
    if board == [0,1,2,3,4,5,6,7,8]:
        return True
    else:
        return False

def solvable(board):
    tento=0
    for i in range(len(board)-1):
        if board[i]==0: 
            continue
        for j in range(len(board)-i-1):
            if board[i+j+1]==0:
                continue
            #print(board[i], board[j+i+1])
            if board[i]>board[i+j+1]:
                #print("tento")
                tento+=1
    
    #if tento%2:
    #    return False
    #else:
    #    return True
    #print(f"tento={tento}")
    return tento%2 == 0
        

def next_state(board):
    pass

def show_board(board):
    str_board=[str(i) for i in board]
    for i in range(BOARD_LEN):
        print(' '.join(str_board[i*3:i*3+3]))
    

if __name__ == "__main__":
    print(solvable(board))
    print(goal(board))
    show_board(board)