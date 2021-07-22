class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_ = []
        t = 0
        while len(pieces) > 0:
        # start with t = 0
            flag = False
            for i in range(len(pieces)):
                if arr[t] == pieces[i][0]:
                    arr_.append(pieces[i])
                    for j in range(1, len(pieces[i])):
                        if arr[t+j] != pieces[i][j]:
                            # elements of arr are not consistent with pieces.
                            return False

                    # index setting
                    t += len(pieces[i])
                    pieces.pop(i)
                    flag = True
                    break

            if not flag:
                return False

        return True