class Solution:
    def minimumDistance(self, word: str) -> int:
        pre_costs = {('BEGIN','BEGIN'): 0}
        for i, x in enumerate(word):
            cur_costs = dict()
            for pre_key, pre_cost in pre_costs.items():
                # Pick each set
                x0 = pre_key[0]
                x1 = pre_key[1]
                
                key0 = tuple(sorted([x1, x]))
                if key0 not in cur_costs:
                    cur_costs[key0] = pre_cost + self.dist(x0, x)
                else:
                    cur_costs[key0] = min(cur_costs[key0], pre_cost + self.dist(x0, x))
                    
                key1 = tuple(sorted([x0, x]))
                if key1 not in cur_costs:
                    cur_costs[key1] = pre_cost + self.dist(x1, x)
                else:
                    cur_costs[key1] = min(cur_costs[key1], pre_cost + self.dist(x1, x))
            pre_costs = cur_costs
        
        res = float('inf')
        for key, total in pre_costs.items():
            res = min(res, total)
        return res
        
        
    def dist(self, x1, x2):
        if x1 == 'BEGIN' or x2 == 'BEGIN':
            return 0
        y1 = ord(x1) - ord('A')
        y2 = ord(x2) - ord('A')
        row1, col1 = y1//6, y1 - 6*(y1//6)
        row2, col2 = y2//6, y2 - 6*(y2//6)
        return abs(row1-row2) + abs(col1 - col2)
