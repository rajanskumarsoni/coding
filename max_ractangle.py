class Solution:
    def maxSumSubmatrix(self, w: List[List[int]], K: int) -> int:
        def get(x1: int, y1: int, x2: int, y2: int) -> int:
            return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
        
        n, m = len(w), len(w[0])
        """
        >>> a = [[1,2,3],[4,2,6]]
        >>> len(a) 行数
        2
        >>> len(a[0]) 列数
        3
        """
        # 预处理得到矩阵前缀和
        s = [[0 for i in range(m + 1)] for y in range(n + 1)]
        for i in range (1, n + 1):
            for j in range (1, m + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + w[i - 1][j - 1]
        
        res = -sys.maxsize
        for i in range(1, m + 1):
            for j in range(i, m + 1):
                L = [0]
                for k in range(1, n + 1):
                    si = get(1, i, k, j)
                    it = bisect.bisect_left(L, si - K)
                    if it != len(L):
                        res = max(res, si - L[it])
                    bisect.insort(L, si)
        return res
