from itertools import permutations  

class Solution:
    def countArrangement(self, n: int) -> int:
        perms = permutations(list(range(1, n + 1)))
        count = 0

        for perm in perms:
            flag = True
            for i in range(len(perm)):
                if not self.check(i + 1, perm[i]):
                    flag = False
                    break
            if flag == True:
                count += 1
        return count
    
    def check(self, index, number):
        if index % number == 0 or number % index == 0:
            return True
        else:
            return False