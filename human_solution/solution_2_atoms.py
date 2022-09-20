import heapq
def solve(s,k):
    res = []
    start_index = -1
    end_index = len(s) - k
    h = [(y, x) for x, y in enumerate(s[:end_index])]
    heapq.heapify(h)

    for _ in range(k):
        heapq.heappush(h, (s[end_index], end_index))
        end_index += 1
        while True:
            val, ind = heapq.heappop(h)
            if ind > start_index: break
        res.append(val)
        start_index = ind
    return ''.join(res)
    
def astring():
    T = int(input())
    for t in range(T):
        s = input()
        k = int(input())
        print(solve(s,k))

if __name__ == "__main__":
  astring()