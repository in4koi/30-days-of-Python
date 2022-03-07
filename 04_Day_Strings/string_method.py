# 1. count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`


# 2. capitalize(): Converts the first character of the string to capital letter - In hoa chữ cái đầu của chuỗi
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'


# 3. endswith(): Checks if a string ends with a specified ending - Kiểm tra một chuỗi có kết thức bằng một chữ chỉ định hay không
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False


# 4. expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument - 
# Thay thế ký tự tab bằng dấu cách, kích thước tab mặc định là 8. Nó nhận đối số kích thước tab
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'


# 5. find(): Returns the index of the first occurrence of a substring, if not found returns -1 - Trả về index mà phần tử đang cần tìm, nếu không có trả về -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th')) # 17


# 6. rfind(): Returns the index of the last occurrence of a substring, if not found returns -1 - Trả về vị trí cuối cùng của phần từ đang cần tìm, không có trả về -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17


# 7. format() : Làm cho định dạng chuỗi có đầu ra đẹp hơn
first_name = 'Dang'
last_name = 'Cuong'
age = 250
job = 'student'
country = 'Viet Nam'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


# 8. index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1).
#  If the substring is not found it raises a valueError. :Trả về chỉ số thấp nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1). Nếu không tìm thấy chuỗi con, nó sẽ tạo ra một valueError.
challenge  = '30  days of python' 
sub_string  =  'da' 
print ( challenge . index ( sub_string ))   # 4 
"""print ( challenge . index ( sub_string , 9 )) # error"""


# 9. rindex(): Trả về chỉ số cao nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
"""print(challenge.rindex(sub_string, 9)) # error"""



# 10. isalnum(): Checks alphanumeric character - kiểm tra kí tự và chữ số
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False



# 11. isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z) - Kiểm tra xem tất cả các phần tử chuỗi có phải là ký tự bảng chữ cái hay không (az và AZ)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# 12. isdecimal(): Checks if all characters in a string are decimal (0-9) -  Kiểm tra xem tất cả các ký tự trong chuỗi có phải là số thập phân (0-9) không
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed


# 13. isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers) - Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số hay không (0-9 và một số ký tự unicode khác cho các số)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


# 14. isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False


# 15. isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# 16. islower: check character in string is lower case or not
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False


# 17. isupper: check character in string is upper case or not
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# 18. join() : Return a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


# 19. strip() : Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of pythoonnn     '
print(challenge.strip()) # 'thirty days of pythoonnn'



# 20. replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


# 21. split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


# 22. Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python


# 23. swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# 24. startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

num = 2932
arr = str(num).split()
arr.sort()
print(arr)
