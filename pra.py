# 重複を消して、0は除外
N = 10
num = [0,5,7,10,4,0,6,10,4,13]
print("input:",num)
# for i in range(0,N):
#     print(num[i], end="")
#     print(" ", end="")

numbers=[]
# if num[0] == 0:
#     leftindex.append(num[0])

for i in num:
    if i != 0:
        numbers.append(i)
leftindex = [numbers[0]]
# print(leftindex)
# print(numbers)
print("numbers:",numbers)

# memo
# 今回は関係ないけどlistよりもsetに変換した方が、inを使ったときに計算量O(1)で済む。
# https://note.nkmk.me/python-in-basic/
# 変換するときは、``s_leftindex = set(leftindex)`

for i in range(0,len(numbers)):
    if not numbers[i] in leftindex:
        leftindex.append(numbers[i])
print("output:", leftindex)
# print(not 5 in leftindex)

# for i in range(0,10):
#     print(i)
# for i in range (0,N):
#     if leftindex.index(num[i]):
#         leftindex.append(num[i])

# print(numbers)
# print(leftindex)