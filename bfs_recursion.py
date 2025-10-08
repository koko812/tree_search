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
    zero_pos = 0
    candidates = []
    for i,n in enumerate(board):
        #print(f"board{n}")
        if n == 0:
            zero_pos=i
    direction = [-3, -1, 1, 3]
    for d in direction:
        candidate = board.copy()
        if zero_pos+d < 0 or BOARD_LEN**2-1 < zero_pos + d:
            continue
        else:
            #print(f"zero_pos={zero_pos}")
            #print(candidate[zero_pos],board[zero_pos+d])
            candidate[zero_pos]=board[zero_pos+d]
            candidate[zero_pos+d]=0
            candidates.append(candidate)

    return candidates


loop_cnt=0
ex_states = set()
ex_states.add(tuple(board))
def bfs(boards, d):
    global loop_cnt
    global ex_states
    if not isinstance(boards[0],list):
        boards=[boards]

    while loop_cnt<d:
        for state in boards:
            print(state)
            ex_states.add(tuple(state))
            if goal(state):
                print("goal")
                return state
            else:
                loop_cnt+=1
                for n_state in next_state(state):
                    if tuple(n_state) not in ex_states:
                        bfs(n_state, d)


def show_board(board):
    str_board=[str(i) for i in board]
    for i in range(BOARD_LEN):
        print(' '.join(str_board[i*3:i*3+3]))
    

if __name__ == "__main__":
    print(solvable(board))
    print(goal(board))
    print("== initial state ==")
    show_board(board)
    print()
    for n in next_state(board):
        show_board(n)
        print()
    bfs(board, 800)