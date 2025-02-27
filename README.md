# README - Pac-Man Ghost AI Search Project

## Introduction

This project, part of CS14003: Introduction to Artificial Intelligence, focuses on implementing search algorithms to control ghosts in a Pac-Man environment. The goal is to analyze their efficiency using BFS, DFS, UCS, and A* based on search time, memory usage, and expanded nodes.

## Project Members

- Trần Hữu Khang - 23127
- Nguyễn Văn Minh - 23127423
- Nguyễn Hữu Anh Trí - 23127130
- Lê Trung Kiên - 23127075

## Language and Libraries

**Programming Language:** Python (>=3.8)

**Required Libraries:**

- `pygame`: Handles game visualization and interaction.
- `numpy`: Efficiently manages matrix-based operations for game state representation.
- `matplotlib`: Visualizes algorithm performance through graphs and tables.
- `heapq`: Supports priority queue operations for UCS and A* search.

## Installation
- Step 1: Ensure Python 3.8 or later is installed on your system.
- Step 2: Install the required libraries using the following command:
  `pip install -r requirements.txt`

# Note: 
The `requirements.txt` file includes the following dependencies:

`pygame numpy matplotlib heapq`

If requirements.txt is not available, manually install them independently.

## Implementation Details
Each ghost is controlled by a unique search algorithm:

- Blue Ghost (BFS - Breadth-First Search): Explores nodes level by level, ensuring an optimal path but with high memory usage.
- Pink Ghost (DFS - Depth-First Search): Explores depth-first, which may be faster but can lead to suboptimal paths.
- Orange Ghost (UCS - Uniform-Cost Search): Expands the lowest-cost node first, making it useful for weighted paths but computationally expensive.
- Red Ghost (A - A-Star Search):* Uses heuristics (Manhattan Distance) to optimize search efficiency.
## Key Functionalities
# State Representation:
The Pac-Man environment is structured as a graph, where nodes represent positions in the maze.
# Ghost Behavior:
Each ghost follows its search strategy, navigating within maze constraints.
# Real-time Execution:
Ghosts continuously update paths based on Pac-Man’s movement for dynamic interactions.
## Performance Metrics
Each algorithm is assessed based on:
- Search Time: Measures execution speed.
- Memory Usage: Tracks memory consumption during execution.
- Expanded Nodes: Counts nodes visited before finding Pac-Man.
A comparative analysis is performed in different maze setups, with results illustrated through visualizations highlighting efficiency and trade-offs. 
