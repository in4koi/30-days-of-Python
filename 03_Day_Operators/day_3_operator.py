from collections import Counter
#                                                           PYTHON OPERACTORS


# Trong Python có một số  toán tử như sau:

# Toán tử số học - Arithmetic Operators
# Toán tử quan hệ - Comparison (Relational) Operators
# Toán tử gán - Assignment Operators.
# Toán tử logic - Logical Operators.
# Toán tử Biwter - Bitwise Operators.
# Toán tử khai thác - Membership Operators.
# Toán tử xác thực - Indentity Operators.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#1. Toán tử số học - Arithmetic Operators

# Các toán tử số học được sử dụng với các giá trị số để thực hiện các phép toán thông thường
# Example
a = 5
b = 7
print(a + b)   # In ra tổng a và b 
print(a - b)   # in ra hiệu a - b
print(a * b)   # In ra tích a và b
print(a / b)   # In ra thương a / b
print(a % b)   # In ra phần dư khi a / b
print(a ** b)  # In ra kết quả dạng a có số mũ b
print(a //b)   # Làm tròn kết quả xuống số nguyên gần nhất, chẳng hạn 0.7 sẽ là 0, -0,7 sẽ là -1


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2. Toán tử quan hệ, so sánh - Comparison (Relational) Operators
# Toán tử so sánh được dùng để so sánh hai giá trị
# Ví dụ ở đây đều sẽ trả về True hoặc False (đã nói ở bài Boolean.py)
a = 5
b = 7
print(a == b)   # == : dấu bằng
print(a != b)   # != : dấu khác bằng
print(a > b)    # >  : dấu lớn hơn
print(a < b)    # <  : dấu bé hơn
print(a >= b)   # >= : dấu lớn hơn hoặc bằng
print(a <= b)   # <= : dấu bé hơn hoặc bằng


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3. Toán tử gán - Assignment Operators.
# Được sử dụng để gán giá trị cho các biến

x = 5     # Same as x = 5 - Đơn giản chỉ là gán giá trị

x += 3    # Same as x = x + 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x -= 3    # Same as x = x - 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x *= 3    # Same as x = x * 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x /= 3    # Same as x = x / 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x %= 3    # Same as x = x % 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x //= 3   # Same as x = x // 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)

x **= 3   # Same as x = x ** 3 - Tính vế phải rồi gán giá trị đó cho vế trái
print(x)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4. Toán tử logic - Logical Operators.

# and : trả về True nếu cả hai điều kiện đều đúng, chỉ cần 1 điều kiện sai thfi sai hết
# or  : trả về True khi 1 trong hai điều kiện là đúng hoặc cả hai đều đúng
# not : đảo ngược kết quả

# Example 
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))


# Lưu ý về not
# Có thể có not a == b nhưng ko bao giờ có a == not b, với a và b là kiểu boolean
# Nếu muốn ghi như trên mà không bị lỗi, chỉ có thể thêm () như sau  a == (not b)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#5.  Toán tử Biwter - Bitwise Operators. - Nhị phân các  thứ - Cần phải nắm rõ toán tử logic thì mới làm được - Nhắc lại
# Luôn nhớ

"""
-------------
# 0 là False|
# 1 là True |
-------------
"""

# Phan ki tu &: trong toán tử logic, có thể hiểu là AND - Bitwise AND operator: Returns 1 if both the bits are 1 else 0.
a = 10  # Binary: 1010
b = 4   # Binary: 0100

c = a & b
print(c)
"""a & b = 1010
            &
           0100
	     = 0000 (binary)
	     = 0 (Decimal)"""


# Kí tự | : trong toán tử logic, có thể hiều là OR - Bitwise or operator: Returns 1 if either of the bit is 1 else 0.
a = 10  # Binary: 1010
b = 4   # Binary: 0100

c = a | b
"""a & b = 1010
            |
           0100
	     = 1110 (binary)
	     = 14 (Decimal)"""
print(c)


