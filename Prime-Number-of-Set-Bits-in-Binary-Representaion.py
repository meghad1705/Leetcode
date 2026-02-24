class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        # Function to check prime
        def isPrime(n):
            if n < 2:
                return False

            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        count = 0

        for num in range(left, right + 1):

            # count set bits
            setBits = bin(num).count('1')

            # check prime
            if isPrime(setBits):
                count += 1

        return count
