#!/usr/bin/env python3
import argparse
import heapq
from collections import deque

def parse_state(raw, size):
    tokens = raw.split()
    if len(tokens) != size * size:
        raise ValueError(f"need {size*size} numbers, got {len(tokens)}")
    tiles = tuple(int(t) for t in tokens)
    if set(tiles) != set(range(size * size)):
        raise ValueError("state must contain all numbers 0..n^2-1 exactly once")
    return tiles

def goal_state(size):
    return tuple(range(1, size * size)) + (0,)


def manhattan(state, size):
    distance = 0
    for idx, tile in enumerate(state):
        if tile == 0:
            continue
        goal_row, goal_col = divmod(tile, size)
        row, col = divmod(idx, size)
        distance += abs(goal_row - row) + abs(goal_col - col)
    return distance

def inversions(state):
    flat = [tile for tile in state if tile != 0]
    total = 0
    for i in range(len(flat)):
        total += sum(1 for j in range(i + 1, len(flat)) if flat[i] > flat[j])
    return total

def solvable(state, size):
    inv = inversions(state)
    if size % 2 == 1:
        return inv % 2 == 0
    blank_row = state.index(0) // size
    blank_from_bottom = size - blank_row
    if blank_from_bottom % 2 == 0:
        return inv % 2 == 1
    return inv % 2 == 0

MOVES = {
    (-1, 0): "up",
    (1, 0): "down",
    (0, -1): "left",
    (0, 1): "right",
}

def expand(state, size):
    idx = state.index(0)
    row, col = divmod(idx, size)
    for dr, dc in MOVES:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            nidx = nr * size + nc
            new_state = list(state)
            new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
            yield tuple(new_state), MOVES[(dr, dc)]

def a_star(start, size):
    goal = goal_state(size)
    h0 = manhattan(start, size)
    frontier = [(h0, 0, start, None, None)]
    heapq.heapify(frontier)
    seen = {start: 0}
    parents = {}

    while frontier:
        f, g, state, parent, move = heapq.heappop(frontier)
        if parent is not None:
            parents[state] = (parent, move)
        if state == goal:
            return reconstruct(state, parents)
        for next_state, move in expand(state, size):
            new_cost = g + 1
            if next_state not in seen or new_cost < seen[next_state]:
                seen[next_state] = new_cost
                heapq.heappush(
                    frontier,
                    (new_cost + manhattan(next_state, size), new_cost, next_state, state, move),
                )
    return None

def reconstruct(state, parents):
    path = deque()
    current = state
    while current in parents:
        parent, move = parents[current]
        path.appendleft((move, current))
        current = parent
    return list(path)

def print_board(state, size):
    width = len(str(size * size - 1))
    for row in range(size):
        line = []
        for col in range(size):
            tile = state[row * size + col]
            line.append(" " * width if tile == 0 else f"{tile:>{width}}")
        print(" ".join(line))
    print()

def main():
    parser = argparse.ArgumentParser(description="Solve sliding puzzle with A* search.")
    parser.add_argument("--size", type=int, default=3, help="board width/height (default: 3)")
    parser.add_argument(
        "--input",
        required=True,
        help="space-separated tile numbers, row-major, with 0 as blank",
    )
    parser.add_argument("--show-steps", action="store_true", help="print boards along solution path")
    args = parser.parse_args()

    start = parse_state(args.input, args.size)
    if not solvable(start, args.size):
        print("This configuration is not solvable.")
        return

    solution = a_star(start, args.size)
    if solution is None:
        print("No solution found.")
        return

    print(f"Solved in {len(solution)} moves.")
    if args.show_steps:
        current = start
        print("Start:")
        print_board(current, args.size)
        for step, (move, state) in enumerate(solution, 1):
            print(f"Move {step}: {move}")
            print_board(state, args.size)

if __name__ == "__main__":
    main()

