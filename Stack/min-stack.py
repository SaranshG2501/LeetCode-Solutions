class MinStack(object):

    def __init__(self):
        # Initialize two stacks: one for the main stack and one for the minimum values
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the current value is less than or equal to the current minimum,
        # push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # Pop the top value from the main stack
        if self.stack:
            top_value = self.stack.pop()
            # If the popped value is the same as the current minimum, pop it from the min_stack as well
            if top_value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Return the top value of the main stack
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # Return the top value of the min_stack, which is the minimum value in the main stack
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
