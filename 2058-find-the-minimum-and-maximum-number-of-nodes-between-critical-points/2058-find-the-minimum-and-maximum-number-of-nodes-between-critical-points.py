class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        if not curr:
            return [-1, -1]
        
        next_node = curr.next
        idx = 1
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        
        while next_node:
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                if first_cp == -1:
                    first_cp = idx
                    last_cp = idx
                else:
                    min_dist = min(min_dist, idx - last_cp)
                    last_cp = idx
            prev = curr
            curr = next_node
            next_node = next_node.next
            idx += 1
            
        if first_cp == -1 or first_cp == last_cp:
            return [-1, -1]
        
        max_dist = last_cp - first_cp
        return [min_dist, max_dist]