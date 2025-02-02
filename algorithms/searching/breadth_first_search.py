# In this algorithm I'll implement the breadth first search algorithm to find the closest mango seller in a network of friends.
# I'll use a dictionary to represent the network of friends and a queue to keep track of the people to check.
# for this example I'm gonna assume that whoever's name ends with an 'n' is a mango seller
from typing import Dict
from collections import deque

graph:  Dict[str,str] = {
    "tola": ["gemechu", "bekele", "selam", "dibora", "ermiyas"],
    "gemechu": ["joe", "john", "betty","fatuma"],
    "bekele": ["gebeyehu", "misgana", "shimelis"]
    }


def bsd(network: dict) ->str:
    search_queue = deque()
    search_queue += network[list(network.keys())[0]]
    while search_queue:
        person = search_queue.popleft()
        if person[-1] == "n":
            return person
        elif person in network.keys():
            search_queue += graph[person]
    return "No one in this network is a mango seller"