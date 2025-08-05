class Solution:
    def transpose(self, mat):
        # code here
        transposed_matrix = list(map(list, zip(*matrix)))
        return transposed_matrix
