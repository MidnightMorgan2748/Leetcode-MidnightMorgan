class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def b(date):
            return sum(a[:int(date[:2]) - 1]) + int(date[3:])
        c = max(b(arriveAlice), b(arriveBob))
        d = min(b(leaveAlice), b(leaveBob))

        return max(0, d-c+1)