# 🔄 Sorting Practice Problems

> **Roadmap Phase:** 1
> **Languages:** C · Python

---

## 📌 Problem Checklist

### Implement from Scratch
- [ ] Bubble sort
- [ ] Selection sort
- [ ] Insertion sort
- [ ] Merge sort
- [ ] Quick sort

### Sorting-Based Problems
- [ ] Sort an array of 0s, 1s, and 2s (Dutch National Flag)
- [ ] Merge two sorted arrays without extra space
- [ ] Merge intervals
- [ ] Sort characters by frequency
- [ ] K-th largest/smallest element

### Custom Comparators
- [ ] C: `qsort()` with custom compare function
- [ ] Python: `sorted()` with `key` parameter
- [ ] Sort array by custom criteria

---

## 🔑 Key Patterns

| Pattern | When to Use |
|---------|------------|
| **Dutch National Flag** | 3-way partitioning |
| **Merge sort logic** | Count inversions, merge intervals |
| **Quick select** | K-th element without full sort |
| **Custom comparator** | Non-standard ordering requirements |

## 🧠 Tips

- Merge sort and quick sort must be coded from memory — focus on divide & conquer intuition
- Sorting is often a preprocessing step — sort first, then apply two-pointer or binary search
- Understand stability — when does the relative order of equal elements matter?
