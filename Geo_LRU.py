from datetime import datetime
import os, time
from apscheduler.schedulers.background import BackgroundScheduler

# A class for an item in the cache, as a node in doubly linked list
class aNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nnext = None

class GeoLRU(object):
    def __init__(self, size, exp_time):
        # check that the input size and expire time are valid arguments
        try:
            val = int(size)
        except ValueError:
            print("The size for the cache should be a positive integer")
            
        if exp_time<=0:
            raise ValueError("The input expire time should be positive")
        
        self.nodes_map = {}
        
        self.size = size
        self.exp_time = exp_time
        self.head = None
        self.tail = None
        
        
    
    def get(self, key):
        # if the key is not found
        if key not in self.nodes_map.keys():
            return -1
        
        node_p = self.nodes_map[key]
        # when the key is the key of the head node
        if self.head == node_p:
            return node_p.value
        
        # else, change the position of the node to be the head of the map
        if self.remove_node(node_p)==-1:
            raise ValueError("The node to be removed does not exist in the map")
        self.insert_head(node_p)
        return node_p.value
    
    
    def set(self, key, value):
        # if the key exists in the map
        if key in self.nodes_map.keys():
            nodes_map[key] = value
            if self.head.key != key:
                if self.remove_node(node_p)==-1:
                    raise ValueError("The node to be removed does not exist in the map")
                self.insert_head(node_p)
        # if the cache is currently full, remove the last node in map and insert the new node at the front
        elif len(nodes_map)==self.size:
            self.end = self.end.prev
            self.end.next = None
        
        node_q = aNode(key, value)
        node_q.next = self.head
        self.head.prev = node_q
        self.head = node_q
        
        # set expire time
        scheduler = BackgroundScheduler()
        exp = datetime.utcnow().replace(tzinfo=pytz.utc) + exp_time
        scheduler.add_job(remove_node, 'date', run_date=exp, args=[self, node_q])
        
        
        
    def remove_node(self, node):
        # if there is currently no element in the map
        if len(nodes_map) == 0:
            return -1
        
        # if this node to be removed is the only element in the map
        if self.head == node:
            self.head = None
            self.tail = None
        # if the node to be removed is the tail of the map
        elif self.tail == node:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    
    def insert_head(self, node):
        # if there is currently no head in the map
        if not self.head:
            self.head = node
            self.end = node
        
        self.head.prev = node
        node.next = self.head
        self.head = node
    