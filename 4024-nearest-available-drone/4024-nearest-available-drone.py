class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        a, b = target
        c = float('inf')
        d = -1
        for i, (dx, dy, drange) in enumerate(drones):
            distance = abs(dx - a) + abs(dy - b)
            if distance <= drange:
                if distance < c:
                    c = distance
                    d = i
        return d