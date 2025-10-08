import collections
import pickle
BOARD_LEN=4

def show_board(board):
    str_board=[str(i).rjust(2) for i in board]
    for i in range(BOARD_LEN):
        print(' '.join(str_board[i*BOARD_LEN:i*BOARD_LEN+BOARD_LEN]))



def show_graph(history):
    last_state = history[max(history.keys())]
    print(len(history))
    loop = last_state[2]
    deq = collections.deque()
    for i in range(loop):
        print(f"last_state={last_state}")
        loop = last_state[2]
        deq.appendleft(last_state)
        last_state=history[last_state[4]]

    for d in deq:
        print()
        show_board(d[1])
    

if __name__ == "__main__":
    with open("history.pkl", "rb") as f:
        history = pickle.load(f)

    print(max(history.keys()))
    show_graph(history)
    