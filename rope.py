import math
OPTIMAL_LENGTH = 10 # would normally be a large number like 1000
MIN_LENGTH = 5 # would normally be a large (but smaller than above) number like 500
MAX_LENGTH = 15 # would normally be a large (and bigger than above) number like 1500

class Rope:
    leftLength = 0
    value = ""
    isNotBalanced = False

    def __init__(self, string, isRoot=True):
        halfWay = int(math.ceil(len(string) / 2))
        self.isRoot = isRoot
        if halfWay > OPTIMAL_LENGTH:
            self.left = Rope(string[:halfWay], False)
            self.right = Rope(string[halfWay:], False)
            self.leftLength = halfWay
        else:
            self.value = string

    def __str__(self):
        if self.value != "":
            return self.value
        else:
            return self.left.__str__() + self.right.__str__()
    
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
            if not checkIfOptimalLength(length, MIN_LENGTH, MAX_LENGTH) and not self.isRoot:
                self.isNotBalanced = True
            return length
        else:
            if offset > self.leftLength:
                self.right.insert(offset - self.leftLength, string)
            else:
                length = self.left.insert(offset, string)
                self.leftLength = length
        if self.isRoot:
            self.rebalance()

        return self.leftLength

    def delete(self, offset, length):
        if self.value != "":
            value = self.value[:offset] + self.value[length + offset:]
            
            self.value = value
            length = len(value)
            if not checkIfOptimalLength(length, MIN_LENGTH, MAX_LENGTH) and not self.isRoot:
                self.isNotBalanced = True
            return length
        else:
            print offset, length, self.leftLength
            if offset > self.leftLength:
                self.right.delete(offset - self.leftLength, length)
            elif offset + length > self.leftLength:
                print "HERE", length, self.leftLength
                leftLength = self.left.delete(offset, self.leftLength - offset)
                self.right.delete(0, length - self.leftLength)
                self.leftLength = leftLength
            else:
                length = self.left.delete(offset, length)
                self.leftLength = length

        if self.isRoot:
            self.rebalance()

        return self.leftLength

    def amIBalanced(self):
        if self.value != "":
            return not self.isNotBalanced
        else:
            if self.left.amIBalanced() and self.right.amIBalanced():
                return True
            return False

    def rebalance(self):
        if not self.amIBalanced():
            string = self.__str__()
            halfWay = int(math.ceil(len(string) / 2))
            if halfWay > OPTIMAL_LENGTH:
                self.left = Rope(string[:halfWay], False)
                self.right = Rope(string[halfWay:], False)
                self.leftLength = halfWay
                self.value = ""
            else:
                self.value = string


def checkIfOptimalLength(length, minimum_length, maximum_length):
    if length > minimum_length and length < maximum_length:
        return True
    
    return False
