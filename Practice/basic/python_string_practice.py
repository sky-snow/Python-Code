#coding=utf-8
# 1. Write a Python program to calculate the length of a string.
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))
# len()

# 2. Write a Python program to count the number of characters (character frequency) in a string
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        print(keys)
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a 
#    given a string. If the string length is less than 2, return instead of the empty string
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
# 4. Write a Python program to get a string from a given string where all occurrences of its 
#    first char have been changed to '$', except the first char itself.
def change_char(str1):
  char = str1[0]
  length = len(str1)
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('restart'))
print('restart'.replace('r','$'))
# 5. Write a Python program to get a single string from two given strings, 
#    separated by a space and swap the first two characters of each string
def change_two_char(str1,str2):
	return str2[:2]+str1[2:],str1[:2]+str2[2:]

str1='abc'
str2='xyz'
print(change_two_char(str1,str2))
# 6.编写一个Python程序，在给定的字符串的末尾添加'ing'（长度应至少为3）。
# 如果给定的字符串已经以“ing”结尾，则添加“ly”。如果给定字符串的字符串长度小于3，请保持不变。
def add_str(str1):
	if len(str1)<3:
		return str1
	elif str1[-3:]=='ing':
		return str1+'ly'
	else:
		return str1+'ing'

print(add_str('a'))
print(add_str('aing'))
print(add_str('abc'))
# 7.编写一个Python程序，从给定的字符串中查找子字符串“not”和“poor”的第一个外观，
#   如果“bad”跟随“poor”，将整个“not”...“差”子字符串替换为'好'。返回结果字符串。
def not_poor(str1):
  snot = str1.find('not')
  sbad = str1.find('poor')
  if sbad > snot:
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')
  return str1

print(not_poor('The lyrics is not that poor!'))

# 8.编写一个Python函数，其中列出了一个单词并返回最长的一个。
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
        print(word_len)
    word_len.sort()
    print(word_len )
    return word_len[-1][1]
              
print(find_longest_word(["PHP", "Exercises", "Backend"]))

# students = [(15,'john', 'A'), (12,'jane', 'B'), (10,'dave', 'B')]
# students.sort()
# print(students)
# students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),] 
# students.sort()
# print(students)

# 9.编写一个Python程序，从非空字符串中删除第n 个索引字符
def del_index_char(str1,n):
	if str1 != '':
		return 	str1[:n]+str1[n+1:]
print(del_index_char('python',3))
# 10.写Python程序给定的字符串更改为第一个和最后一个字符都被更换一个新的字符串
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]  
print(change_sring('abcd'))
print(change_sring('12345'))
# 11.编写一个Python程序来删除给定字符串的奇数索引值的字符
def del_index_odd(str1):
	return str1[0::2]

print(del_index_odd('python'))
# 12.编写一个Python程序来计算给定句子中每个单词的出现次数
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

# 13.编写一个Python脚本，它从用户那里获取输入，并将该输入显示在大写和小写的情况下
def display_up_lo():
	str1=raw_input('please input a word:')
	return str1.upper(),str1.lower()

# print(display_up_lo())

# 14.写接受一个逗号分隔的单词作为输入的序列，并打印在排序的形式（字母数字）的唯一字Python程序。
def display_sort_word():
	items = raw_input("Input comma separated sequence of words:")
	words = [word for word in items.split(",")]
	print(",".join(sorted(list(set(words)))))


# 15.编写一个Python函数来创建HTML字符串，带有围绕单词的标签
def add_tags(tag, word):
	return "<%s>%s</%s>"% (tag, word, tag)

# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

# 16.编写一个Python函数，在字符串的中间插入一个字符串
def insert_middle_char(str1,char):
	return str1[0:(len(str1)-1)/2+1]+char+str1[(len(str1)-1)/2+1:]

# print(insert_middle_char('abc','f'))

# 17.编写一个Python函数来获取由指定字符串的最后两个字符的4个副本组成的字符串（长度必须至少为2）
def get_end_of_str(str1):
	if len(str1)<2:
		return None
	else:
		return str1[-2:]*4

print(get_end_of_str('abc'))

# 18.编写一个Python函数来获取一个由指定字符串的前三个字符组成的字符串。
# 	如果字符串的长度小于3，则返回原始字符串
# 19.编写一个Python程序，在指定的字符之前获取一个字符串的最后一部分
# 20.编写一个Python函数来反转一个字符串，如果它的长度是4的倍数
# 21.编写一个Python函数将给定的字符串转换为全部大写，如果它在前4个字符中至少包含2个大写字符。
# 22.编写一个Python程序，按字典顺序对字符串进行排序
# 23.编写一个Python程序来删除Python中的换行符。
# 24.编写一个Python程序来检查一个字符串是否以指定的字符开始
# 25.编写一个Python程序来创建一个Caesar加密
# 26.编写一个Python程序来显示格式化的文本（width = 50）作为输出
# 27.编写一个Python程序来删除给定文本中所有行的现有缩进
# 28.编写一个Python程序，为字符串中的所有行添加一个前缀文本
# 29.写Python程序设定第一行的缩进。
# 30.写Python程序打印以下浮点数高达2位小数。
# 31.编写一个Python程序，将下列浮点数显示为带小数点的小数位
# 32.编写一个Python程序来打印不带小数位的下列浮点数。
# 33.写Python程序与上指定宽度的左零打印以下的整数
# 34.写Python程序上打印指定的宽度的右侧用“*”以下的整数
# 35.写Python程序，以显示用逗号分隔的数
# 36.写Python程序格式化数量与比例
# 37.写Python程序，以显示在左，右和中心宽度10的对准的数目
# 38.写一个Python程序来算子串的出现在一个字符串。
# 39.写Python程序扭转的字符串。
# 40.写Python程序扭转词语的字符串。
# 41.写Python程序从一个字符串中去除一组字符
# 42.写apython程序字符串中的计数重复字符
# 43.写Python程序打印的平方和立方符号在汽缸的矩形和体积的区域
# 44.写Python程序打印字符的索引中的字符串
# 45.写一个Python程序来检查，如果一个字符串包含字母表中的所有字母
# 46.写Python程序将字符串转换列表中。
# 47.写Python程序为小写字符串中的第n个字符。
# 48.写Python程序交换逗号和圆点的字符串。
# 49.写Python程序计算并显示给定文本的元音
# 50.写Python程序上的分隔符的最后出现分裂的字符串
