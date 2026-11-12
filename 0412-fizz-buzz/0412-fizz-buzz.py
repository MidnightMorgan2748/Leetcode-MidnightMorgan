class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        a = []
        for i in range(n):
            a.append(str(i+1))

        for i in range(n):
            if (i+1) % 3 == 0:
                a[i] = "Fizz"
            if (i+1) % 5 == 0:
                a[i] = "Buzz"
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                a[i] = "FizzBuzz"

        return a