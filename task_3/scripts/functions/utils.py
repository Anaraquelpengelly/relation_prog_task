import pandas as pd
import os
from collections import deque
from typing import List

# define a BFS function
def bfs(interaction_dictionary:dict , start:str):
    """finds the subgraph of a node (start) given a dictionary of all direct interactions of each node.
    Args:
        interaction_dictionary (dict): dictionary of each node's interacting nodes (keys are nodes and values are a list of corresponding interacting nodes
        start (str): the node to start the search with.

    Returns: a subgraph of interactions of the start node in order

    """
    visited = []  # List to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:  # While there are still nodes to process
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visited:  # Check if the node has been visited
            visited.append(node)  # Mark the node as visited
            # print(node, end=" ")  # Output the visited node

            # Enqueue all unvisited neighbors (children) of the current node
            for neighbor in interaction_dictionary[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue
    return visited

#define a function to save lists as csvs
def save_csv(l:List[tuple], column_name:str, filename:str, path:str):
    """
    Saves lists as CSV files.

    Args:
        l List(str): list to save
        column_name (str): wanted name for the single column
        filename (str): wanted filename of the csv
        path (str): path where the csv is to be saved

    Returns: saves list as csv

    """
    df = pd.DataFrame()
    df[column_name] = l
    df.to_csv(os.path.join(path, filename), index=False)
    print(f"{filename} saved!")

