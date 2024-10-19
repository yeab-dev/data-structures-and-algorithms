from typing import Optional
from linked_list import LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.child: Optional[LinkedList] = None