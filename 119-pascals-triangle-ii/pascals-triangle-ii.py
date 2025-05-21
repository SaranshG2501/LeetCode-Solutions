class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Initialize the first row of Pascal's Triangle
        row = [1]
        
        # Generate rows up to rowIndex
        for i in range(rowIndex):
            # Create the next row based on the current row
            new_row = [1]  # Start with 1
            for j in range(1, len(row)):
                # Each element is the sum of the two elements above it
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)  # End with 1
            row = new_row  # Move to the next row
        
        return row
