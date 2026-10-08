count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
# Fixed by adding a colon after the condition.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original condition count < 5 stopped the loop before adding 5.
# Fixed by changing it to count <= 5.

# BUG: A string cannot be concatenated directly with an integer.
# Fixed by converting total to a string using str(total).
print("Sum of 1 to 5 is: " + str(total))