# Kí tự ~ : trong toán từ logic, có thể hiểu là NOT - Bitwise not operator: Returns one’s complement of the number.
a = 10  # Binary: 1010
b = 4   # Binary: 0100
print(~a) # = -11 (Decmical)
# Giải thích:~a = ~1010 (binary)
"""	            = -(1010 + 1)
	            = -(1011)
	            = -11 (Decimal)"""
print(~b) # = -5 
"""Giải thích: ~b = ~0100 (binary)
   					 = -(100+1)
   					 = -(101) (binary)
   					 = -5 (Decmical) """	

# Kí tự ^ : Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
a = 5  # Binary: 101
b = 3   # Binary:011

c = a ^ b
"""a & b = 101
            ^
           011
	     = 110 (binary)
	     = 6 (Decimal)"""
print(c)

# Shift Operators
# Bitwise left shift <<
"""" Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result.
Similar effect as of multiplying the number with some power of two.
"""
x = 10 # 0000 1010 (Binary)
"""          || 
x << 1 : 0001 0100 (Binary) = 20 (Demical)
x << 2 : 0010 1000 (Binary) = 40 (Demical)

"""
c = x <<1
b = x << 2
print(c)
print(b)
# Cách tính nhẩm left shift ko cần đổi sang binary
# Example 
x = 3
b = x << 1   # Ở đây chỉ cần lấy giá trị x * 2 mũ (số lượng muốn chuyển sang trái), tức 3 * 2^1
a = x << 2   # Ở đây chỉ cần lấy giá trị x * 2 mũ (số lượng muốn chuyển sang trái), tức 3 * 2^2 
print(b)
print(a)




# Bitwise right shift >>
"""" Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. 
Similar effect as of dividing the number with some power of two.
"""
x = 10 # 0000 1010 (Binary)
"""          || 
x >> 1 : 0000 0101 (Binary) = 5 (Demical)
x >> 2 : 0000 0010 (Binary) = 2 (Demical)

"""
c = x >> 1
b = x >> 2
print(c)
print(b)

# Cách tính nhẩm right shift
# Example 
x = 3
b = x >> 1   # Ở đây chỉ cần lấy giá trị x / 2 mũ (số lượng muốn chuyển sang phải), tức 3 / 2^1, chỉ lấy phần nguyên
a = x >> 2   # Ở đây chỉ cần lấy giá trị x / 2 mũ (số lượng muốn chuyển sang phải), tức 3 / 2^2 , chỉ lấy phần nguyên
print(b)
print(a)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#5.  Toán tử khai thác - Membership Operators.
# Các toán tử thành viên được sử dụng để kiểm tra xem một chuỗi có được trình bày trong một đối tượng hay không:
# Dùng in và not in

x = ["apple", "banana"]
print("banana" in x)  # Nếu banana có trong x thì trả về True không có thì trả về False
print("banana" not in x)  # Nếu banana không có trong x thì trả về True có trong x thì trả về False


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#6. Toán tử xác thực - Indentity Operators.
# is và is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # Trả về True vì x và z cùng ô nhớ

print(x is y) # Trả về False vì x và y tuy giống nhau nhưng không cùng ô nhớ

print(x == y) # Trả về True vì x và y giống nhau, không liên quan đến ô nhớ
#Tương tự với is not

# SỰ KHÁC NHAU GIỮA == và is:
# + == là so sánh hai giá trị có giống nhau không, Giống --> True, Không giống --> False
# + is là so sánh hai giá trị có cùng ô nhớ không, cùng ô nhớ --> True, khác ô nhớ --> False, kể cả giá trị bằng nhau 

# So sánh hai operator: is vs ==
# * is: so sánh id() của hai object
# * ==: so sánh giá trị hai object


a = 120
a = list(str(a))
a.reverse()
for x in a:
    if x == "0":
        continue
    else:
        print(int(x))
print(a)
a ="aav"
print(Counter(a))


# So sánh hai operator: is vs ==
# * is: so sánh id() của hai object
# * ==: so sánh giá trị hai object