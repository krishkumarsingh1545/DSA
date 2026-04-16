# 🔍 Searching Practice Problems

> **Roadmap Phase:** 1
> **Languages:** Java · Python

---

## 📌 Problem Checklist

### Classic Binary Search
- [ ] Binary search (iterative & recursive)
- [ ] First and last occurrence of element
- [ ] Count occurrences of element in sorted array
- [ ] Search in rotated sorted array
- [ ] Find peak element in array

### Binary Search on Answer Space
- [ ] Find square root of N
- [ ] Koko eating bananas
- [ ] Allocate minimum number of pages
- [ ] Aggressive cows / magnetic balls
- [ ] Minimum days to make M bouquets
- [ ] Median of two sorted arrays

### Other Search Techniques
- [ ] Linear search with sentinel
- [ ] Ternary search
- [ ] Exponential search (for unbounded arrays)

---

## 🔑 Key Patterns

| Pattern | When to Use |
|---------|------------|
| **Classic BS** | Sorted array, find target |
| **First/Last occurrence** | Count, boundaries, ranges |
| **BS on answer** | Minimze max, maximize min |
| **Rotated array** | Two sorted halves |

## 🧠 Tips

- Binary search on answer space is a game-changer — *"If I fix the answer, can I verify it in O(n)?"*
- Off-by-one errors are the #1 bug — be precise with `lo <= hi` vs `lo < hi`
- Always think about the **monotonic property** — what's the boundary condition?
