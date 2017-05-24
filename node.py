import math

class Node:
    leftLength = 0
    value = ""
    isBalanced = True
    
    def __init__(self, string, optimalLength=1000, minLength=500, maxLength=1500, isRoot=True):
        halfWay = int(math.ceil(len(string) / 2))

        self.isRoot = isRoot

        # These are constants which are used to decide whether or not to re-build the tree
        self.OPTIMAL_LENGTH = optimalLength
        self.MIN_LENGTH = minLength
        self.MAX_LENGTH = maxLength

        # We build the rope by splitting the string in two until we get to the desired length
        if halfWay > self.OPTIMAL_LENGTH:
            self.left = Node(string[:halfWay], self.OPTIMAL_LENGTH, self.MIN_LENGTH, self.MAX_LENGTH, False)
            self.right = Node(string[halfWay:], self.OPTIMAL_LENGTH, self.MIN_LENGTH, self.MAX_LENGTH,  False)
            self.leftLength = halfWay
        else:
            self.value = string

    def __str__(self):
        if self.value != "":
            return self.value
        else:
            return str(self.left) + str(self.right)
    
    def __len__(self):
        if self.value != "":
            return len(self.value)
        else:
            return self.leftLength + len(self.right)

    def insert(self, offset, string):
        if self.value != "":
            value = self.value[:offset] + string + self.value[offset:]
            self.value = value
            length = len(value)
            if not checkIfOptimalLength(length, self.MIN_LENGTH, self.MAX_LENGTH) and not self.isRoot:
                self.isBalanced = False
            return length
        else:
            if offset > self.leftLength:
                self.right.insert(offset - self.leftLength, string)
            else:
                length = self.left.insert(offset, string)
                self.leftLength = length


        return self.leftLength

    def delete(self, offset, length):
        if self.value != "":
            value = self.value[:offset] + self.value[length + offset:]
            self.value = value
            length = len(value)
            if not checkIfOptimalLength(length, self.MIN_LENGTH, self.MAX_LENGTH) and not self.isRoot:
                self.isBalanced = False
            return length
        else:
            if offset > self.leftLength:
                self.right.delete(offset - self.leftLength, length)
            elif offset + length > self.leftLength:
                leftLength = self.left.delete(offset, self.leftLength - offset)
                self.right.delete(0, length - (self.leftLength - offset))
                self.leftLength = leftLength
            else:
                leftLength = self.left.delete(offset, length)
                self.leftLength = leftLength


        return self.leftLength

    def amIBalanced(self):
        if self.value != "":
            return self.isBalanced
        else:
            if self.left.amIBalanced() and self.right.amIBalanced():
                return True
            return False

# Checks to see if the length provided is within the desired range
def checkIfOptimalLength(length, minimum_length, maximum_length):
    if length > minimum_length and length < maximum_length:
        return True
    return False
