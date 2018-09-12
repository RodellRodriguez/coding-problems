""" https://leetcode.com/problems/lru-cache/description/

There are 3 main requirements for an LRU cache:
	1. Has to be a fixed size set by the user
	2. Needs O(1) access and insert for any item
	3. Needs a cache eviction policy/algorithm when the cache is full
	whereby the least recently used item is deleted upon inserting a new item

An additional feature is that if an item is already in the cache and is requested
by the user, then that item must be updated to the most recently used


The main solution to this problem is to use a combination of 2 well known data
data structures i.e. hash table (dict) and a doubly linked list.

If we were only concerned with the 2'nd requirement then a hash table would've sufficed
but because of the 3'rd requirement, we need a doubly linked list to track
the most/least recently used via head/tail respectively. Additionally we cant just use
a doubly linked list on its own because we then sacrifice O(1) access when we search
for the node. Therefore the hash table will make up for that so long as we hash the key
of a node as the same key as the hash table (and minus any 
considerations towards hashing collisions).

Finally, the 1'st requirement is fulfilled simply by setting a capacity variable
in the LRU cache to track to set the ceiling for the number of nodes that the LRU cache
may hold. One drawback to this capacity approach is that we are assuming that each
node will take up the same number of bytes in memory i.e. the memory distribution
throughout all the nodes are uniform. Because really preventing out of memory error (oom) 
is the goal here. So, if this assumption of uniform memory distribution is not true 
then we would need to think of a different way to control capacity or use an algorithm
that guarantees uniformity.

Note that solution treats the TAIL.prev as the most recently used node and the HEAD.next
is the least recently used node. Tail and Head are both dummy nodes that never get
deleted. They're used as markers to simplify knowing where the head and tail are at
and preventing annoying edge cases namely off by 1 errors
"""


# Has prev and next attributes to support doubly linked list capabilities
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None


class LRUCache():
    def __init__(self, capacity):

        self.capacity = capacity
        self.hash_table = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        if key in self.hash_table:
            node = self.hash_table[key]
            # Removal and adding guarantees the order of the node is 
            # changed to most recent in the linked list
            self._remove(node)
            self._add(node)
            # Gotcha. Be sure to return the actual value not the node bject
            return node.value
        return -1

    def put(self, key, value):
        if key in self.hash_table: self._remove(self.hash_table[key])
        node = Node(key, value)
        self._add(node)
        self.hash_table[key] = node
        if len(self.hash_table) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.hash_table[node.key]
        
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)