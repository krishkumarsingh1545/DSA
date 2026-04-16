# 📚 Stack

> **Roadmap Phase:** 0 — Revision Sprint
> **Languages:** Java · Python

---

## 🎯 Topics Covered

### Stack Implementations
- **Array-based stack** — fixed size, O(1) push/pop
- **Linked list-based stack** — dynamic size, reference-based
- **Java:** Manual implementation with class/array, `Stack<T>`, `Deque<T>` as stack
- **Python:** Using `list` as stack (`append`/`pop`)

### Monotonic Stack
- Monotonic increasing and decreasing stacks
- Intuition: maintaining order for efficient lookups
- Applications: next greater element, stock span

---

## 🔑 Key Concepts

- **LIFO principle:** Last In, First Out
- **Stack overflow/underflow:** Handle boundary conditions
- **Call stack:** Understanding recursion through the stack frame
- **Monotonic stack pattern:** Solve O(n²) problems in O(n)

## 📌 Common Problems

| Problem | Technique |
|---------|-----------|
| Balanced parentheses | Stack matching |
| Next greater element | Monotonic stack |
| Min stack | Auxiliary stack or pair storage |
| Infix to postfix | Operator precedence + stack |
| Stock span problem | Monotonic stack |

## 🧠 Practice Tips

- Implement both array and linked-list versions from scratch
- Trace through the call stack manually for recursive functions
- Monotonic stack is a must-know pattern — practice at least 5 problems
