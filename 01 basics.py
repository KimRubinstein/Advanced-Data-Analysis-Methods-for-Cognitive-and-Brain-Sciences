# lessons 01-03 are based on Mattan S. Ben-Shachar 
# "Practical Applications in R for Psychologists" 01-intro Github repo
# https://github.com/mattansb/Practical-Applications-in-R-for-Psychologists


# Anything after a "#" symbol is ignored by Python, so we can (and should!) use it to write comments

# %%
3 + 4 # execute a line with Ctrl + Enter
# Results of any command will appear in the "Cell Output" below

# %%
# ASSIGN a value to an object with =
# (it will now appear under "VARIABLES" section)
a = 3

# %%
# Running code with only the name of an object results in "printing" its contents:
a

# %%
# You can use the object just as you would its value:
a + 4
# Note that the value of "a" is not changed, 
# and that the results were not saved anywhere

# %%
b = 4

# %%
a + b

# %%
a * b

# %%
a = 8

# %%
c = a + b

# %%
c = a * b

# %%
c = b - a

# %%
c = B - A # Your first ERROR. Why?

# %%
c = a + b # assign without print
c          # then print


 # %%
# The variables we created above were all type "int".
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Let's look at other types of variables that we can use when writing a code.

# %%
# Strings:

# A string is a sequence of characters (Python does not have a character data type, 
# a single character is simply a string with a length of 1)

string = "sequence of characters (letters/ numbers/ symbols)"

# %%
Group1 = "77"

# %%
Group2 = "experimental"

# %%
Group1 / a # what's happened here?

# %%
# adding strings to each other
Group3 = Group1+Group2
print(Group3)

# %%
Group3 = Group1+' '+Group2
print(Group3)

# %%
# for numbers, the + character works as a mathematical operator
# what will happen if we will try to combine a string and a number using +?
new = a + Group3

# %%
# Floats:
# used for defining decimal values
a = 3.1

# %%
d = c - a

# %%
# another example is needed here

# %%
# Logical:
# TRUE/FALSE object
a > b

# %%
a = 7

# %%
a == 7

# %%
a = a == 7

# %%
a != 7

# %%
a < 10 & b > 8

# %%
a < 10 | b > 8

# %%
# "isinstance" function:
# returns "True" if the specified object is of the specified type, otherwise "False"
isinstance(a, int)

# %%
# check if a is one of the types described in the type parameter
isinstance("a", (float, int, str, list, dict, tuple))

# %%
type(a)

# %%
type(a) == type(b)

# %%
# change the type of object
a = str(a)

# %%
# back to int
a = int(a)

# %%
# Operators:

# (+)   addition  
# (-)   subtraction  
# (*)   multiplication  
# (/)   division  
# (^)   power  
# (%%)  modulo. The remainder after division. E.g., 5 %% 2  gives  1  
# (%/%) integer division. E.g., 7 %/% 3  gives  2

# %%
a + b / 2

# %%
a + (b / 2)

# %%
(a + b) / 2


# %%
# (lists, tuples and dictionaries code chuncks origin: https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python)

# %%
# List:
# a collection of ordered and changeable data

list1=[1,4,"Be'er-Sheva",6,"five"]
list2=[]  # creates an empty list
list3=list((1,2,3))
print(list1)
print(list2)
print(list3)

# %%
print(list1[4])

# %%
print(list1[-1]) # list also allow negative indexing

# %%
print(list1[1:4]) # slicing

# %%
list2=["apple","mango","banana"]
print(list1+list2) # list concatenation

# %%
# append() method adds a single item at the end of the list without modifying the original list.
list1=["apple","banana","grapes"]
print(list1)

# %%
list1.append("strawberry")   # strawberry is added to the list
print(list1)

# %%
# pop() method removes the item at the given index from the list and returns it.
list1.pop()  # removes the last element from the list
print(list1)

# %%
list1.pop()
print(list1)




# %%
# Tuple:
# an ordered and unchangeable collection of data (a constant list)
tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))
print(tuple1)
print(tuple2)
print(tuple3)

# %%
tuple2=("orange","grapes")
print(tuple1+tuple2)  # tuples can be concatenated

# %%
tuple3=(1,2,3)
print(type(tuple3))

# %%
# Dictionary:
# an unordered, changeable and indexed collection of data that stores data in key-value pairs
dict1={"key1":"value1","key2":"value2"}
dict2={}   # empty dictionary
dict3=dict({1:"apple",2:"cherry",3:"strawberry"})
print(dict1)
print(dict2)
print(dict3)

# %%
# mutable vs. immutable variables

# some variables can change their value after creation while some cannot. 
# Therefore, if a variable can change its value it is mutable in nature. 
# Otherwise, if it cannot change its value after creation it is immutable in nature. 

# Moreover, if we try to change the value of an immutable variable then the old variable destroys 
# and a new variable is created with the same name and new value. 
# Hence, mutable variables can change their state or content. Whereas immutable variables cannot change their state or content.

# (explanation origin: https://www.toppr.com/guides/computer-science/introduction-to-python/mutable-and-immutable-variables/mutable-and-immutable-variables/)

# %%
# lists are mutable
list1=["hello",1,4,8,"good"]
print(list1)

# %%
list1[0]="morning"  # assigning values ("hello" is replaced with "morning")
print(list1)

# %%
# tuples are immutable
tuple1=("good",1,2,3,"morning")
print(tuple1)

# %%
print(tuple1[0])  # accessing values using indexing

# %%
tuple1[1]="change"  # a value cannot be changed as tuples are immutable

# %%
tuple1.pop()   # a value cannot be removed as tuples cannot be modified

# %%
tuple1.append() # an item cannot be added as tuples cannot be modified

# %%
# dictionaries are also mutable
dict1={"key1":1,"key2":"value2",3:"value3"}
print(dict1.keys())  # all the keys are printed
dict1.values() # all the values are printed

# %%
dict1["key1"]="replace_one"  # value assigned to key1 is replaced
print(dict1)
print(dict1["key2"])


# %%
dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
print(dict1)

# %%
dict1.update({"veg2":"brinjal"})
print(dict1)


# %%
dict1.update({"veg3":"chilli"})  # updates the dictionary at the end
print(dict1)


# %%
dict1.pop("veg2") # what will happen now?
print(dict1)

# %%
# let's have another example
a = [5]

# %%
b = a

# %%
a[0] =7 #what will happen now?

# %%
b

# %%
a = [2] # what will happen now?

 # %%
b
