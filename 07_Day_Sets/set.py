# Day 07 - SET

# Set is a collection of items. 
# Let me take you back to your elementary or high school Mathematics lesson.
# The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements.
# In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.



# CREATING A SET
# We use curly brackets, {} to create a set or the set() built-in function.

# 1.Creating an empty set
# syntax
st = {}
# or
st = set()

# Creating a set with initial items
#syntax
st = {'item1', 'item2', 'item3', 'item4'}
# Example:
fruits = {'banana', 'orange', 'mango', 'lemon'}


# 2. Getting Set's Length - Use len() method
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))


# 3. Accessing Items in a Set
# We use loops to access items. We will see this in loop section
st = {1, 2,3,4}
for x in st:
	print(x)

# 4. Checking an item in set - Làm như bình thường, dùng in thôi là được
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True



# 5. Adding an item to set 
# Dùng add() method - Chỉ dùng add() khi đó là set - Chỉ thêm được 1 phần tử - Giống append() của list
st = {1,2}
st.add(3)
print(st)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument. - Có thể thêm 1 hoặc nhiều element
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5']) # lưu ý phải là list
print(st)





# 6. Remove an item from a set
# Dùng remove() giống như trong list
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')



# Dùng pop() - Khác với list, pop trong set sẽ xóa một phần tử bất kì, không giống như xóa phần tử của cùng của list
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set




# 7. Clearing a set
# Using clear method
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()


# 7. Delete a set
# Using a del operator
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits




# 8. Convert list to set
# Syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}  - Do những phẩn tử trùng nhau sẽ xóa bớt, chỉ để lại 1 phần tử trong số các phần tử trùng nhau đó




# 9. Joining sets
# Cái này khá giống với update(), nhưng không cần ngoặc [] - Dùng union
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# Cách dùng update không cần []
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}




# 10. Finding Intersection Items - Sơ sơ là tìm phần tử giống nhau giữa hai set - Khá hay - Có thể áp dụng trên leetcode nhiều thứ
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'}



# 11. Checking subset  - Kiểm tra set này có là tập con của set kia hay không
# Checking superset - Kiểm tra set này có chứa đủ hết các phần tử của set khác hay không
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False




# 12. Checking the difference Between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() - Do các phần tử trong st2 đều có trong st1 nên nó không khác nhau
st1.difference(st2) # {'item1', 'item4'} => st1\st2



# 13. Finding Symmetric Difference Between Two Sets
# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets,
# except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}




# 14. Joining sets - If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False


# Example 
odd_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


