# 🍞 Bread First Algo



> An efficient 2D grid pathfinder powered by Python AI that visualizes the Breadth-First Search (BFS) algorithm to guarantee the absolute shortest route through any maze.


[![Language](https://shields.io)](https://python.org)
[![License](https://shields.io)](https://opensource.org)
[![Algorithm](https://shields.io)](#-how-it-works)

---

## 📸 Preview

<p align="center">
  <img src="https://i.postimg.cc/fbXTBGtW/Screenshot-2026-06-09-at-7-59-06-PM.png" width="45%" alt="Maze Generation Preview" />
  <img src="https://i.postimg.cc/m22kBpqQ/Screenshot-2026-06-09-at-7-58-34-PM.png" width="45%" alt="BFS Pathfinding Visualization" />
  
</p>

---

## 💡 Overview

**Bread First Algo** utilizes the **Breadth-First Search (BFS)** algorithm to solve complex 2D array mazes by exploring every possible path level by level. Because BFS systematically validates the closest unvisited positions first, it mathematically guarantees finding the optimal, shortest path from your starting coordinate to the destination. 
--

## ✨ Features

- **Guaranteed Shortest Path**: Employs rigorous BFS queue mechanics to ensure the truest path is found.
- **Performance Logging**: Tracks exploration step metrics and nodes visited during the search phase.
---

## 🛠️ Tech Stack & Requirements

- **Language:** 🐍 Python 3.10+
- **Core Modules:** `collections.deque,copy,deque` (for optimized $O(1)$ queue operations)
- **AI/Math Frameworks:** `numpy` (optional, for matrix transformations)

---

---

## 🧠 How it Works

1. **Queue Initialization**: The starting point is pushed into a First-In, First-Out (FIFO) queue structure.
2. **Neighbor Checking**: The algorithm checks adjacent positions (Up, Down, Left, Right) level by level.
3. **Dead-end Pruning**: Visited coordinates are logged instantly to prevent infinite looping and same calculations.
4. **Backtracking**: Once the destination node is intercepted, the code traces back the exact parent pointers to draft the final path in a array that provides the pathwayt.


<p align="center">
  <img src="https://i.postimg.cc/TwD4bz9d/Screenshot-2026-06-10-at-5-40-45-PM.png width="45%" alt="Maze Generation Preview" />
</p>

---.
