#given an int(stairs) how many different ways can u split(climb) them
#O(2^n)

def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1)+self.climbStairs(n-2)
