# 🔄 Sorting Algorithms

> **Roadmap Phase:** 1 — Core Foundations
> **Languages:** Java · Python

---

## 🎯 Topics Covered

### Basic Sorts (Theory & Understanding)
- **Bubble Sort** — repeated adjacent swaps, O(n²)
- **Selection Sort** — find min and place, O(n²)
- **Insertion Sort** — build sorted portion, O(n²), adaptive

### Efficient Sorts (Code Both Languages)
- **Merge Sort** — divide & conquer, O(n log n), stable
- **Quick Sort** — partition-based, O(n log n) avg, in-place
- **Java:** `Comparator<T>` for custom sort via `Arrays.sort()` / `Collections.sort()`
- **Python:** `key` parameter in `sorted()` and `.sort()`

---

## 📊 Comparison

| Algorithm | Time (Best) | Time (Worst) | Space | Stable |
|-----------|-------------|-------------|-------|--------|
| Bubble | O(n) | O(n²) | O(1) | ✅ |
| Selection | O(n²) | O(n²) | O(1) | ❌ |
| Insertion | O(n) | O(n²) | O(1) | ✅ |
| Merge | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick | O(n log n) | O(n²) | O(log n) | ❌ |

## 🔑 Key Concepts

- **Stability:** A stable sort preserves the relative order of equal elements
- **In-place:** Sorting without extra memory (Quick Sort > Merge Sort here)
- **Divide & Conquer:** Break the problem in half, solve, then combine
- **Pivot selection:** Random pivot in Quick Sort avoids worst-case

## 🧠 Practice Tips

- Focus on Merge Sort and Quick Sort — code them from scratch in both languages
- Understand when to use which sort (stable vs fast vs space-efficient)
- Sorting is a prerequisite for two-pointer and binary search problems
