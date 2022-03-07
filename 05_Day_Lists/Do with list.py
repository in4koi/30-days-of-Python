#ACCESS LIST ITEMS

thislist = ["apple", "banana", "cherry", "orange"]


#PHẦN TỬ ĐẦU TIÊN CỦA LIST LUÔN CÓ CHỈ SỐ LÀ 0
#Note: The first item has index 0.
print(thislist[0])     # in ra phần tử đầu tiên chỉ số của nó là 0 trong list: apple
print(thislist[1])     # ỉn ra phần tử có chỉ số 1 của list: banana. 

# Phần tử cuối của list có chỉ số -1
print(thislist[-1])    # in ra phần tử cóc chỉ số -1 cuối cùng của list: orange ==  -1 refers to the last item
print(thislist[-2])    # in ra phần tử có chỉ số -2 tính từ cuối lên của list: cherry == -2 refers to the second last item etc.


# RANGES OF INDEXES
# NOTE:  EG : Print from index 1 to index 3 ==> 1 <= x < 3
print(thislist[1:3])  # The search will start at index 1 (included) and end at index 3 (not included).  Tìm kiếm sẽ bắt đầu ở chỉ mục 1 (bao gồm) và kết thúc ở chỉ mục 3 (không bao gồm).
print(thislist[:3])   # The range will start at the first item (not include 3)   Trả về các mục từ đầu đến, nhưng KHÔNG bao gồm "orange" (-3)
print(thislist[2:])   # The range will go on to the end of the list    Trả về từ mục số 2 đến hết list

# Range of Negative Indexes
print(thislist[-3:-1])  # The range returns the items from "banana" (-3) to "cherry" (-2), not include "orange"  (-1) 


# Chia chuỗi với bước nhảy như sau:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Trước hết là Positive
print(a[0:5:1])    # 0:5 vẫn là in từ phần tử có chỉ số 0 đến chỉ số 5 (ko bao gồm 5) còn :1 ở cuối là bước đi, hay bước nhảy 1 
# Vẫn in ra là 0,1,2,3 vì bước nhảy là 1, kiểu như bắt đầu từ chỉ số 0, bước nhảy 1 là cộng 1 là in sang chỉ số 1, bước nhảy 1 tiếp là +1 = 2 in ra tiếp chỉ số 2
print(a[::])     # Kiểu in từ phần tử đầu đến phần tử cuối trong a
print(a[::2])		 # Kiểu in từ phần tử đầu đến phần tử cuối trong a nhưng có bước nhảy là 2 
# Kí tự in ra sẽ là 0,2,4,6,8,10,12
print(a[2:8:2])  # In từ từ phần tử có chỉ số = 2 đến phần tử có chỉ số = 8(không bao gồm ) với bước nhảy là 2

# Negative 
print(a[-6:-1:2])   # In từ phần tử có index -6 đến phần tử có index -1 (không bao gồm) với bước nhảy là 2

# Bước nhảy âm thì sao
# Với bước nhảy có chỉ số âm, phần tử đầu tiên in ra luôn có chỉ số -1 và từ lúc này mới bắt đầu tính bước nhảy
print(a[::-1])     # In từ phần tử đầu đến phần tử cuối với bước nhảy -1 , In ra phần tử cuối --> -1 , in ra phần tử có index -2 --> lại -1, in ra phần tử có index -3
# Đảo ngược một list và in thành: 12 ,11 ,10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1
print(a[::-2])   # In từ phần tử đầu đến phần tử cuối với bước nhảy -1 nhưng Index phần tử đầu bằng 0, bước nhảy -2 --> In ra phần tử cuối --> -2 tiếp, in ra phần tử có index -2
# Đảo ngược chuỗi nhưng bước nhảy là 2 nên in thành : 12 10 8 6 4 2 0
print(a[::-3])  # Kết quả 12 9 6 3



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#LOOP LISTS

# Cách 1
for x in thislist:
	print(x)       # phần tử x lần lượt là các phần tử trong thislist, nên dùng khi không phải làm việc với chỉ số i

# Cách 2
for i in range(len(thislist)):
	print(thislist[i])     # In ra các phần tử trong list với chỉ số index tương ứng, nên dùng khi phải làm việc với i

# Cách 3
i = 0 
while i < len(thislist):
	print(thislist[i])       # Rất ít khi dùng cách này đa số toàn dùng for
	i+=1

# Cách 4
[print(x) for x in thislist]   # Max nên dùng khi không phải làm việc với chỉ số i ==> vừa nhanh vừa tiện 1 dòng

# Cách 5, for fun
[print(i) for i in range(10)]    
[print("Em xin loi") for i in range(5)]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# List Comprehension - Danh sách hiểu - Dùng để tạo ra 1 list mới dựa trên list cũ bằng cách ngắn gọn hơn


# Without Comprehension
newlist = []
for x in thislist:
	newlist.append(x)
print(newlist)

# With  Comprehension
newlist1 = [x for x in thislist]
print(newlist1)


# Syntax:
# newlist = [expression for item in iterable if condition == True]


# With  Comprehension 1
newlist2 =  [x for x in thislist if "a" in x]     # Nếu phần tử x lần lượt trong list mà có chứa kí tự a thì được trả về để in ra màn hình
print(newlist2)


#With Comprehension 2
newlist3 = [x for x in thislist if x != "apple"]   # Trả về các giá trị trong thislist nhưng ko bao gồm phần tử apple (nếu có)
print(newlist3)

#With Comprehension 3
newlist4 = [x if x != "cherry" else "test" for x in thislist]  #Nếu có phần tử cherry thì thay thành test, nếu ko phải đó là phần tử cherry thì giữ nguyên như  ban đầu
print(newlist4)



# Conditionals for evaluating True and False in a python list comprehension
a = [1, 2, 3, 4, 5, 6]
b =  [n > 3 for n in a] # [False, False, False, True, True, True]
print(b)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



