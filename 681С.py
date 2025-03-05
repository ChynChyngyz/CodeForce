import heapq

def main():
    n = int(input())
    operations = []
    heap = []
    result = []

    for _ in range(n):
        parts = input().split()
        if parts[0] == "insert":
            x = int(parts[1])
            heapq.heappush(heap, x)
            result.append(f"insert {x}")
        elif parts[0] == "getMin":
            x = int(parts[1])
            while heap and heap[0] < x:
                result.append("removeMin")
                heapq.heappop(heap)
            if not heap or heap[0] != x:
                heapq.heappush(heap, x)
                result.append(f"insert {x}")
            result.append(f"getMin {x}")
        elif parts[0] == "removeMin":
            if not heap:
                result.append("insert 0")
                heapq.heappush(heap, 0)
            result.append("removeMin")
            heapq.heappop(heap)

    print(len(result))
    for op in result:
        print(op)

if __name__ == "__main__":
    main()