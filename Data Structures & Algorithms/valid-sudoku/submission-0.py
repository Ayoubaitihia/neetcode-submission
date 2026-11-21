class Solution:
    
    def remove_points(self, lst: list):
        return [l for l in lst if l != '.']

    def isDuplicated(self, lst):
        return len(lst) != len(set(lst))

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        ColsHashMap = {}
        squaresHashMap = {}

        for i in range(len(board)):
            ColsHashMap[i] = []
            squaresHashMap[i] = []

        for i, b in enumerate(board):
            if self.isDuplicated(self.remove_points(b)):
                return False

        for i, lst in enumerate(board):
            for j, l in enumerate(lst):
                ColsHashMap[j].append(l)
                squaresHashMap[int(j/3)].append(l)

        for i in range(len(board)):
            if self.isDuplicated(self.remove_points(ColsHashMap[i])):
                return False

        for j in range(int(len(board)/3)):
            i = 0
            while i in range(len(board) * 3):
                start = i
                end = start + (len(board))
                if self.isDuplicated(self.remove_points(squaresHashMap[j][start:end])):
                    return False
                i += len(board)

        return True
        