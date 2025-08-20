class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        # Base case
        if n == 1:
            return 1
        # Recursive case: total moves = left + 1 + right
        moves = self.towerOfHanoi(n - 1, fromm, aux, to)
        moves += 1
        moves += self.towerOfHanoi(n - 1, aux, to, fromm)
        return moves
