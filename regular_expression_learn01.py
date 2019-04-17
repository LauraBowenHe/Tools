# -*- coding: utf-8 -*-
"""
All contents From: https://www.w3cschool.cn/python/python-reg-expressions.html
Created on Wed Apr 17 11:32:05 2019

@author: bwhe
"""

import re


# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
"""
@pattern: regular expression
@flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""

#re.match(pattern, string, flags=0)


line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
   
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
   

# re.sub() 返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。
# 可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 电话号码是:  2004-959-559
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
# 电话号码是 :  2004959559

# re.sub(pattern, repl, string)
# repl参数是一个函数
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


# re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
# re.compile(pattern, flags)
"""
参数：

pattern : 一个字符串形式的正则表达式
flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
"""

pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)                                         # 返回一个 Match 对象
# <_sre.SRE_Match object at 0x10a42aac0>
print(m.group(0))   # 可省略 0
# '12'
print(m.start(0))   # 可省略 0
# 3
print(m.end(0))     # 可省略 0
# 5
print(m.span(0))    # span([group]) 方法返回 (start(group), end(group))。可省略 0 
# (3, 5)


# findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有
# findall(string, pos, endpos)
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('school 123 google 456')
result2 = pattern.findall('sch88ool123google456', 0, 10)

print(result1) # ['123', '456']
print(result2) # ['88', '12']


#re.finditer(pattern, string, flags=0)
#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group())
  
    
#re.split(pattern, string, maxsplit=0, flags=0)
#split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下
#maxsplit: 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数
#\w: 匹配字母数字
#\W: 匹配非字母数字
re.split('\W+', 'w3cschool, w3cschool, w3cschool.')
re.split('(\W+)', ' w3cschool, w3cschool, w3cschool.') 
re.split('\W+', ' w3cschool, w3cschool, w3cschool.', 1) 
re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割,['hello world']