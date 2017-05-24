from node import Node
# A Rope is a way of storing very large strings in a binary tree.
# The datastructure of a rope has it that the branches only store the length of the nodes on it's left hand side.

class Rope:
    def __init__(self, string, optimalLength=1000, minLength=500, maxLength=1500):

        # These are constants which are used to decide whether or not to re-build the tree
        self.OPTIMAL_LENGTH = optimalLength
        self.MIN_LENGTH = minLength
        self.MAX_LENGTH = maxLength

        self.node = Node(string, optimalLength, minLength, maxLength)
    
    def __str__(self):
        return str(self.node)
    
    def __len__(self):
        return len(self.node)
    
    def insert(self, offset, string):
        self.node.insert(offset, string)
        
        # Rebalance the tree. 
        if(not self.node.amIBalanced()):
            self.node = Node(str(self.node), self.OPTIMAL_LENGTH, self.MIN_LENGTH, self.MAX_LENGTH)
    
    def delete(self, offset, length):
        self.node.delete(offset, length)
        
        # Rebalance the tree. 
        if(not self.node.amIBalanced()):
            self.node = Node(str(self.node), self.OPTIMAL_LENGTH, self.MIN_LENGTH, self.MAX_LENGTH)


