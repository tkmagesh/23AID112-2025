
# 1. Postfix Expression Evaluation (Using Stack)

### Idea

Postfix format:
`operand operand operator`

Example:

```
2 3 * 5 4 * + 9 -
```

### Algorithm

1. Create an empty stack.
2. Scan expression **left → right**.
3. If token is **operand**, push it into stack.
4. If token is **operator**:

   * Pop two elements from stack.
   * Apply operator.
   * Push result back.
5. Final stack value = answer.

---

### Python Implementation

```python
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack.pop()


expr = "2 3 * 5 4 * + 9 -"
print("Postfix Result:", evaluate_postfix(expr))
```

### Output

```
Postfix Result: 17
```

---

# 2. Prefix Expression Evaluation (Using Stack)

### Idea

Prefix format:
`operator operand operand`

Example:

```
- + * 2 3 * 5 4 9
```

### Algorithm

1. Create an empty stack.
2. Scan expression **right → left**.
3. If token is **operand**, push into stack.
4. If token is **operator**:

   * Pop two elements.
   * Apply operation.
   * Push result back.
5. Final stack element = answer.

---

### Python Implementation

```python
def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack.pop()


expr = "- + * 2 3 * 5 4 9"
print("Prefix Result:", evaluate_prefix(expr))
```

### Output

```
Prefix Result: 17
```

---

# 3. Visual Stack Example (Postfix)

Expression:

```
5 6 2 + * 12 4 / -
```

| Step | Stack     |
| ---- | --------- |
| 5    | [5]       |
| 6    | [5,6]     |
| 2    | [5,6,2]   |
| +    | [5,8]     |
| *    | [40]      |
| 12   | [40,12]   |
| 4    | [40,12,4] |
| /    | [40,3]    |
| -    | [37]      |

Result = **37**

---

**Key Difference**

| Feature        | Prefix                 | Postfix                |
| -------------- | ---------------------- | ---------------------- |
| Scan Direction | Right → Left           | Left → Right           |
| Stack Pops     | operand1 then operand2 | operand2 then operand1 |
| Example        | `+ 2 3`                | `2 3 +`                |

