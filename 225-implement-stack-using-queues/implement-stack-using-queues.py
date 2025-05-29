from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()  # Main queue to hold stack elements
        self.queue2 = deque()  # Auxiliary queue for operations

    def push(self, x):
        """
        Pushes element x to the top of the stack.
        """
        # Add the new element to the auxiliary queue
        self.queue2.append(x)
        
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the names of the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        Removes the element on the top of the stack and returns it.
        """
        return self.queue1.popleft()  # The front of queue1 is the top of the stack

    def top(self):
        """
        Returns the element on the top of the stack.
        """
        return self.queue1[0]  # The front of queue1 is the top of the stack

    def empty(self):
        """
        Returns true if the stack is empty, false otherwise.
        """
        return not self.queue1  # Check if queue1 is empty

# Example usage:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())   # Returns 2
# print(obj.pop())   # Returns 2
# print(obj.empty()) # Returns False
