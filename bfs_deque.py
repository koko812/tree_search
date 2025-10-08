import collections
BOARD_LEN=3

initial_board = [8,0,2,5,6,3,7,4,1]

def goal (board):
    if board == (0,1,2,3,4,5,6,7,8):
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
    board = list(board)
    candidates = []
    for i,n in enumerate(board):
        if n == 0:
            zero_pos=i
    direction = [-3, -1, 1, 3]
    for d in direction:
        candidate = board.copy()
        if zero_pos//BOARD_LEN==0 and d==-3 or zero_pos//BOARD_LEN==2 and d==3:
            continue
        elif zero_pos%BOARD_LEN==0 and d==-1 or zero_pos%BOARD_LEN==2 and d==1:
            continue
        else:
            candidate[zero_pos]=board[zero_pos+d]
            candidate[zero_pos+d]=0
            candidates.append(tuple(candidate))

    return candidates


def show_board(board):
    str_board=[str(i) for i in board]
    for i in range(BOARD_LEN):
        print(' '.join(str_board[i*3:i*3+3]))

loop_cnt=0
ex_states = set()
ex_states.add(tuple(initial_board))
deque = collections.deque()
history = dict()

def bfs_deque(board, d):
    global loop_cnt
    print("-- initial state --")
    show_board(board)
    print("-------------------")
    loop = 0
    depth=0
    pre=-1
    deque.appendleft((board, depth, loop, pre))
    history[loop]= (board, depth, loop, pre) 

    flag = False
    while loop < d or not flag:
        state = deque.pop()
        history[state[2]]=state
        print(state)
        if goal(state[0]):
            flag=True
            print(state)
            loop_cnt=state[2]
            break
        for n_state in next_state(state[0]):
            if n_state not in ex_states:
                ex_states.add((n_state))
                deque.appendleft((n_state, state[1]+1, loop, state[2]))
                loop+=1
        


def show_graph():
    last_state = history[loop_cnt]
    print(len(history))
    loop = last_state[1]
    deq = collections.deque()
    for i in range(loop):
        print(f"last_state={last_state}")
        loop = last_state[1]
        deq.appendleft(last_state)
        last_state=history[last_state[3]]

    show_board(initial_board) 
    for d in deq:
        print()
        show_board(d[0])
    

if __name__ == "__main__":
    print(solvable((initial_board)))
    print(goal((initial_board)))
    print("== initial state ==")
    show_board(initial_board)
    print()
    for n in next_state((initial_board)):
        show_board(n)
        print()
    bfs_deque((initial_board), 800)
    show_graph()
