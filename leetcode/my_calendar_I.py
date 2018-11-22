""" https://leetcode.com/problems/my-calendar-i/

2 solutions. First one is mine with a brute force. Second solution
is the leetcode solution where binary tree is used to sort the events

Solution 1:
Time complexity: O(n^2) and Space Complexity: O(n)

Loop through each event that is already scheduled and compare the start and end
times with the new event. If the new event doesnt clash at all with any of the
events already scheduled then we can append that event to the array of events
already scheduled


Solution 2:
Time Complexity: O(n^2) worst case and O(nlgn) on random data
Space Complexity: O(n)

We can improve on the previous algorithm a little bit by sorting the scheduled events
each time it is "appended". Instead of appending however we will create
a binary tree instead. We create a node that will represent an event. 
This node will have the start and end
properties but in addition that node will a left and a right property. The left
property will point to the next node that is less than the current node while 
the right node will point to the next node that is greater than the current node

The way we are inserting the nodes in the binary tree will not make the tree
balanced hence why worst case scenario it could take a linear number of steps
to add each event node thus the O(n^2)
"""

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for event in self.events:
            if (start >= event['start'] and start < event['end']) or (
                start < event['start'] and end > event['start']):
                return False
            
        self.events.append({
            'start': start,
            'end': end
        })
            
        return True
        


class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)