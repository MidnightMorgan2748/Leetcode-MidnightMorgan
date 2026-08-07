import collections

FACTOR_COUNTS = {
    0: collections.Counter(),
    1: collections.Counter(),
    2: collections.Counter([2]),
    3: collections.Counter([3]),
    4: collections.Counter([2, 2]),
    5: collections.Counter([5]),
    6: collections.Counter([2, 3]),
    7: collections.Counter([7]),
    8: collections.Counter([2, 2, 2]),
    9: collections.Counter([3, 3]),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, isDivisible = self._getPrimeCount(t)
        if not isDivisible:
            return '-1'

        factorCount = self._getFactorCount(primeCount)
        if sum(factorCount.values()) > len(num):
            return ''.join(str(f) * c for f, c in factorCount.items())

        primeCountPrefix = sum((FACTOR_COUNTS[int(c)] for c in num),
                                start=collections.Counter())
        firstZeroIndex = next((i for i, d in enumerate(num) if d == '0'), len(num))

        if firstZeroIndex == len(num) and primeCount <= primeCountPrefix:
            return num  

        for i, c in reversed(list(enumerate(num))):
            d = int(c)
            primeCountPrefix -= FACTOR_COUNTS[d]
            spaceAfterThisDigit = len(num) - 1 - i

            if i <= firstZeroIndex:
                for biggerDigit in range(d + 1, 10):
                    needed = primeCount - primeCountPrefix - FACTOR_COUNTS[biggerDigit]
                    factorsAfterReplacement = self._getFactorCount(needed)
                    if sum(factorsAfterReplacement.values()) <= spaceAfterThisDigit:
                        fillOnes = spaceAfterThisDigit - sum(factorsAfterReplacement.values())
                        return (num[:i] + str(biggerDigit) + '1' * fillOnes +
                                ''.join(str(f) * c for f, c in factorsAfterReplacement.items()))

        factorCount = self._getFactorCount(primeCount)
        return ('1' * (len(num) + 1 - sum(factorCount.values())) +
                ''.join(str(f) * c for f, c in factorCount.items()))

    def _getPrimeCount(self, t: int):
        count = collections.Counter()
        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                count[p] += 1
        return count, t == 1

    def _getFactorCount(self, count):
        count8, rem2 = divmod(count[2], 3)
        count9, count3 = divmod(count[3], 2)
        count4, count2 = divmod(rem2, 2)
        if count2 == 1 and count3 == 1:
            count2, count3, count6 = 0, 0, 1
        else:
            count6 = 0
        if count3 == 1 and count4 == 1:
            count2, count6, count3, count4 = 1, 1, 0, 0
        return {2: count2, 3: count3, 4: count4, 5: count[5],
                6: count6, 7: count[7], 8: count8, 9: count9}