def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1: return [[1]]
        master = generate(numRows-1)
        prev = master[-1]
        row = [1]
        for i in range(len(prev)-1):
                row.append(prev[i] + prev[i+1])
        row.append(1)
        master.append(row)
        return master

print(generate(5))