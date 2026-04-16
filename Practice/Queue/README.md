# 🚶 Queue Practice Problems

> **Roadmap Phase:** 0
> **Languages:** Java · Python

---

## 📌 Problem Checklist

### Basic Queue Problems
- [ ] Implement queue using arrays
- [ ] Implement circular queue
- [ ] Implement queue using two stacks
- [ ] Implement stack using two queues
- [ ] Implement deque (double-ended queue)

### Application Problems
- [ ] First non-repeating character in a stream
- [ ] Sliding window maximum (deque approach)
- [ ] Generate binary numbers from 1 to N using queue
- [ ] Rotting oranges (BFS with queue)
- [ ] Number of islands (BFS with queue)

---

## 🔑 Key Patterns

| Pattern | When to Use |
|---------|------------|
| **BFS traversal** | Shortest path, level-order processing |
| **Deque** | Sliding window max/min problems |
| **Two-stack queue** | Amortized O(1) operations |
| **Circular queue** | Fixed-size buffer, round-robin |

## 🧠 Tips

- Queue using two stacks is asked very frequently — know both push-heavy and pop-heavy variants
- BFS problems almost always use a queue — practice connecting queue to graph traversal
- **Java:** Use `ArrayDeque<Integer>` (preferred over `Stack`/`Queue` interface + `LinkedList`)
- **Python:** Use `collections.deque` for O(1) append/popleft
