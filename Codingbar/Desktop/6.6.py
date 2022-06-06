'''
https://leetcode-cn.com/problems/reshape-the-matrix/
複習 二維矩陣
'''


'''
實作 max() 變化版 

輸入 一列數列

輸出 最大的整數,索引值

ex
1 9 8 67 32 

67 3

-1 -9 -8 -67 -32 

儲存最大值的變數 初始值?

(1) 設值極值
    (1) float("inf") 無限大 -float("inf")無限小
    (2) 10**9               -10**9
(2) 設置串列的第一項

'''

# a = list(map(int,input().split()))
# count = 0
# b = 0
# for i in range(len(a)):
#     if a[i]>count:
#         count = a[i]
#         b = i
# print(count,b)





'''
最遙近的距離

判斷時間複雜度


(1) 暴力法

(2) 先 sort ， 再處理   O(nlogn)
    1.串列.sort()   改動原本的串列
    2.sorted(串列)  不會改動原本的串列


時間複雜度 ?
n**2    n!

2 3
n**2  >  n!

n >= 4
n**2  <  n!


不理會 常數次數
只在意 變數次數

為什麼要學會判斷時間複雜度?
(1) 時間越短越好，能知道如何改善程式碼

(2) 由時間複雜來判斷，寫出的程式碼有沒有符合出題人的規定
    由時間複雜來判斷，出題人要考的演算法 和 資料結構

EX. len(a) == 1000 => 1000*1000 => 10**6
len(a) == 10000 => 10000*10000 => 10**8
今天 oj 有時間上的規定， 原則上 c c++ : 1s， py : 3s
c/c++/py : 10**6~7  基準判斷

'''
# (1) O(n**2) 一組測資
# n=int(input())

# for i in range(n):
#     a=input().split()   #O(1)
#     a=list(map(int,a))  #O(1)
#     c=float("inf")      #O(1)

#     for j in range(len(a)): #O(n)   
#         for i in range(j+1,len(a)): #O(n)   O(n**2)
#             if abs(a[i]-a[j])<c: #O(1)
#                 c=a[i]-a[j] #O(1)

#     print(c)

# (2) O(n**2) 
# n = int(input())

# for i in range(n):
#     a = list(map(int,input().split()))
#     c = 10**34000

#     a.sort()

#     for j in range(len(a)-1):   # O(n)
#         if a[j+1]-a[j]<c:
#             c = a[j+1]-a[j]
#     print(c)


'''
Bubble sort
時間複雜度 O(n**2)

    排序數列 

ex  產生隨機數列

import random   #匯入 模組
a = []
for i in range(5):
    a.append(random.randint(1,30))  #random.randint(1,30) 產生1 ~ 30 數字

print(a)
'''
import random
a = []
for i in range(5):
    a.append(random.randint(1,30))
print(sorted(a))    #用sorted()來排序 跟 下面寫的程式碼 做比對
for k in range(len(a)-1): #len(a) * (len(a) - 1)  O(n*(n-1)) => O(n**2)
    for j in range(len(a)-1-k):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]=temp
print(a)


'''
B. WeirdSort
泡沫排序思維實戰
https://codeforces.com/problemset/problem/1311/B

題目翻譯
https://www.luogu.com.cn/problem/CF1311B


[[1,2,3,4]]

1 3 5 7 9


13256
13311

12 321 12 213 


6
3 2     n , m
3 2 1   a   a[1] a[2] 2 3 1     a[1] a[2] 1 2 3
1 2     p   a[2] a[3] 2 1 3  
4 2
4 1 2 3     2 3     3 4
3 2
5 1
1 2 3 4 5
1
4 2
2 1 4 3
1 3
4 2
4 3 2 1
1 3
5 2
2 1 2 3 3
1 4


YES
NO
YES
YES
NO
YES
'''
# n = int(input())
# for m in range(n):
#     b = list(map(int,input().split()))
#     a = list(map(int,input().split()))
#     p = list(map(int,input().split()))
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#     a.sort()

