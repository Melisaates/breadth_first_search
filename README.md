# breadth_first_search_pythonn

# Breadth First Search (BFS) Algorithm

This project contains an example of the Breadth First Search (BFS) algorithm in the Python language. The algorithm performs a breadth-first search on a graph.

## Algorithm Description

- The project uses three different colors, "black," "white," and "gray," to indicate the states of nodes.
- The working of the BFS algorithm can be summarized in the following steps:
    1. The starting node is marked as gray and added to the queue.
    2. As long as the queue is not empty, the following steps are repeated:
        - A node is removed from the queue, and operations are performed on it.
        - The neighbors of the removed node are checked.
        - If neighbors have not been visited before, they are marked as gray and added to the queue.
        - The processed node is marked as black.
    3. When all nodes are visited, the BFS process is completed.

## Usage

To run this Python code, you can follow these steps:

1. Include the `math` module in your project, which is used for mathematical operations.
2. Copy the code and run it in a Python environment.
3. You can update the `G` variable to change the example graph structure. This graph is represented using key-value pairs. Keys represent nodes, and values represent adjacent nodes.
4. The `Point` class is used to define node objects. You can customize this class according to your needs.
5. The `colors` dictionary contains RGB values of colors to determine the states of nodes. You can modify these colors to suit your requirements.
6. Run the code and observe the output of the BFS algorithm.

## Example Output

Breadfirst:
5 3 7 2 4 8

This output demonstrates that the BFS algorithm started from the "5" node and visited other nodes in a breadth-first manner.
