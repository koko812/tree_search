import collections
import heapq
BOARD_LEN=4

#initial_board = [8,0,2,5,6,3,7,4,1]
#initial_board = [1,0,2,3,4,5,6,7,8,9,10,12,13,11,14,15]
initial_board = [14,13,12,15,4,2,3,0,5,9,6,7,1,8,10,11]
goal_board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def goal (board):
    if board == (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
        return True
    else:
        return False

def manhattan(board):
    total = 0
    for i, c in enumerate(board):
        if c==0:
            continue
        total += abs(i%BOARD_LEN-c%BOARD_LEN) + abs(i//BOARD_LEN-c//BOARD_LEN)

    return total


def solvable(board):
    tento=0
    for i in range(len(board)-1):
        if board[i]==0: 
            continue
        for j in range(len(board)-i-1):
            if board[i+j+1]==0:
                continue
            if board[i]>board[i+j+1]:
                tento+=1
    
    return tento%2 == 0
        

def next_state(board):
    zero_pos = 0
    print(f"board={board}")
    board = list(board)
    candidates = []
    for i,n in enumerate(board):
        if n == 0:
            zero_pos=i
    direction = [-BOARD_LEN, -1, 1, BOARD_LEN]
    for d in direction:
        candidate = board.copy()
        if zero_pos//BOARD_LEN==0 and d==-BOARD_LEN or zero_pos//BOARD_LEN==BOARD_LEN-1 and d==BOARD_LEN:
            continue
        elif zero_pos%BOARD_LEN==0 and d==-1 or zero_pos%BOARD_LEN==BOARD_LEN-1 and d==1:
            continue
        else:
            candidate[zero_pos]=board[zero_pos+d]
            candidate[zero_pos+d]=0
            candidates.append(tuple(candidate))

    return candidates


def show_board(board):
    str_board=[str(i).rjust(2) for i in board]
    for i in range(BOARD_LEN):
        print(' '.join(str_board[i*BOARD_LEN:i*BOARD_LEN+BOARD_LEN]))

loop_cnt=0
ex_states = set()
ex_states.add(tuple(initial_board))
queue = []
history = dict()


def a_star(board, d):
    global loop_cnt
    print("-- initial state --")
    show_board(board)
    print("-------------------")
    loop = 0
    depth=0
    pre=-1
    distance = manhattan(board)
    heapq.heappush(queue, (distance, board, depth, loop, pre))
    history[loop]= (distance, board, depth, loop, pre) 

    flag = False
    while loop < d or not flag:
        state = heapq.heappop(queue)
        history[state[3]]=state
        print(state)
        if goal(state[1]):
            flag=True
            print(state)
            loop_cnt=state[3]
            break
        for n_state in next_state(state[1]):
            if n_state not in ex_states:
                ex_states.add((n_state))
                distance = manhattan(n_state)
                heapq.heappush(state[2]+queue, (distance, n_state, state[2]+1, loop, state[3]))
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
    print(initial_board)
    show_board(initial_board)
    a_star(initial_board, 800)
    #show_graph()
    