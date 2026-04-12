# 🔍 Searching Algorithms

> **Roadmap Phase:** 1 — Core Foundations
> **Languages:** C · Python

---

## 🎯 Topics Covered

### Binary Search — Core Template
- **lo / hi / mid pattern** — the universal binary search template
- Iterative and recursive implementations
- Condition: array must be sorted (or search space must be monotonic)

### Binary Search on Arrays
- Search for target in sorted array
- First and last occurrence of an element
- Search in rotated sorted array
- Find peak element

### Binary Search on Answer Space
- Binary search isn't just for arrays — apply it on the answer!
- Minimize the maximum / maximize the minimum patterns
- Examples: allocate books, aggressive cows, Koko eating bananas

---

## 🔑 Key Concepts

- **Time complexity:** O(log n) — halving the search space each step
- **lo/hi/mid template:** `mid = lo + (hi - lo) / 2` (avoids overflow in C)
- **Search on answer space:** When the answer lies in a range, binary search on it
- **Monotonic condition:** Binary search works whenever there's a clear boundary

## 📌 Common Problems

| Problem | Type |
|---------|------|
| Search in sorted array | Classic BS |
| First/last occurrence | Modified BS |
| Rotated sorted array | Two-part BS |
| Square root of N | BS on answer |
| Allocate minimum pages | BS on answer |
| Koko eating bananas | BS on answer |

## 🧠 Practice Tips

- Master the lo/hi/mid template — it's the foundation for every BS problem
- Always think: *"Can I binary search on the answer?"* before brute-forcing
- Common pitfall: off-by-one errors — be precise about `lo <= hi` vs `lo < hi`
