# 🍞 Bread First Algo

> An efficient 2D grid pathfinder that uses the ManHattan distance protocol to determine the quickest route through a single run.


---

## 📸 Preview

<p align="center">
  <img src="https://www.kodeclik.com/assets/manhattan-distance-formula.webp" width="45%" alt="Maze Generation Preview" />
  <img src="https://i.postimg.cc/NfSQvczz/Screenshot-2026-06-10-at-5-29-52-PM.png" width="45%" alt="BFS Pathfinding Visualization" />
</p>

---

## 💡 Overview

** Greedy Bread First Algo** prioritizes efficent results over stable ones. The Greedy BFS algo is made to produce results rapidly and sloving any task at hand in one go. This is used to get results in a rapid pace under a strict deadline.
---

## ✨ Features

- **Guaranteed path under a few Miliseconds (IF POSSIBLE TO SLOVE) **: Employs rigorous BFS queue mechanics to ensure the quickest path is found.
- **Performance Logging**: Tracks exploration step metrics and nodes visited during the search phase.
- **Results produced rapidly** - BFS Greedy algo is made for this.
---

## 🛠️ Tech Stack & Requirements

- **Language:** 🐍 Python 3.10+
- **Core Modules:** `collections.deque, priority queue, list` (for optimized $O(1)$ queue operations)
- **AI/Math Frameworks:** `numpy,random` (optional, for matrix transformations)


---

## 🧠 How it Works

1. **Queue Initialization**: The starting point is pushed into a priority queue from distance from current node to goal using manahattan distance.
2. **Neighbor Checking**: The algorithm checks adjacent positions (Up, Down, Left, Right) level by level
3. **Dead-end Pruning**: Visited coordinates are logged instantly to prevent infinite looping and same calculations.
4. **Backtracking**: Once the destination node is intercepted, the code traces back the exact parent pointers to draft the final path in a array and live chart to show the pathway it took.


<p align="center">
  <img src="https://i.postimg.cc/TwD4bz9d/Screenshot-2026-06-10-at-5-40-45-PM.png width="45%" alt="Maze Generation Preview" />
</p>

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.


