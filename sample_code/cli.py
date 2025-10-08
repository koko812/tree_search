# cli.py
import argparse
from solver import SlidingPuzzle, BFSSolver, AStarSolver, manhattan

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=3)
    parser.add_argument("--input", required=True)
    parser.add_argument("--algo", choices=["bfs", "astar"], default="bfs")
    parser.add_argument("--show-steps", action="store_true")
    args = parser.parse_args()

    board = tuple(int(x) for x in args.input.split())
    puzzle = SlidingPuzzle(args.size, board)
    solver = BFSSolver() if args.algo == "bfs" else AStarSolver(manhattan)
    path = solver.solve(puzzle)
    ...

if __name__ == "__main__":
    main()