#     for j in range(len(p)):
#         for i in range(len(p)):
#             if c[p[i]-1]>c[p[i]]:
#                 temp = c[p[i]-1]
#                 c[p[i]-1]=c[p[i]]
#                 c[p[i]]=temp
#     # print(c)
#     # print(a)
#     if c!=a:
#         print("NO")
#     elif c==a:
#         print("YES")

a = [2,3,4,5]
a = a.sort()
print(a)



'''
檢查有沒有走過

append(索引直的方式)
缺點: 事後再查詢這個索引直的時候，
    所需的時間複雜度 會根據你走路的數量決定 O(n)


O(1)
建立一個新的 複製版的串立
設定 初始值為 0

在電腦的世界裡，只要知道地址 時間複雜度 O(1)


'''

'''
None : 空
a = [2,3,4,5]
a = a.sort()
print(a)



串列.index(data)

大到小
a = [2,6,7,3,1]
a.sort(reverse = True)
b = sorted(a,reverse =  True)
print(b)

#數對排序
a = [[1,2],[1,4],[1,4,5],[1,4,4]]
a.sort()
print(a)


a = ['a','r','s','h']
a.sort()
print(a)

每一個文字，會用一個數字來代表他，ascii


如何獲得 字元 的 ascii
ord()
a = ['a','r','s','h']
a.sort()
for i in a:
    print(ord(i))

#判斷英文字母的方法
a = ord("a")
b = ord("z")

c = ord("A")
d = ord("Z")

string = input()
for i in string:
    if a <= ord(i) <= b or c <= ord(i) <= d:
        pass
    else:
        print(False)
        break
else:
    print(True)


盡量用內建的函式，


logn:
n = 4
logn = 2
n = 8 
logn = 3

logn < n
n*logn  < n*n


'''

a = list(map(int,input().split()))
b = []
e = []
ii =0
jj =0
g = False
f = 0
count = 10**9
dire = [[-1,0],[1,0],[0,-1],[0,1]]
for i in range(a[0]):
    c = list(map(int,input().split()))
    b.append(c)
d = [[0]*a[1] for i in range(a[0])]
for i in range(a[0]):
    for j in range(a[1]):
        if b[i][j]<count:
            count = b[i][j]
            x = i
            y = j
d[x][y]=1
while True:
    count = 10**9
    for k in range(len(dire)):
        now_i=x+dire[k][0]
        now_j=y+dire[k][1]
        if 0<=now_i<a[0] and 0<=now_j<a[1]:
            if b[now_i][now_j]<count and d[now_i][now_j]!=1:
                g = True
                count = b[now_i][now_j]
                ii = now_i
                jj = now_j

    if g==False:
        break 

    x = ii
    y = jj   
    d[x][y]=1
    g = False
for i in range(a[0]):
    for j in range(a[1]):
        if d[i][j]==1:
            f+=b[i][j]
print(f)














'''
字母變大寫 字串.upper()
字母變小寫 字串.lower()


https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/

「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


text = "Leetcode is cool"
text = text.split()
text = text.lower()
text = "Leetcode is cool"
text = text.lower()
print(text)
'''
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text = text.lower()
#         text = text.split() 
#         for i in range(len(text)):
#             text[i] = [len(text[i]),i,text[i]]
#         text.sort()
#         ans = ""
#         print(text[0][1])
#         text[0][2] = text[0][2][0].upper() + text[0][2][1:]
#         for i in text[:-1]:
#             ans += i[2] + " "
#         ans += text[-1][2]
                
#         print(ans)
        
#         return ans
text = "Keep calm and code on"
text = list(text.split())
ans = ""
for j in range(len(text)):
    for i in range(len(text)-1):
        if len(text[i])>len(text[i+1]):
            temp = text[i]
            text[i]= text[i+1]
            text[i+1]=temp
for i in range(len(text)):
    if i==0:
        text[i]=text[i][0].upper()+text[i][1:]
    else:
        text[i]=text[i].lower()
    ans+=text[i]
    ans+=" "
print(ans)





