# 🎨 Pattern Printing Problems

> **Languages:** Java · Python
> **Purpose:** Master nested loops and logical thinking

---

## 📂 Files

| File | Pattern |
|------|---------|
| `Pattern1.c` | Right-angled triangle (stars) |
| `Pattern2.c` | Inverted right-angled triangle |
| `Pattern3.c` | Number triangle |
| `Pattern4.c` | Number pyramid |
| `Pattern5.c` | Inverted number triangle |
| `Pattern6.c` | Star pyramid (centered) |
| `Pattern7.c` | Inverted star pyramid |
| `Pattern8.c` | Diamond pattern |
| `Pattern9.c` | Half diamond |
| `Pattern10.c` | Pascal's triangle |
| `Pattern11.c` | Floyd's triangle |
| `Pattern12.c` | Butterfly pattern |

> 🔄 **Migrating to Java & Python** — Java versions go in `Java/`, Python versions go in `Python/`

---

## 🔑 Key Concepts

- **Outer loop** → controls rows
- **Inner loop(s)** → controls columns (spaces + symbols)
- **Symmetry** → for centered patterns, calculate leading spaces as `n - row`
- **Number patterns** → use row/column index to derive the number

## 🧠 Tips

- Pattern problems train your loop control — essential for DSA thinking
- Don't memorize patterns — understand the relationship between row, column, and the symbol
- Try re-creating each pattern from scratch without looking at the code
- **Java:** Use `System.out.print()` / `System.out.println()` with `String.repeat()`
- **Python:** Use string multiplication (`"*" * n`) and f-strings

---

## ✅ Status

All 12 patterns implemented ✔️ (migrating from C → Java & Python)
