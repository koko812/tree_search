# solver.py
from dataclasses import dataclass
from collections import deque
import heapq

@dataclass(frozen=True)
class PuzzleState:
    board: tuple[int, ...]
    blank: int
    depth: int = 0
    parent: "PuzzleState | None" = None
    move: str | None = None

class SlidingPuzzle:
    MOVES = {(-1, 0): "up", (1, 0): "down", (0, -1): "left", (0, 1): "right"}

    def __init__(self, size: int, board: tuple[int, ...]):
        self.size = size
        self.start = PuzzleState(board, board.index(0))

    @staticmethod
    def goal(size: int) -> tuple[int, ...]:
        return tuple(range(1, size * size)) + (0,)

    # solvable(...) / neighbors(...) / reconstruct_path(...) をここへ集約
    @staticmethod
    def inversions(state):
        flat = [tile for tile in state if tile != 0]
        total = 0
        for i in range(len(flat)):
            total += sum(1 for j in range(i + 1, len(flat)) if flat[i] > flat[j])
        return total

    @staticmethod
    def solvable(state, size):
        inv = SlidingPuzzle.inversions(state)
        if size % 2 == 1:
            return inv % 2 == 0
        blank_row = state.index(0) // size
        blank_from_bottom = size - blank_row
        if blank_from_bottom % 2 == 0:
            return inv % 2 == 1
        return inv % 2 == 0

class Solver:
    def solve(self, puzzle: SlidingPuzzle):
        raise NotImplementedError

class BFSSolber(Solver):
    pass


class AStarSolver(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, puzzle: SlidingPuzzle):
        start = puzzle.start
        goal = SlidingPuzzle.goal(puzzle.size)
        frontier = [(self.heuristic(start.board, puzzle.size), 0, start)]
        best_g = {start.board: 0}
        while frontier:
            f, g, curr = heapq.heappop(frontier)
            if curr.board == goal:
                return puzzle.reconstruct_path(curr)
            if g > best_g[curr.board]:
                continue
            for nxt in puzzle.neighbors(curr):
                new_g = g + 1
                if new_g < best_g.get(nxt.board, float("inf")):
                    best_g[nxt.board] = new_g
                    heapq.heappush(frontier, (new_g + self.heuristic(nxt.board, puzzle.size), new_g, nxt))
        return None

