import copy

# =========================
# INPUT GOAL STATE
# =========================

print("Enter the 3x3 goal state row by row:")
goal = [list(map(int, input().split())) for _ in range(3)]

# Store goal positions for Manhattan Distance
goal_pos = {}

for i in range(3):
    for j in range(3):
        goal_pos[goal[i][j]] = (i, j)

# =========================
# HEURISTIC FUNCTION
# =========================

def h(s):
    d = 0

    for i in range(3):
        for j in range(3):

            val = s[i][j]

            if val != 0:
                x, y = goal_pos[val]
                d += abs(i - x) + abs(j - y)

    return d

# =========================
# FIND BLANK TILE
# =========================

def find0(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

# =========================
# DISPLAY BOARD
# =========================

def show(s):
    for r in s:
        print(" ".join(str(x) if x != 0 else "_" for x in r))

# =========================
# GENERATE NEXT STATES
# =========================

def next_states(s):

    r, c = find0(s)

    moves = [
        (r-1, c, 'DOWN'),
        (r+1, c, 'UP'),
        (r, c-1, 'RIGHT'),
        (r, c+1, 'LEFT')
    ]

    res = []

    for nr, nc, direction in moves:

        if 0 <= nr < 3 and 0 <= nc < 3:

            ns = copy.deepcopy(s)

            tile = ns[nr][nc]

            ns[r][c], ns[nr][nc] = ns[nr][nc], ns[r][c]

            res.append((ns, tile, direction))

    return res

# =========================
# FORMAT SEPARATOR
# =========================

def separator():
    print("\n" + "-" * 40 + "\n")

# =========================
# HILL CLIMBING
# =========================

def hill(s):

    print("=" * 40)
    print("   Hill Climbing — 8 Puzzle Solver")
    print("=" * 40)

    step = 0

    while True:

        separator()

        hval = h(s)

        if step == 0:
            print(f"  Step {step} | Initial State | h = {hval}\n")

        show(s)

        # Goal check
        if s == goal:

            separator()

            print(f"   GOAL REACHED in {step} steps!")

            print("\n" + "=" * 40)

            return

        neighbors = next_states(s)

        best = None
        best_h = hval
        best_tile = None
        best_dir = None

        # Find best neighbor
        for ns, tile, direction in neighbors:

            nh = h(ns)

            if nh < best_h:

                best = ns
                best_h = nh
                best_tile = tile
                best_dir = direction

        # Local minimum
        if best is None:

            separator()

            print(f"   LOCAL MINIMUM reached at step {step}.")

            print("\n" + "=" * 40)

            return

        step += 1

        s = best

        separator()

        print(f"  Step {step} | Move tile {best_tile} {best_dir} | h = {best_h}\n")

        show(s)

# =========================
# INPUT INITIAL STATE
# =========================

print("\nEnter puzzle (0 for blank):")

start = [list(map(int, input().split())) for _ in range(3)]

# =========================
# RUN
# =========================

hill(start)
