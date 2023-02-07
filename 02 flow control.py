

# If, if else

# %%
a = 7
b = 5

# %%
if b > a:
    print("b is greater than a") # what's happening here?

# %%
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")

# %%
# short hand "if"
print("b is greater than a") if b > a else print("a is greater than b") if a > b else print ("a and b are equal")

# %%
# using "or"
if a > b or a > c:
    print("at least one statement is true")

# %%
# using "and"
if a > b and c > b:
    print("both statements are true")

# %%
# nested "if"
if a > 1:
    print ("a is bigger than 1,")
    if a > 5:
        print("and also above 5")
    else:
        print("but not above 5")

# %%
# now let's try it again for a = 3
a = 3
if a > 1:
    print ("a is bigger than 1,")
    if a > 5:
        print("and also above 5")
    else:
        print("but not above 5")


# %%
# "for" loop

students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    print (students)

# %%
students = ["Avi","Dana","Mor","Na'ama"]
for i_student, student in enumerate(students):
    print(i_student, student)

# %%
students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    if student == "Dana":
        continue # with the continue statement we can stop the current iteration of the loop, and continue with the next:
    print (student)

# %%
students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    print (student)
    if student == "Mor":
        break # with the break statement we can stop the loop before it has looped through all the items

# %%
students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    if student == "Mor":
        break
    print(student) # exit the loop when i is "Mor", but this time the break comes before the print:

# %%
# nested loops
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
  for fruit in fruits:
    print(adj, fruit)

# %%
for num in range(6):
    print(num)

# %%
for num in range(2,6):
    print(num)

# %%
for num in range(6):
  print(num)
else:               # the "else" keyword in a for loop specifies a block of code to be executed when the loop is finished
  print("finished!")


# %%
# "while" loops
# while loop execute a set of statements as long as a condition is true
# (origin :https://www.w3schools.com/python/python_while_loops.asp)

i = 1
while i < 6:
  print(i)
  i += 1        # why do we need to increment i?

# %%
i = 1
while i < 6:
  print(i)
  if i == 3:
    break       # using "break" we can stop the loop even if the while condition is true
  i += 1

# %%
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue        # using "continue" we can stop the current iteration, and continue with the next
  print(i)

# %%
i = 1
while i < 6:
  print(i)
  i += 1
else:       # using "else" we can run a block of code once when the condition no longer is true
  print("i is no longer less than 6")