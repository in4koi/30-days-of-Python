# %%


def largest_num(s, k):
    stack = [] 
    remove = len(s) - k
    for digit in s:
        while remove and stack and stack[-1] < digit:
            stack.pop()
            remove -=1
        stack.append(digit)
    while remove:
        stack.pop()
        remove -=1
    ans = "".join(stack)
    return ans if ans else "0"
    
print(largest_num("183468", 3))  # 868

# %%
def sum_recursion(num):
    if not num:
        return 0 
    return num[0] + sum_recursion(num[1:])
print(sum_recursion([i for i in range(10000)]))





# %%
# Recursion
def power_of_two(n):
    if n == 0:
        return 1
    power = power_of_two(n-1)
    return power * 2
print(power_of_two(4))




# %%
# Iteraive Solution
def power_of_two_ite(n):
    i = 0
    power = 1
    while i < n:
        power *=2
        i+=1
    return power
print(power_of_two_ite(4))


# %%
# Find the fibonacci number at kth



# %%
row=int(input("Nhap so hang ban muon tao ma tran: "))
col=int(input("Nhap so cot ban muon tao ma tran: "))

matrix=[[0 for i in range(col)] for j in range(row)]

for i in range(len(matrix)):
    print(i)
    for j in range(len(matrix[i])):
        print("Nhap phan tu thu", j+1,"dong thu", i+1,end=": ")
        matrix[i][j] = input()
        #print(matrix)
print("\n", matrix)
for m in range(row):
    print(matrix[m]) 


    
# %%
from collections import Counter
def check(num): 
    lst_height = Counter(num) 
    count_height = max(lst_height, key = lst_height.get)
    print(lst_height[count_height])
    print(count_height)
check([158,158,160,160])


# %%
def check(num): 
    count_height = num.count(num[0])
    height = num[0]
    for i in range(1,len(num)):
        if num.count(num[i]) > count_height:
            count_height = num.count(num[i]) 
            height = num[i]
    print(count_height)
    print(height)
check([160, 158, 158, 160, 159, 158, 159, 160, 158, 161])


# %%
a = 2
a-=-1
print(a)


# %%
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lst = []
        look = Counter(nums)
        for x in look:
            if look[x] == 1:
                lst.append(x)
        return lst

# %%
class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        count = 1
        sum = 0
        while count < k+1:
            if count in nums:
                sum += count+1
            else:
                sum += count
            count += 1
        return sum