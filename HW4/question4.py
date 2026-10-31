import sys
import heapq
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    out = []

    while idx < len(data):
        n = int(data[idx]); idx += 1

        stack = []
        queue = deque()
        pq = []  # max-heap via negated values
        is_stack = is_queue = is_pq = True

        for _ in range(n):
            cmd = int(data[idx]); x = int(data[idx + 1]); idx += 2

            if cmd == 1:
                stack.append(x)
                queue.append(x)
                heapq.heappush(pq, -x)
            else:
                # Taking from an empty bag: none of the three can explain it
                if not stack:
                    is_stack = is_queue = is_pq = False
                    continue
                if stack.pop() != x:
                    is_stack = False
                if queue.popleft() != x:
                    is_queue = False
                if -heapq.heappop(pq) != x:
                    is_pq = False

        count = is_stack + is_queue + is_pq
        if count == 0:
            out.append("impossible")
        elif count > 1:
            out.append("not sure")
        elif is_stack:
            out.append("stack")
        elif is_queue:
            out.append("queue")
        else:
            out.append("priority queue")

    sys.stdout.write("\n".join(out) + "\n")


main()