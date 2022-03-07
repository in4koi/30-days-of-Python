import datetime
# List Basic W3chools

# CÁCH KHỞI TẠO LIST
# Cách 1
my_list = ["green", "blue", "yellow", "Color", "apple", "green"]  # Một list khi khai báo bình thường

# Cách 2
# Dùng từ khóa list để tạo một list
thislist = list(("apple", "banana", "cherry")) # lưu ý phải 2 cặp dấu ngoặc tròn
print(thislist)

my_list = ["green", "blue", "yellow", "Color", "apple", "green"]
# COPY LIST : SAO CHÉP CHUỖI
list1 = my_list.copy() #sao chép my_list vào list 1
print(list1)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ADD LIST ITEMS : THÊM PHẦN TỬ VÀO LIST
my_list.append("red") #.append() thêm 1 phần tử vào vị trí cuối cùng của list
my_list.extend(("pink", "orange"))  #.extend thêm nhiều phần tử vào vị trí cuối cùng của list hoặc có thể thêm mộ list, tuple, set, dic mới vào vị trí cuối cùng của list
my_list.insert(1, "cuong")  #.insert chèn phần tử vào vị trí bạn muốn trong list


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# NOTHING
print(my_list.count("green"))  #.count() Đếm  số lần phần tử đó xuất hiện trong list

# SORT LIST - SẮP XẾP LIST
# Lưu ý về  hàm .sort()
# 1.Hàm sort() không trả về một list mới được sắp xếp, mà thay đổi ngay tại chỗ đối tượng list đã gọi nó. Vì vậy bạn không nên gán kết quả trả về của list.sort() vào 1 biến vì giá trị của biến đó sẽ là None.
# 2.Hàm sort() vẫn nhận thêm từ khóa key và reverse như hàm sorted
# 3.Hàm sort() không phải là method của tuple và set, nên đối tượng thuộc kiểu này sẽ không gọi được nó
my_list.sort() #.sort() sắp xếp các phần tử theo kí chiều tăng dần (chữ in hoa đứng trước tí có cách khắc phục)
my_list.sort(reverse = True) #.sort(reverse = True) sắp xếp các phần tử theo thứ tự giảm dần
my_list.sort(key = str.lower) # key = str.lower sắp xếp lại list theo kí tự tăng đân không phân biệt chữ in hoa
my_list.reverse() #. reverse() đảo ngược lại thứ tự trong list

# sorted() - pro hơn hàm .sort()
# Cách dùng đơn giản
str1 = sorted(my_list)
print(sorted(my_list))
print(str1)
# Một ví dụ hay về sorted
# Sắp xếp string sau
a= "is2 sentence4 This1 a3"
b = a.split()
b = sorted(b, key=lambda b: b[-1])
sum1 =""
for x in b:
	sum1 += x[:-1] + " "
print(sum1[:-1])

# Giải thích key=lambda b: b[-1]
# Trước hết ở hàm sorted cho phép lấy key làm tham số để mình sắp xếp
# Thêm tham số key = len
# Len là độ dài, danh sách được sắp xếp dựa trên độ dài của phần tử, từ số thấp nhất đến cao nhất, độ dài to thì sau, bé thì được đứng trước
# Ở key=lambda b: b[-1], nó sẽ cho từng kí tự cuối cùng của từng phần tử trong list b, kí tự cuối cùng của từng phần tử ở đây là : 2 4 1 3, sắp xếp lại, 1 2 3 4 , được list mới tương ứng với phần tử chứa số được sắp xếp, ở đây là This1 is2 a3 sentenc3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# NOTHING #2
print(my_list.index("apple"))  #.index() tìm vị trí của phần tử trong list

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# REMOVE LIST ITEMS - XÓA PHẦN TỬ TRONG LIST
my_list.remove("blue") #.remove() xóa phần tử chỉ định trong list
my_list.pop(2)  #.pop() xóa phần tử thông qua vị trí của nó
del my_list[4]  # del xóa phần tử thông qua vị trí của nó

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LEN OF LIST
print(len(my_list))  #len() ỉn ra độ dài của chuỗi

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CLEAR OR DELETE LIST
my_list.clear()  #.clear() xóa toàn bộ chuỗi
del list1     # xóa toàn bộ chuỗi, sạch chuỗi, in chuỗi ra có lỗi ngay, làm chuỗi ko đc định nghĩa

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Unpacking List Items
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)



# Lưu Ý
a = [1,2,3]
b = a
b.remove(1)
print(a) # [2,3]
print(b) # [2,3]
# Giải thích:
# b sẽ chỉ là tham chiếu( cùng vị trí trong bộ nhớ ) đến a và các thay đổi được thực hiện b cũng sẽ tự động được thực hiện a.
# Tham chiếu là tên đề cập đến vị trí cụ thể trong bộ nhớ của một giá trị (đối tượng)
# Khi để b = a tức chỉ là tạo một bản sao của a trên địa chỉ ô nhớ đấy

# Cách khắc phục
# Dùng copy
a = [1,2,3]
b = a.copy()
b.remove(1)
print(a) # [1,2,3]
print(b) # [2,3]

# So sánh hai operator: is vs ==
# * is: so sánh id() của hai object
# * ==: so sánh giá trị hai object