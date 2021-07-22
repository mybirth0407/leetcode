class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if num of rows is 1, then n * 1 array that eqaul to input string s.
        if numRows == 1:
            return s
        
        output = [[-1 for j in range(len(s))] for i in range(numRows)]
        s_re = list(reversed(s))
        # start point to write down direction.
        idx_rows = [row for row in range(0, len(s), numRows - 1)]
        for i in idx_rows:
            # write down direction.
            for j in range(numRows):
                if len(s_re) == 0:
                    break
                output[j][i] = s_re.pop()
            # write digonal direction.
            for j in range(1, numRows - 1):
                if len(s_re) == 0:
                    break
                output[numRows-1-j][i+j] = s_re.pop()
        s_ret = ''
        for l in output:
            for out in l:
                if out != -1:
                    s_ret += out
        return s_ret