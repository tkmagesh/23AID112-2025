
### Level 1 – Basic variables & data types (1–5)
1. Create 4 variables of different data types (integer, float, string, boolean) that describe yourself (age, height, name, are_you_student). Print all of them with nice formatting.

2. Ask the user for their birth year (as string), convert it to integer, calculate their age in 2025 and print:  
   "You will be X years old in 2025!" (X = 2025 - birth_year)

3. Create two variables: `price = 599.99` and `discount = 0.15`  
   Calculate and print the final price after discount with 2 decimal places.

4. Create a variable with your favourite number.  
   Print whether this number is even or odd (use % operator).

5. Ask user for two numbers (as strings), convert them to integers, then print:
   - their sum
   - their difference
   - their product
   - which one is bigger (or if they are equal)

### Level 2 – If statements practice (6–10)
6. Ask user for their age. Print different messages:
   - < 13 → "You are a child"
   - 13–17 → "You are a teenager"
   - 18–64 → "You are an adult"
   - ≥ 65 → "You are a senior"

7. Ask user for a number. Tell them if the number is:
   - positive
   - negative
   - zero

8. Create a simple traffic light simulator:  
   Ask user to enter "red", "yellow" or "green".  
   Print appropriate action:
   - red → "STOP!"
   - yellow → "Prepare to stop"
   - green → "You can go"
   - anything else → "Wrong input!"

9. Ask user for two exam scores (0–100).  
   Print "You passed!" if both scores are ≥ 50, otherwise "You need to retake some exams".

10. Temperature converter + advice:  
    Ask user for temperature in Celsius.  
    Convert to Fahrenheit (°F = °C × 9/5 + 32)  
    Then print advice:
    - < 0 → "Very cold! Wear thick jacket"
    - 0–15 → "Cold. Wear jacket"
    - 16–25 → "Nice weather"
    - > 25 → "Hot! Stay hydrated"

### Level 3 – Loops + Lists basics (11–20)
11. Use a for loop to print numbers 1 to 15.

12. Use a while loop to print all even numbers from 2 to 30.

13. Create a list with 6 different food names.  
    Use a for loop to print each food with numbering:
    ```
    1. Pizza
    2. Sushi
    3. ...
    ```

14. Create an empty list.  
    Use a loop to ask user 5 times to enter their favourite movies.  
    Add each movie to the list.  
    After all inputs, print the whole list.

15. Create list = [12, 45, 3, 98, 7, 34, 21]  
    Use a loop to:
    a) print each number
    b) print only numbers greater than 30
    c) count how many numbers are greater than 30

16. Create list of numbers 1–20.  
    Print only numbers that are divisible by 3 (use %).

17. Create a list with 8 random integers between 1–100.  
    Find and print:
    - the biggest number
    - the smallest number
    (without using max() / min() functions – use loop and variables)

18. Number guessing game (simple version):  
    Secret number = 7  
    Let user guess (use while loop) until they guess correctly.  
    After each wrong guess print "Too high" or "Too low".

19. Create this list:  
    ```python
    grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
    ```
    Count how many students:
    - got A (≥90)
    - got B (80–89)
    - got C (70–79)
    - got below 70

20. "Shopping list manager" mini-project:  
    Start with empty list.  
    Keep asking user what to do in a while loop:
    - "add" → ask for item name and add to list
    - "remove" → ask which item to remove (by name)
    - "show" → print current shopping list
    - "quit" → exit the program  
    (use if-elif inside while loop)

