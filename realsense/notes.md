# PythonでRealSenseが使えるようになるまで

```
# 自分の場合、~/Workspace/Libraryディレクトリ内で作業を行う
$ cd ~/Workspace/Library

# Githubからインストールに必要なデータを取得
$ git clone https://github.com/IntelRealSense/librealsense

# 取得したディレクトリに移動
$ cd librealsense

# build用のディレクトリを作成 & 移動
$ mkdir build & cd build

# cmakeコマンドでbuildに必要なMakefikeの作成
$ cmake ../ -DBUILD_PYTHON_BINDINGS=bool:true

# build開始！ -jオプションで処理に使うコア数を指定できる
$ make -j4

# インストール
$ sudo make install

# .bashrc または .zshrc などにPYTHONPATHを追記
$ echo "export PYTHONPATH=$PYTHONPATH:/usr/local/lib" >> ~/.bashrc
```

Pythonで動作確認

```
-> % python3
Python 3.8.6 (default, Mar  7 2021, 20:48:20) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyrealsense2
>>> 
```

🎉🥳

[参考](https://github.com/IntelRealSense/librealsense/issues/5275#issuecomment-555830996)

## 仮想環境で使えるようにするには

### 例:pyenvでpython3.8.6使用時:

```
-> % where python
/Users/sasa/.anyenv/envs/pyenv/shims/python
/usr/bin/python
/Users/sasa/.anyenv/envs/pyenv/shims/python
/Users/sasa/opt/anaconda3/bin/python

-> % ls ~/.anyenv/envs/pyenv/versions/3.8.6/lib/python3.8
# 多分ここに配置すればいいぽい

# 一旦/usr/local/lib/に移動して、中身の確認
-> % ls /usr/local/lib/ | grep py              
pybackend2.2.32.1.cpython-37m-darwin.so
pybackend2.2.cpython-37m-darwin.so
pybackend2.cpython-37m-darwin.so
pyrealsense2.2.32.1.cpython-37m-darwin.so
pyrealsense2.2.32.cpython-37m-darwin.so
pyrealsense2.cpython-37m-darwin.so
python3.7
# ここにあるのは3.7のやつっぽい?→sudo make install 時のlogをみてみる

-----
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pybackend2.2.42.0.cpython-38-darwin.so
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pybackend2.2.cpython-38-darwin.so
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pybackend2.cpython-38-darwin.so
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pyrealsense2.2.42.0.cpython-38-darwin.so
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pyrealsense2.2.42.cpython-38-darwin.so
-- Installing: /Library/Python/3.8/site-packages/pyrealsense2/pyrealsense2.cpython-38-darwin.so
-----
# pybackend2.cpython-38-darwin.so と pyrealsense2.cpython-38-darwin.so のリンクを貼れば良さそう

-> % cd ~/.anyenv/envs/pyenv/versions/3.8.6/lib/python3.8
-> % ln -s /Library/Python/3.8/site-packages/pyrealsense2/pybackend2.cpython-38-darwin.so pybackend2.so
-> % ln -s /Library/Python/3.8/site-packages/pyrealsense2/pyrealsense2.cpython-38-darwin.so pyrealsense2.so
```

多分、`make install`時にどこにインストールされたかわかるはず→`/usr/local/lib/`内に欲しいものがあることがわかる

[参考](https://github.com/IntelRealSense/librealsense/issues/5275#issuecomment-565902666)

## -jオプションの値はどうする？

コア数+1がいいらしい

### 参考
http://lpha-z.hatenablog.com/entry/2018/12/30/231500
https://qiita.com/ymdymd/items/312c9f554d4ffb1f8dc6

## アンインストール

buildディレクトリ内で`sudo make uninstall`

[make installしたソフトウェアをアンインストールする](https://leico.github.io/TechnicalNote/Linux/make-uninstall)
