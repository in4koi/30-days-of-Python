# TUPLE
"""Một bộ tuple là một tập hợp các kiểu dữ liệu khác nhau được sắp xếp theo thứ tự và không thể thay đổi (không thay đổi được). Các bộ giá trị được viết bằng dấu ngoặc tròn, (). Khi một tuple được tạo, chúng tôi không thể thay đổi các giá trị của nó. Chúng ta không thể sử dụng các phương thức add, insert, remove trong một tuple vì nó không thể sửa đổi (có thể thay đổi). Không giống như list, tuple có ít phương thức. Các phương pháp liên quan đến bộ giá trị:

tuple (): để tạo một tuple trống
count (): để đếm số lượng của một mục được chỉ định trong một bộ
index (): để tìm chỉ mục của một mục được chỉ định trong một bộ
toán tử: để nối hai hoặc nhiều bộ và tạo một bộ mới"""


# Creat a tuples
# Empty tuple: Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()


# Tuple with initial values
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')


# Length of tuple
# Use len() method to get the lenth of a tuple
tpl = ('item1', 'item2', 'item3')
len(tpl)


# Accessing In Tuple : Đã nói quá nhiều - Phần tử đầu tiên trong tuple luôn có index = 1



# Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')



# Checking An Item in a tuple, Deleting Tupless, Joining Tuples đã quá quen thuộc, bỏ qua yayyy :))))))