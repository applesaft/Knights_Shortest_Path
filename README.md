# Knight's Shortest Path

A Python program that finds the **shortest sequence of moves** for a knight to travel from a starting square to a target square on a standard 8×8 chessboard.

## What It Does

You give the program a start position and a target position (each as `x, y` coordinates between `0` and `7`). It then searches the board for the fewest number of legal knight moves needed to get from one to the other, and reports:

- the **number of moves** in the shortest path
- the **full path** of squares the knight passes through
- the **number of nodes visited** during the search (a measure of how much work the search did)

A knight moves in an "L" shape, so from any square `(x, y)` it can reach up to eight positions:

```
next_moves = [
        (x - 1, y - 2),
        (x - 2, y - 1),
        (x + 1, y - 2),
        (x - 1, y + 2),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x + 1, y + 2),
        (x + 2, y + 1),
    ]
```

### How the search works

The program uses a **recursive depth-first search (DFS) with backtracking**. From the current square it generates all legal next moves, recurses into each one, and undoes the move (`current_path.pop()`) before trying the next branch.

To avoid exploring the whole tree, it applies **branch-and-bound pruning**: it keeps track of the shortest complete path found so far, and abandons any branch whose move count has already reached or exceeded that best result. As better solutions are found, the bound tightens and more of the search space gets cut off.

The search also avoids revisiting squares already on the current path, and it ignores any move that would land off the board.

## The Manhattan Distance Heuristic

The order in which moves are explored matters a lot for performance. If the search stumbles onto a short path early, the branch-and-bound pruning becomes far more aggressive, so the program tries to explore *promising* moves first.

To decide which moves look promising, it uses the **Manhattan distance** between a candidate square and the target:

```
manhattan((x1, y1), (x2, y2)) = |x1 - x2| + |y1 - y2|
```

This is simply the sum of the horizontal and vertical distance to the target. Before recursing, the list of legal next moves is **sorted by Manhattan distance**, so squares that are geometrically closer to the target are tried first.

A couple of things worth noting:

- The heuristic is only used to **order** the moves, not to decide correctness. Optimality is still guaranteed by the exhaustive DFS together with the pruning bound — the heuristic just helps the program *find* a good path sooner.
- Manhattan distance is a rough guide for a knight (which doesn't move in straight steps), but it works well in practice as a cheap, simple way to bias the search toward the goal and cut down the number of nodes visited.

## Running the Program

```bash
python knight.py
```

The program prompts for four integers: the start coordinates and the target coordinates. All four must be in the range `0`–`7`; if any are out of range it will ask again.

## Example

Finding the shortest path from the bottom-left corner `(0, 0)` to the top-right corner `(7, 7)`:

```
Starting Position
x_start: 0
y_start: 0
Target Position
x_target: 7
y_target: 7
number of moves: 6, number of nodes visited during search: 7514, position: (7, 7)
(0, 0) -> (1, 2) -> (2, 4) -> (3, 6) -> (5, 7) -> (6, 5) -> (7, 7)
From position (0, 0) to (7, 7), 6 moves is needed
```

So the knight reaches the opposite corner in **6 moves**, and the program shows the exact squares it passes through.

A shorter trip, from `(0, 0)` to `(3, 3)`:

```
number of moves: 2, number of nodes visited during search: 13, position: (3, 3)
(0, 0) -> (1, 2) -> (3, 3)
From position (0, 0) to (3, 3), 2 moves is needed
```

## Files

- `knight.py` — the complete program (input handling, recursive search, heuristic, and output).
