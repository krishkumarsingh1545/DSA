# 📚 Stack Practice Problems

> **Roadmap Phase:** 0 & 6
> **Languages:** Java · Python

---

## 📌 Problem Checklist

### Basic Stack Problems
- [ ] Valid parentheses (balanced brackets)
- [ ] Implement stack using arrays
- [ ] Implement stack using linked list
- [ ] Min stack — O(1) getMin()

### Monotonic Stack
- [ ] Next greater element
- [ ] Next smaller element
- [ ] Largest rectangle in histogram
- [ ] Stock span problem
- [ ] Trapping rain water

### Expression Evaluation
- [ ] Infix to postfix conversion
- [ ] Evaluate postfix expression
- [ ] Infix to prefix conversion

---

## 🔑 Key Patterns

| Pattern | When to Use |
|---------|------------|
| **Matching brackets** | Any open/close pairing problem |
| **Monotonic increasing** | Next smaller element |
| **Monotonic decreasing** | Next greater element |
| **Two stacks** | Implement queue, min stack |

## 🧠 Tips

- Monotonic stack problems appear frequently in interviews — practice until intuitive
- Always think about what the stack *represents* (pending items? open brackets?)
- Histogram problem is a classic — connects to trapping rain water
- **Java:** Use `Deque<Integer> stack = new ArrayDeque<>()` (preferred over `Stack<T>`)
- **Python:** Use `list` with `append`/`pop` for O(1) stack operations
