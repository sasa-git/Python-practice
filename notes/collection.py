data = ["apple", "orange", "banana"]
print(data)
print(data[0])
print(data[-1])

data.append("melon")
print(data)

data.remove("banana")
print(data)

### 反転
data2 = data # 参照渡し
data2.reverse()
# reverse()が返すのはNone 破壊的処理
print(data2)

data3 = reversed(data)
# reversedではlistではなくイテレータを返す 非破壊的
print(data3)

# data4 = list(reversed(data))
data4 = data
print(data4)

### スライス
data = ["apple", "orange", "banana", "melon"]
print(data[1:2])
print(data[1:4])
print(data[1:])
print(data[2:])
print(data[::-1])

data[1] = "cherry"
print(data)

### ソート
data = [85, 2, 99, 10, -5]
data.sort() # これの返り血はNone
print(data)

# タプル
data = ("apple", "orange", "banana")
print(data)

## こっちだと数値として
data = (11)
print(type(data))
## こっちだとタプルとして扱われる
data = (11,)
print(type(data))

# セット
data = {"apple", "orange", "banana"}
print(data)

data = set(["apple", "cherry", "orange"])
print(data)

data.add("melon")
print(data)

## 同じ要素を追加しても無視される
data.add("melon")
print(data)

## リスト型のようなオブジェクトはセットに追加できない
# data = {["apple", "orange"], "melon"}
# print(data)
#=>Traceback (most recent call last):
#=>  File "collection.py", line 68, in <module>
#=>    data = {["apple", "orange"], "melon"}
#=> TypeError: unhashable type: 'list'

data = {"apple", "orange", "banana"}
data.remove("banana")
print(data)

# 削除対象がない場合、KeyErrorが出力
# data = {"apple", "orange", "banana"}
# data.remove("melon")
#=>Traceback (most recent call last):
#=>  File "collection.py", line 81, in <module>
#=>    data.remove("melon")
#=>KeyError: 'melon'

## discard()で削除すると対応する要素がなくてもエラー出力されない
data = {"apple", "orange", "banana"}
data.discard("melon")
print(data)

## 重複を除外してデータを結合
data1 = {"apple", "orange", "banana"}
data2 = {"apple", "melon"}
print(data1.union(data2))

data3 = {"orange", "kiwi"}
print(data1.union(data2, data3))

## 重複している要素を抽出
data1 = {"apple", "orange", "banana"}
data2 = {"apple", "melon"}
print(data1.intersection(data2))

## 元のセットの固有な要素を抽出
data1 = {"apple", "orange", "banana"}
data2 = {"apple", "melon"}
print(data1.difference(data2))

## 両方のセットに共通でない要素を抽出
data1 = {"apple", "orange", "banana"}
data2 = {"apple", "melon"}
print(data1.symmetric_difference(data2))

## Aセット(data1)にBセット(data2)が含まれているか data1⊃data2
data1 = {"apple", "orange", "banana"}
data2 = {"apple", "orange"}
print("○", data2.issubset(data1))
print("×", data1.issubset(data2))

# 辞書 keyはハッシュ化できるものであればなんでも使える
item = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
print(item)

fruits = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
fruits["melon"] = "500"
print(fruits)
fruits["orange"] = "300"
print(fruits)
del(fruits["apple"])
print(fruits)

## pop()メソッドでも削除できる。削除時に値を取り出せる
fruits = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
data = fruits.pop("apple")
print(data)
print(fruits)

## pop()メソッドでは指定したキーが存在しなかった場合にデフォルト値として指定した値を返せる
fruits = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
data = fruits.pop("melon", "Not Found!")
print(data)
print(fruits, "(変わってない)")

### デフォルト値を指定せずに存在しないキーを削除しようとするとKeyErrorが出る
# fruits = {
#     "apple": "200",
#     "orange": "150",
#     "banana": "100",
# }
# data = fruits.pop("melon")
#=>Traceback (most recent call last):
#=>  File "collection.py", line 167, in <module>
#=>    data = fruits.pop("melon")
#=>KeyError: 'melon'

# clear()で要素を全削除
fruits = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
fruits.clear()
print(fruits)

## 辞書の全ての値を取得
fruits = {
    "apple": "200",
    "orange": "150",
    "banana": "100",
}
print(fruits.keys())
print(fruits.values())
print(fruits.items())

data = {"apple", "orange", "banana"}
print("orange" in data)
print("melon" in data)