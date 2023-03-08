class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        counter = 0
        while True:
            counter += 1
            k -= 1
            temp = queue.popleft() - 1
            if temp != 0:
                queue.append(temp)
            if k == -1:
                k = len(queue) - 1
                if temp == 0:
                    break
                
        return counter