## Infix → Postfix Conversion Using Stack (Python)

This is a **classic stack application** used in compilers and expression evaluation. The idea is to use a **stack to temporarily hold operators** while scanning the infix expression.

Example
Infix:

```
A + B * C
```

Postfix:

```
A B C * +
```

---

# Algorithm

1. Create an **empty stack** for operators.
2. Create an **empty list/string for output**.
3. Scan the infix expression **from left to right**.
4. For each symbol:

   * **Operand (A, B, 1, 2, etc.)** → add to output.
   * **'('** → push to stack.
   * **')'** → pop from stack to output until '(' is found.
   * **Operator (+, -, *, /)**

     * Pop operators from stack with **higher or equal precedence**.
     * Push current operator to stack.
5. After scanning expression, **pop remaining operators** to output.

---

# Operator Precedence

| Operator | Precedence |
| -------- | ---------- |
| `^`      | 3          |
| `* /`    | 2          |
| `+ -`    | 1          |

---

# Full Python Program

```python
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = ""

    for char in expression:
        
        # If operand → add to output
        if char.isalnum():
            output += char

        # If '(' → push to stack
        elif char == '(':
            stack.append(char)

        # If ')' → pop until '('
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        # If operator
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output += stack.pop()
            stack.append(char)

    # Pop remaining operators
    while stack:
        output += stack.pop()

    return output


# Example
expr = "A+B*(C-D)"
result = infix_to_postfix(expr)

print("Infix Expression :", expr)
print("Postfix Expression :", result)
```

---

# Output

```
Infix Expression : A+B*(C-D)
Postfix Expression : ABCD-*+
```

---

# Step-by-Step Example

Expression

```
A + B * (C - D)
```

| Symbol | Stack   | Output  |
| ------ | ------- | ------- |
| A      |         | A       |
| +      | +       | A       |
| B      | +       | AB      |
| *      | + *     | AB      |
| (      | + * (   | AB      |
| C      | + * (   | ABC     |
| -      | + * ( - | ABC     |
| D      | + * ( - | ABCD    |
| )      | + *     | ABCD-   |
| End    |         | ABCD-*+ |

---

# Time Complexity

* **O(n)** where *n = length of expression*

# Space Complexity

* **O(n)** (stack storage)

## TODO:
Write a python program to demonstrate infix expression processing using stack