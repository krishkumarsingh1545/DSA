# 🚶 Queue

> **Roadmap Phase:** 0 — Revision Sprint
> **Languages:** C · Python

---

## 🎯 Topics Covered

### Queue Implementations
- **Array-based queue** — simple and circular variants
- **Linked list-based queue** — dynamic, pointer-based
- **C:** Struct-based with front/rear pointers
- **Python:** `collections.deque` and manual implementations

### Circular Queue
- Efficient space utilization with wrap-around indexing
- `front` and `rear` pointer management
- Full vs empty conditions

### Deque (Double-Ended Queue)
- Insert and delete from both ends
- Applications: sliding window maximum

### Queue Using Two Stacks ⚠️
- Push-heavy vs pop-heavy approaches
- Amortized O(1) per operation
- *Gap to fill — make sure to implement this!*

---

## 🔑 Key Concepts

- **FIFO principle:** First In, First Out
- **Circular indexing:** `(index + 1) % capacity` to wrap around
- **BFS connection:** Queue is the backbone of Breadth-First Search
- **Priority queue preview:** Leads into heaps in Phase 3

## 🧠 Practice Tips

- Implement circular queue from scratch — tricky edge cases!
- Queue using 2 stacks is a classic interview question — master both approaches
- Connect queue knowledge to BFS traversal in graphs (Phase 4)
