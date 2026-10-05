"""
Question 4: timing add and delete operations on Python lists
at the front, back, and middle.

For each cell (operation, size n):
  repeat REPEATS times:
    - for deletes, first fill the list with n items (not timed)
    - start the timer
    - do the operation n times (adds grow 0 -> n, deletes shrink n -> 0)
    - stop the timer
  report the average time.

Cells that would take longer than TIME_LIMIT seconds are marked "too big".
"""
import time

# ---- settings: edit SIZES to match the table ----
SIZES = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
REPEATS = 10
TIME_LIMIT = 180  # seconds per cell (the assignment says 2-3 minutes)


# ---- the six operations ----
# Each takes a list and n, and performs the operation n times.

def add_front(lst, n):
    for i in range(n):
        lst.insert(0, i)

def add_back(lst, n):
    for i in range(n):
        lst.append(i)

def add_middle(lst, n):
    for i in range(n):
        lst.insert(len(lst) // 2, i)

def delete_front(lst, n):
    for _ in range(n):
        lst.pop(0)

def delete_back(lst, n):
    for _ in range(n):
        lst.pop()

def delete_middle(lst, n):
    for _ in range(n):
        lst.pop(len(lst) // 2)


# Same row order as the table in the assignment.
OPERATIONS = [
    ("add to front", add_front, False),
    ("add to middle", add_middle, False),
    ("add to end", add_back, False),
    ("del from front", delete_front, True),
    ("del from middle", delete_middle, True),
    ("del from end", delete_back, True),
]


def time_cell(op, n, is_delete):
    """Run one cell REPEATS times and return the average time in seconds."""
    total = 0.0
    for _ in range(REPEATS):
        # Setup (not timed): deletes start with a full list, adds start empty.
        lst = list(range(n)) if is_delete else []

        start = time.perf_counter()   # high-resolution timer
        op(lst, n)
        end = time.perf_counter()

        total += end - start
    return total / REPEATS


def format_time(seconds):
    if seconds < 1e-3:
        return f"{seconds * 1e6:.1f} us"
    if seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    return f"{seconds:.2f} s"


def main():
    # results[name][n] = average seconds, or None for "too big"
    results = {name: {} for name, _, _ in OPERATIONS}

    for name, op, is_delete in OPERATIONS:
        history = []      # (n, avg) for sizes already measured in this row
        too_big = False
        for n in SIZES:
            # Predict the next cell from how fast this row has been growing.
            # Each size is 10x the last; growth ratio ~10 means linear, ~100 quadratic.
            # (Assume at least linear, since we always do n operations.)
            if not too_big and len(history) >= 2:
                (n1, a1), (n2, a2) = history[-2], history[-1]
                ratio = max(a2 / a1 if a1 > 0 else 10, n / n2)
                predicted_cell = a2 * ratio * REPEATS
                if predicted_cell > TIME_LIMIT:
                    too_big = True
            if too_big:
                results[name][n] = None
                print(f"{name:<16} n={n:<12,} too big")
                continue

            try:
                avg = time_cell(op, n, is_delete)
            except MemoryError:
                too_big = True
                results[name][n] = None
                print(f"{name:<16} n={n:<12,} too big (out of memory)")
                continue

            results[name][n] = avg
            history.append((n, avg))
            print(f"{name:<16} n={n:<12,} avg = {format_time(avg)}", flush=True)

    # Print the finished table in the same layout as the assignment
    # (rows = operations, columns = sizes).
    labels = ["1", "10", "100", "1k", "10k", "100k", "1M", "10M", "100M"]
    col_labels = labels[:len(SIZES)] if len(SIZES) == len(labels) else [f"{n:,}" for n in SIZES]
    print("\n" + "n".ljust(17) + "".join(lb.ljust(11) for lb in col_labels))
    for name, _, _ in OPERATIONS:
        row = name.ljust(17)
        for n in SIZES:
            val = results[name][n]
            row += ("too big" if val is None else format_time(val)).ljust(11)
        print(row)


if __name__ == "__main__":
    main()