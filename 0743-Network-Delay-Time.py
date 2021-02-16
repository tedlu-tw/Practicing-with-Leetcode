from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times or not N:
            return 0
        d = defaultdict(list)
        for k, v, w in times:
            d[k].append((w, v))

        h = [(0, K)]
        costSoFar = {K: 0}
        visited = set()
        while h:
            cost, node = heappop(h)
            visited.add(node)
            
            for edgeCost, nei in d[node]:
                if nei not in visited:
                    newCost = cost + edgeCost
                    if (nei not in costSoFar) or (nei in costSoFar and newCost < costSoFar[nei]):
                        heappush(h, (newCost, nei))
                        costSoFar[nei] = newCost
        if len(costSoFar) != N:
            return -1
        maxCost = 0        
        for k in costSoFar:
            maxCost = max(maxCost, costSoFar[k])
        return maxCost
