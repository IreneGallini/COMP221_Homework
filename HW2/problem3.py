"""
Brute-force solver for the alphametic:
    ELEVEN + NINE + FIVE + FIVE = THIRTY

Idea: try every way of assigning distinct digits to the letters,
and check which assignment makes the equation true.
"""
from itertools import permutations

words = ["ELEVEN", "NINE", "FIVE", "FIVE"]   # the words being added
result = "THIRTY"                            # the sum word

# put all letters in a sorted set
letters = sorted(set("".join(words) + result))

# first letters can't be 0
leading = set(w[0] for w in words + [result])


def to_number(word, mapping):
    """Turn a word into a number using a letter -> digit mapping."""
    num = 0
    for ch in word:
        num = num * 10 + mapping[ch]
    return num


def solve():
    solutions = []
    # try every assignment of distinct digits to the letters.
    # permutations(range(10), k) gives every ordered choice of k distinct digits.
    for digits in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))

        # skip assignments with a leading zero.
        if any(mapping[ch] == 0 for ch in leading):
            continue

        # 5. Check whether the equation holds.
        total = sum(to_number(w, mapping) for w in words)
        if total == to_number(result, mapping):
            solutions.append(mapping)
    return solutions


if __name__ == "__main__":
    print(f"Letters ({len(letters)}): {letters}")
    sols = solve()
    print(f"Solutions found: {len(sols)}")
    for mapping in sols:
        print(" ".join(f"{ch}={mapping[ch]}" for ch in letters))
        nums = [to_number(w, mapping) for w in words]
        print(" + ".join(map(str, nums)), "=", to_number(result, mapping))